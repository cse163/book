import os
import pathlib
import re
import unicodedata
import xml.etree.ElementTree as ET

import yaml

LESSONS_DIR = "../lesson_data"
OUTPUT_DIR = "book_source/source/"


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


class EdStemXMLVisitor:
    def __init__(self, tree, out, starting_heading_level=0):
        self.tree = tree
        self.out = out
        self.starting_heading_level = starting_heading_level

        # Formatting state
        self.print_newlines = True
        self.indent = 0
        self.skip_indents = 0

    def _print(self, text="", newline=True, force_indent=False):
        should_indent = text or force_indent
        if should_indent and self.skip_indents == 0:
            indent = "    " * self.indent
        else:
            indent = ""
            if should_indent and self.skip_indents > 0:
                self.skip_indents -= 1

        self.out.write(indent + str(text))
        if self.print_newlines and newline:
            self.out.write("\n")
        else:
            self.out.write(" ")

    def _visit_mixed_body(self, element, print_stripped=True):
        def strip_none_safe(s):
            if s:
                return s.strip() if print_stripped else s
            else:
                return s

        text = strip_none_safe(element.text)

        if text:
            self._print(text)

        for child in element:
            self.visit(child)
            if child.tail:
                child_text = strip_none_safe(child.tail)
                self._print(child_text)
        self._print()

    def start(self):
        for el in self.tree.getroot():
            self.visit(el)

    def visit(self, element):
        if element.tag == "bold":
            self.visit_bold(element)
        elif element.tag == "callout":
            self.visit_callout(element)
        elif element.tag == "code":
            self.visit_code(element)
        elif element.tag == "heading":
            self.visit_heading(element)
        elif element.tag == "italic":
            self.visit_italic(element)
        elif element.tag == "list":
            self.visit_list(element)
        elif element.tag == "paragraph":
            self.visit_paragraph(element)
        elif element.tag == "pre":
            self.visit_pre(element)
        elif element.tag == "snippet":
            self.visit_snippet(element)
        elif element.tag == "video":
            self.visit_video(element)
        else:
            self._print(element)

    def visit_bold(self, element):
        self._print(f"**{element.text}**")

    def visit_callout(self, element, print_stripped=True):
        callout_type = element.get("type")

        self._print("```{" + callout_type + "}")
        self._visit_mixed_body(element, print_stripped=print_stripped)
        self._print("```")
        self._print()

    def visit_code(self, element):
        self._print(f"`{element.text}`")

    def visit_heading(self, element):
        level = int(element.get("level"))
        level = level + self.starting_heading_level

        save_print_newlines = self.print_newlines
        self.print_newlines = False

        self._print(f"{'#' * level} ")
        self._visit_mixed_body(element)

        self.print_newlines = save_print_newlines

        self._print()
        self._print()

    def visit_italic(self, element):
        self._print(f"*{element.text}*")

    def visit_list(self, element):
        is_numbered = element.get("style") == "numbered"

        for i, item in enumerate(element.findall("list-item")):
            if is_numbered:
                self._print(f"{i + 1}. ", newline=False)
            else:
                self._print("- ", newline=False)

            self.indent += 1
            self.skip_indents = 1
            for child in item:
                self.visit(child)
            self.indent -= 1

        self._print()

    def visit_paragraph(self, element, print_stripped=True):
        save_print_newlines = self.print_newlines

        self.print_newlines = False
        self._visit_mixed_body(element, print_stripped=print_stripped)
        self.print_newlines = save_print_newlines

        self._print()

    def visit_pre(self, element):
        self._print("```text")
        self._print(element.text)
        self._print("````")
        self._print()

    def visit_snippet(self, element):
        # TODO do I need to turn py to python?
        language = element.get("language")
        language = language if language else "console"

        content = element.find("snippet-file").text

        self._print(f"```{language}")
        self._print(content)
        self._print("```")
        self._print()

    def visit_video(self, element):
        video_tag = f"""
<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="{element.get('src')}" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>"""
        self._print(video_tag)
        self._print()


def write_toc(out, ref_names, max_depth=2, caption="Contents"):
    out.write("```{toctree}\n")
    out.write("\n")
    out.write(f":maxdepth: {max_depth}\n")
    out.write(f":caption: {caption}\n")
    out.write("")

    for ref in ref_names:
        out.write(f"{ref}\n")
    out.write("```")


def main():
    with open(os.path.join(LESSONS_DIR, "modules.yaml")) as f:
        modules = yaml.safe_load(f)

    for module in modules["modules"]:
        # Make module folder
        module_path = os.path.join(OUTPUT_DIR, slugify(module["name"]))
        pathlib.Path(module_path).mkdir(exist_ok=True)

        lesson_ids = []

        for lesson in module["lessons"]:

            if "lesson" in lesson["id"]:
                lesson_ids.append(lesson["id"])

                # Make a folder for each lesson
                lesson_path = os.path.join(module_path, lesson["id"])
                pathlib.Path(lesson_path).mkdir(exist_ok=True)

                # Load lesson metadata
                with open(os.path.join(LESSONS_DIR, lesson["id"], "toc.yaml")) as f:
                    slide_info = yaml.safe_load(f)

                slide_ids = []
                for slide in slide_info:
                    if slide["type"] == "document":
                        # Use a special naming convention for the overview slide
                        is_overview = slide["id"] == "overview"
                        if is_overview:
                            title = lesson["title"]
                            slide_file_name = "index.md"
                        else:
                            slide_ids.append(slide["id"])
                            title = slide["title"]
                            slide_file_name = slide["id"] + ".md"

                        with open(os.path.join(lesson_path, slide_file_name), "w") as f:
                            f.write(f"# {title}\n")

                            tree = ET.parse(
                                os.path.join(LESSONS_DIR, lesson["id"], slide["id"])
                            )
                            visitor = EdStemXMLVisitor(
                                tree, f, starting_heading_level=1
                            )
                            visitor.start()

                lesson_index_file = os.path.join(lesson_path, "index.md")
                if os.path.exists(lesson_index_file):

                    with open(lesson_index_file, "a") as f:
                        f.write("\n")
                        f.write("\n")
                        f.write("## Table of Contents\n")
                        f.write("\n")

                        write_toc(f, slide_ids)

        with open(os.path.join(module_path, "index.md"), "w") as f:
            f.write(f"# {module['name']}\n")

            write_toc(f, [l + "/index" for l in lesson_ids])


if __name__ == "__main__":
    main()
