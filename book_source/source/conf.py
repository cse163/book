# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Intermediate Data Programming"
copyright = "2021, Hunter Schafer"

# The full version, including alpha/beta/rc tags
release = "0.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ["myst_parser", "myst_nb"]
extensions = [
    "myst_nb",
    "sphinx_thebe",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Suppress warnings
suppress_warnings = ["myst.header"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_title = project
html_logo = "_static/logo.png"

# -- Configuring BookTheme -------------------------------------------------
jupyter_execute_notebooks = "off"

html_theme_options = {
    "theme_dev_mode": True,
    "repository_url": "https://github.com/cse163/book",
    "repository_branch": "main",
    "path_to_docs": "book_source/source/",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
    },
    "extra_footer": 'Have feedback or spotted a bug? Please make a <a href="https://github.com/cse163/book/issues">GitHub issue</a> or contact <a href="https://homes.cs.washington.edu/~hschafer/">Hunter Schafer</a>!',
}
