import json
import logging
import os
import pathlib
import re
import shutil
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

import pandas as pd
import yaml
from pytablewriter import MarkdownTableWriter

LESSONS_DIR = "../lesson_data"
OUTPUT_DIR = "book_source/source/"

IGNORE_LESSONS = [
    "lesson-28-web-scraping-not-worth-credit",
    "lesson-29-distributed-computing-not-worth-credit",
]


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
        # Kind of a gross way to simplify this visitor
        # Programmatically find if they have a method
        # for the given tag type, and if so call that
        # visit function. Otherwise just print a placeholder.
        visit_func_name = f"visit_{element.tag}"
        visit_func_name = visit_func_name.replace("-", "_")
        if hasattr(self, visit_func_name):
            visit_func = getattr(self, visit_func_name)
            visit_func(element)
        else:
            self._print(element)

    def visit_blockquote(self, element):
        if element.text:
            self._print("> " + element.text.strip())

        for child in element:
            self._print("> ", newline=False)
            self.visit(child)
            if child.tail:
                self._print("> " + child.tail.strip())

    def visit_bold(self, element):
        self._print(f"**{element.text}**")

    def visit_break(self, element):
        self._print("<br />")

    def visit_callout(self, element, print_stripped=True):
        # Get type of callout
        callout_type_translations = {
            "success": "tip",
            "info": "note",
            "warning": "warning",
            "error": "error",
        }

        callout_type = callout_type_translations[element.get("type")]

        # Print callout
        self._print()
        self._print("```{admonition} " + callout_type.capitalize())
        self._print(f":class: {callout_type}")
        self._print()

        self._visit_mixed_body(element, print_stripped=print_stripped)
        self._print("```")
        self._print()

    def visit_code(self, element):
        self._print(f"`{element.text}`")

    def visit_figure(self, element):
        img = element.find("image")
        src = img.get("src")
        alt = img.get("alt", "TODO")
        width = img.get("width")

        self._print("```{image} " + src)
        self._print(f":alt: {alt}")
        self._print(f":width: {width}")
        self._print(f":align: center")
        self._print("```")
        self._print()

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

    def visit_link(self, element):
        self._print(f"[{element.get('text')}]({element.get('href')})")

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
        self._print()

    def visit_pre(self, element):
        self._print("```text")
        self._print(element.text)
        self._print("````")
        self._print()

    def visit_underline(self, element):
        # There is no underline in MyST so we will bold instead
        self.visit_bold(element)

    def visit_snippet(self, element):
        language_translation = {
            "txt": "text",
            "c": "c",
            "py": "python",
            "py3": "python",
            "console": "console",
        }
        language = element.get("language", "console")
        language = language_translation.get(language, language)

        snippet_file = element.find("snippet-file")
        if snippet_file is not None:
            content = snippet_file.text
        else:
            content = element.text

        self._print(f"```{language}")
        self._print(content)
        self._print("```")
        self._print()

    def visit_video(self, element):
        # Have to change the /share/ of the URL to /embed
        src = element.get("src")
        src = src.replace("/share/", "/embed/")

        video_tag = f"""
<div style="position: relative; padding-bottom: 62.5%; height: 0;">
    <iframe src="{src}" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>"""
        self._print(video_tag)
        self._print()

    def visit_web_snippet(self, element):
        html_content = element.find("web-snippet-file[@language='html']")
        if "table" in html_content.text:
            table = pd.read_html(html_content.text)
            if type(table) is list:
                table = table[0]
            writer = MarkdownTableWriter()
            writer.from_dataframe(table)
            self._print()
            self._print(writer.dumps())
        else:
            self._print(html_content.text)


def write_toc(out, ref_names, max_depth=2, caption="Contents"):
    out.write("```{toctree}\n")
    out.write(f":maxdepth: {max_depth}\n")
    out.write(f":caption: {caption}\n")
    out.write("\n")

    for ref in ref_names:
        out.write(f"{ref}\n")
    out.write("```")


def save_lesson_slide(
    output_file_md,
    title=None,
    input_file_xml=None,
    input_xml_str=None,
    input_str=None,
    subtitle=None,
    sub_heading_text=None,
    mode="w",
):

    with open(os.path.join(output_file_md), mode) as f:
        if title:
            f.write(f"# {title}\n\n")
        elif subtitle:
            f.write(f"## {subtitle}\n\n")

        if sub_heading_text:
            f.write(f"{sub_heading_text}\n\n")

        if input_file_xml or input_xml_str:
            try:
                if input_file_xml:
                    tree = ET.parse(input_file_xml)
                else:  # input_xml_str
                    tree = ET.ElementTree(ET.fromstring(input_xml_str))
                visitor = EdStemXMLVisitor(tree, f, starting_heading_level=1)
                visitor.start()
            except ET.ParseError:
                logging.warning(f"XML Parse Error {input_file_xml}")
        elif input_str:
            f.write(input_str)


def save_questions(output_file_md, questions):
    def write_task():
        save_lesson_slide(
            output_file_md, input_str="\n\n**📝 Your Task**\n\n", mode="a",
        )

    for i, question in enumerate(questions):
        q_type = question["data"]["type"]
        q_title = f"Question {i}"
        if q_type in ["numerical", "short-answer", "true-false", "general"]:
            save_lesson_slide(
                output_file_md,
                subtitle=q_title,
                input_xml_str=question["data"]["content"],
                mode="a",
            )
            write_task()
            save_lesson_slide(
                output_file_md,
                input_str="Write your answer down in your own space.",
                mode="a",
            )

        else:
            logging.error("Unknown question type: %s (%s)", q_type, output_file_md)

        save_lesson_slide(
            output_file_md, input_str="\n\n", mode="a",
        )


