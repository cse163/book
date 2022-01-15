import base64
import json
from logging import debug
from trace import Trace

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.addnodes import download_reference
from sphinx.util.docutils import SphinxDirective

IFRAME_CODE = """<iframe width="100%" height="{height}" src="https://www.learnwithtrace.com/playground/code?embed=true&files={params}&language=PYTHON&hideReadonlyFiles=true"></iframe>"""


def snippet_iframe_height(code):
    # All of these are guesses based on how it looks on a few examples
    #   lines = 2, height = 200px
    #   lines = 4, height = 250 px
    #   height = 150px + 25 * lines
    return str(155 + 22 * len(code)) + "px"


def create_trace_files_param(code):
    payload = {
        "version": 0,
        "files": [
            {
                "version": 0,
                "filename": "main.py",
                "directory": "src",
                "contents": code,
                "editable": True,
            }
        ],
    }
    return base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()


class TraceSnippet(SphinxDirective):
    has_content = True

    def run(self):

        code = "\n".join(self.content)
        options = {
            "params": create_trace_files_param(code),
            "height": snippet_iframe_height(self.content),
        }

        return [nodes.raw("", IFRAME_CODE.format(**options), format="html")]


class DataDownloadLinks(SphinxDirective):
    has_content = True
    # Custom fields

    def admonition_title(self):
        """
        Return the title text for the note
        """
        return None

    def prefix_content(self):
        """
        List of content lines to put before download links
        """
        return None

    def download_prefix(self):
        """
        Prefix to put in front of each child element
        """
        return None

    def postfix_content(self):
        """
        List of content lines to put after download links
        """
        return None

    def run(self):
        admonition = nodes.admonition()
        admonition += nodes.title(self.admonition_title(), self.admonition_title())

        new_content = (
            self.prefix_content()
            + [self.download_prefix() + line for line in self.content if line]
            + self.postfix_content()
        )

        self.state.nested_parse(new_content, self.content_offset, admonition)
        return [admonition]


class ReadingDataDownload(DataDownloadLinks):
    def admonition_title(self):
        """
        Return the title text for the note
        """
        return "Data"

    def prefix_content(self):
        """
        List of content lines to put before download links
        """
        return ["You can download the dataset used in this reading here:"]

    def download_prefix(self):
        """
        Prefix to put in front of each child element
        """
        return "* "

    def postfix_content(self):
        """
        List of content lines to put after download links
        """
        return []


class JupyterInfo(DataDownloadLinks):
    def admonition_title(self):
        """
        Return the title text for the note
        """
        return "Jupyter Info"

    def prefix_content(self):
        """
        List of content lines to put before download links
        """
        return [
            'Reminder, that on this site the Jupyter Notebooks are read-only and you can\'t interact with them. Click the <i class="fas fa-rocket fa-fw"></i> button above to launch an interactive version of this notebook.',
            "",
            "* With Binder, you get a temporary Jupyter Notebook website that opens with this notebook. Any code you write will be lost when you close the tab. Make sure to download the notebook so you can save it for later!",
            "* With Colab, it will open Google Colaboratory. You can save the notebook there to your Google Drive. If you don't save to your Drive, any code you write will be lost when you close the tab. You can find the data files for this notebook below:",
        ]

    def download_prefix(self):
        """
        Prefix to put in front of each child element
        """
        return "    * "

    def postfix_content(self):
        """
        List of content lines to put after download links
        """
        return [
            "",
            'You will need to run all the cells of the notebook to see the output. You can do this with hitting `Shift-Enter` on each cell or clicking the "Run All" button above.',
        ]


def download(prefix):
    def role_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
        node = download_reference(rawtext, text, reftarget=prefix + text, **options)
        return [node], []

    return role_fn


def setup(app):
    app.add_directive("jupyter-info", JupyterInfo)
    app.add_directive("reading-data", ReadingDataDownload)
    app.add_directive("snippet", TraceSnippet)
    app.add_role("rel-data-download", download("./"))
    app.add_role("static-data-download", download("/_static/data/"))

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
