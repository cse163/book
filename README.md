# CSE 163: Intermediate Data Programming (Public)

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://cse163.github.io/book/)

Author: [Hunter Schafer](https://homes.cs.washington.edu/~hschafer/)

Contributors: Wen Qiu, Mitchell Estberg, Ryan Siu, Rit Shah, Apollo Zhu, Soham Pardeshi for proofreading and adding practice problems. Wen Qiu helped edit the lessons to this publicly accessible website.

This repository stores the source files for the public-facing resources for our UW course, CSE 163: Intermediate Data Programming.

## Note on Repo Structure

Much of this book was originally written in a learning tool used in our course called EdStem. EdStem allows for interactivity with code in both the readings and practice problems, which this public version is not able to provide. Since the repo that stores the original EdStem files also contains assignment solutions, we assume the directory of raw EdStem files lives outside of this repo in order to generate a new version of the site. The `scripts/generate_pages.py` script is really only necessary for our initial translation, and won't be likely used again. We leave it though for reference.

## Feedback or Spot a Bug?

If you have any feedback about the book text or structure, or you spot a bug somewhere in the book, please let us know! The best way to contact us
is to make an [GitHub Issue](https://github.com/cse163/book/issues) or to contact [Hunter Schafer](https://homes.cs.washington.edu/~hschafer/) directly.

## Contributing

This book is built with the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html) to generate HTML.

### Setup

Create a virtual environment with Python 3.8 or higher. For example, if you use Anaconda you can write:

```bash
conda create --name 163-book python=3.8
conda activate 163-book
```

Install the book theme dependencies. All of these are libraries used for themes/templating in the book. `Sphinx` is the documentation templating tool, `sphinx-book-theme` is the specific book theme, `myst-nb` changes the Sphinx langauge from rST to MyST (more similar to Markdown), and `sphinx-thebe` allows interactive notebooks in the browser.

```bash
pip install -r requirements.txt
```

### Editing the book

The book text is stored in `book_source/source`. Each MyST file (`.md`) corresponds to a single page of the book. Some pages, like the `index.md` files for the Modules don't contain any useful information other than links. Some of the book pages are Juptyer notebooks which also get converted to HTML.

Edit the book text by editing the appropriate MyST file. See [MyST's documentation](https://myst-parser.readthedocs.io/en/latest/) for syntax examples (note: it is incredibly similar to plain markdown, with some extra macros available).

The practice problem starter code and tests live in `book_source/coding_problems`.

### Rebuilding the book

#### Step 1) Update starter code zips [optional, if changing starter code]

**If you changed starter code or tests for the practice problems, you will need to do this step first, otherwise skip to the next step** The code in `book_source/coding_problems` needs to be copied to appropriate `.zip` file in the book source. To do this, run the following Python script.

```bash
python scripts/generate_pages.py

# Or
make zips
```

#### Step 2) Build HTML output

Build the new book HTML by running:

```
# From the top-most directory
jupyter-book build book_source/source

# Or with the make command
make html
```

This will rebuild the whole book into the `book_source/source/_build` directory, which might take some time depending on the change.

### Committing and pushing changes

Stage any changes to the `book_source` and push. We **do not** stage any changes to build files. Whenever we push to `main`,
GitHub Actions will build the site again and deploy it to the `gh-pages` branch.

**Special note aboute deploying:**

This will likely not matter, but is a bug we ran into a few times when setting up the book so I thought we should docunment it. T
here must be a file called `.nojekyll` in the directory wherever GitHub Pages is deployed. This file exists on the `gh-pages` branch
and should stay there by itself. If something weird happens though, check to make sure it is still there.
