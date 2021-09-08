SRC_DIR=book_source/source

html:
	jupyter-book build "$(SRC_DIR)"

clean:
	jupyter-book clean "$(SRC_DIR)"

zips:
	python scripts/generate_pages.py
