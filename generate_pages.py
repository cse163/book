import sys
import xml.etree.ElementTree as ET


class EdStemXMLVisitor:
    def __init__(self, tree, out, starting_heading_level=0):
        self.tree = tree
        self.out = out
        self.starting_heading_level = starting_heading_level

    def _print(self, text=""):
        self.out.write(str(text))
        self.out.write("\n")

    def _visit_mixed_body(self, element, print_stripped=True):
        if element.text:
            self._print(element.text.strip() if print_stripped else element.text)

        for child in element:
            self.visit(child)
            if child.tail:
                self._print(child.tail.strip() if print_stripped else element.text)
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
        title = element.text

        self._print(f"{'#' * level} {title}")
        self._print()

    def visit_paragraph(self, element, print_stripped=True):
        self._visit_mixed_body(element, print_stripped=print_stripped)

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


def main():
    tree = ET.parse("lesson.xml")

    with open("book_source/source/out.md", "w") as f:
        f.write(f"# Title of Lesson")

        visitor = EdStemXMLVisitor(tree, f, starting_heading_level=1)
        visitor.start()


if __name__ == "__main__":
    main()
