# CSE 163: Intermediate Data Programming (Public)

Author: [Hunter Schafer](https://homes.cs.washington.edu/~hschafer/)

Contributors: Wen Qiu and Mitchell Estberg

This repository stores the source files for the public-facing resources for our UW course, CSE 163: Intermediate Data Programming.

## Note on Repo Structure

Much of this book was originally written in a learning tool used in our course called EdStem. EdStem allows for interactivity with code in both the readings and practice problems, which this public version is not able to provide. Since the repo that stores the original EdStem files also contains assignment solutions, we assume the directory of raw EdStem files lives outside of this repo in order to generate a new version of the site. The `generate_pages.py` script is really only necessary for our initial translation, and won't be likely used again. We leave it though for reference.

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

The book text is stored in `book_source/source`. Each MyST file (`.md`) corresponds to a single page of the book. Some pages, like the `index.md` files for the Modules don't contain any useful information other than links.

Edit the book text by editing the appropriate MyST file. See [MyST's documentation](https://myst-parser.readthedocs.io/en/latest/) for syntax examples (note: it is incredibly similar to plain markdown, with some extra macros available).

The practice problem starter code and tests live in `book_source/coding_problems`.

### Rebuilding the book

#### Step 1) Update starter code zips [optional, if changing starter code]

**If you changed starter code or tests for the practice problems, you will need to do this step first, otherwise skip to the next step** The code in `book_source/coding_problems` needs to be copied to appropriate `.zip` file in the book source. To do this, run the following Python script.

```bash
python generate_pages.py
```

#### Step 2) Build HTML output

Build the new book HTML by running:

```
# From the top-most directory
make --directory book_source github

# Or, from the book_source directory
make github
```

This will rebuild the whole book into the `docs` directory, which might take some time depending on the change.

### Committing and pushing changes

Since we are using GitHub pages, we unfortunately need to commit the generated HTML files in `docs` 😭. We recommend
making separate commits for your changes to `book_source` and then one final commit to commit all the changes to `docs`.
If you look at the repository's commit history, you will see many commits that have big changes to the `docs` folder with
the commit message

```
Docs: Bump docs
```

This is preferred to separate the "logical" changes in `book_source` from the generated changes in `docs`.

### Special Note

This will likely not matter, but is a bug we ran into a few times when setting up the book. While `docs` is
all generated files, GitHub pages requires that we have an empty file called `docs/.nojekyll` for it to function
correctly. This will likely not matter, but if you ended up deleting the whole `docs` folder, make sure you run:

```bash
touch docs/.nojekyll
```
