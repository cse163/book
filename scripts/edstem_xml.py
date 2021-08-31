import pandas as pd
from pytablewriter import MarkdownTableWriter


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