def make_scaffold_zip(scaffold_path, output_zip_path, output_root):
    # Source: https://thispointer.com/python-how-to-create-a-zip-archive-from-multiple-files-or-directory/https://thispointer.com/python-how-to-create-a-zip-archive-from-multiple-files-or-directory/
    with zipfile.ZipFile(output_zip_path, "w") as out:
        for folder_name, _, filenames in os.walk(scaffold_path):
            for filename in filenames:
                # create complete filepath of file in directory
                file_path = os.path.join(folder_name, filename)
                # Add file to zip
                out_path = os.path.relpath(file_path, scaffold_path)
                out.write(file_path, out_path)


def main():
    with open(os.path.join(LESSONS_DIR, "modules.yaml")) as f:
        modules = yaml.safe_load(f)

    for module in modules["modules"]:
        # Make module folder
        module_path = os.path.join(OUTPUT_DIR, slugify(module["name"]))
        pathlib.Path(module_path).mkdir(exist_ok=True)

        lesson_ids = []

        for lesson in module["lessons"]:

            if "lesson" in lesson["id"] and lesson["id"] not in IGNORE_LESSONS:
                lesson_ids.append(lesson["id"])

                # Make a folder for each lesson
                lesson_path = os.path.join(module_path, lesson["id"])
                pathlib.Path(lesson_path).mkdir(exist_ok=True)

                # Load lesson metadata
                with open(os.path.join(LESSONS_DIR, lesson["id"], "toc.yaml")) as f:
                    slide_info = yaml.safe_load(f)

                # Process each slide in the lesson
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

                        output_file_md = os.path.join(lesson_path, slide_file_name)
                        input_file_xml = os.path.join(
                            LESSONS_DIR, lesson["id"], slide["id"]
                        )
                        save_lesson_slide(output_file_md, title, input_file_xml)
                    elif slide["type"] == "code":
                        slide_file_name = slide["id"] + ".md"
                        title = slide["title"]
                        slide_ids.append(slide["id"])

                        # Create a zip file with the scaffold code
                        scaffold_path = os.path.join(
                            LESSONS_DIR, lesson["id"], slide["id"], "scaffold"
                        )
                        output_zip = os.path.join(lesson_path, slide["id"] + ".zip")
                        make_scaffold_zip(scaffold_path, output_zip, slide["id"])

                        # Coding challenges have a passage file with the problem text
                        output_file_md = os.path.join(lesson_path, slide_file_name)
                        input_file_xml = os.path.join(
                            LESSONS_DIR, lesson["id"], slide["id"], "passage"
                        )

                        zip_url = os.path.relpath(output_zip, OUTPUT_DIR)
                        sub_heading_text = (
                            "{download}`Download starter code </" + zip_url + ">`"
                        )

                        save_lesson_slide(
                            output_file_md,
                            title,
                            input_file_xml,
                            sub_heading_text=sub_heading_text,
                        )
                    elif slide["type"] == "jupyter":
                        # Start by getting the ID for this slide by getting the name of the .ipynb
                        # file in this scaffold.
                        scaffold_path = os.path.join(
                            LESSONS_DIR, lesson["id"], slide["id"], "scaffold"
                        )

                        notebook_name = [
                            f for f in os.listdir(scaffold_path) if f.endswith(".ipynb")
                        ]
                        assert len(notebook_name) == 1, notebook_name
                        notebook_name = notebook_name[0]

                        # Note that we don't want the .ipynb in the slide_id
                        slide_id = os.path.join(
                            slide["id"], pathlib.Path(notebook_name).stem
                        )
                        slide_ids.append(slide_id)

                        # Make a copy of the scaffold folder in a folder with the slide name
                        output_path = os.path.join(lesson_path, slide["id"])
                        shutil.copytree(scaffold_path, output_path, dirs_exist_ok=True)

                        # Need to add a title cell at the top of the notebook for the build
                        output_notebook_path = os.path.join(output_path, notebook_name)
                        with open(output_notebook_path, "r") as f:
                            notebook = json.load(f)
                        cells = notebook["cells"]
                        cells.insert(
                            0,
                            {
                                "cell_type": "markdown",
                                "metadata": {},
                                "source": [f"# {slide['title']}"],
                            },
                        )
                        with open(output_notebook_path, "w") as f:
                            json.dump(notebook, f)
                    elif slide["type"] == "quiz":
                        slide_ids.append(slide["id"])
                        title = slide["title"]

                        # Read passage file and save it as the start of the quiz page
                        input_file_xml = os.path.join(
                            LESSONS_DIR, lesson["id"], slide["id"], "passage"
                        )
                        output_file_md = os.path.join(lesson_path, slide["id"] + ".md")

                        save_lesson_slide(output_file_md, title, input_file_xml)

                        # Read the questions (JSON) file to save each question
                        input_file_json = os.path.join(
                            LESSONS_DIR, lesson["id"], slide["id"], "questions"
                        )
                        questions = json.load(open(input_file_json, "r"))
                        save_questions(output_file_md, questions)

                # For the main page of the lesson, save a table of contents
                lesson_index_file = os.path.join(lesson_path, "index.md")
                if os.path.exists(lesson_index_file):

                    with open(lesson_index_file, "a") as f:
                        f.write("\n")
                        f.write("\n")
                        f.write("## Table of Contents\n")
                        f.write("\n")

                        write_toc(f, slide_ids, max_depth=1)

        # Write a table of contents for the module page
        with open(os.path.join(module_path, "index.md"), "w") as f:
            f.write(f"# {module['name']}\n")

            write_toc(f, [l + "/index" for l in lesson_ids])


if __name__ == "__main__":
    main()
