import json
import logging
import os
import pathlib
import re
import shutil
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

import yaml

from edstem_xml import EdStemXMLVisitor

LESSONS_DIR = "../lesson_data"
OUTPUT_DIR = "book_source/source/"
CODE_DIR = "book_source/coding_problems"

IGNORE_LESSONS = [
    "lesson-28-web-scraping-not-worth-credit",
    "lesson-29-distributed-computing-not-worth-credit",
]

REGENERATE_PAGES = False
REGENERATE_ZIPS = True


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
    def write_task_header():
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
            write_task_header()
            save_lesson_slide(
                output_file_md,
                input_str="Write your answer down in your own space.",
                mode="a",
            )
        elif q_type in ["multiple-choice", "reorder"]:
            save_lesson_slide(
                output_file_md,
                subtitle=q_title,
                input_xml_str=question["data"]["content"],
                mode="a",
            )
            write_task_header()

            if q_type == "multiple-choice":
                items_property = "answers"
                if question["data"]["multiple_selection"]:
                    task_text = "Select one or more options. Write your answer down in your own space."
                else:
                    task_text = (
                        "Select one option. Write your answer down in your own space."
                    )
            else:  # q_type == "reorder"
                items_property = "items"
                task_text = "Reorder the following options. Write your answer down in your own space."

            save_lesson_slide(
                output_file_md, input_str=task_text, mode="a",
            )

            # Write options
            for j, option in enumerate(question["data"][items_property]):
                save_lesson_slide(
                    output_file_md, input_str=f"\n\n*❓ Option {j}*\n\n", mode="a",
                )
                if q_type == "multiple-choice":
                    save_lesson_slide(
                        output_file_md, input_xml_str=option, mode="a",
                    )
                else:  # q_type == "reorder"
                    save_lesson_slide(
                        output_file_md, input_str=option, mode="a",
                    )

        else:
            logging.error("Unknown question type: %s (%s)", q_type, output_file_md)

        save_lesson_slide(
            output_file_md, input_str="\n\n", mode="a",
        )


def make_scaffold_zip(scaffold_path, output_zip_path):
    # Source: https://thispointer.com/python-how-to-create-a-zip-archive-from-multiple-files-or-directory/https://thispointer.com/python-how-to-create-a-zip-archive-from-multiple-files-or-directory/
    with zipfile.ZipFile(output_zip_path, "w") as out:
        for folder_name, _, filenames in os.walk(scaffold_path):
            for filename in filenames:
                # create complete filepath of file in directory
                file_path = os.path.join(folder_name, filename)
                # Add file to zip
                out_path = os.path.relpath(file_path, scaffold_path)
                out.write(file_path, out_path)


def make_all_scaffold_zips():
    """
    Makes a zip of each directory in CODE_DIR and copies them
    to the appropriate place in the book source.
    """
    for module in os.listdir(CODE_DIR):
        module_path = os.path.join(CODE_DIR, module)
        for lesson in os.listdir(module_path):
            lesson_path = os.path.join(module_path, lesson)
            for slide in os.listdir(lesson_path):
                slide_path = os.path.join(lesson_path, slide)
                output_zip_path = os.path.join(
                    OUTPUT_DIR, module, lesson, slide + ".zip"
                )
                make_scaffold_zip(slide_path, output_zip_path)


def generate_slide(lesson, slide, lesson_path):
    if "Attending Class?" in slide["title"]:
        # Skip these slides, they aren't useful
        return None

    if slide["type"] == "document":
        # Use a special naming convention for the overview slide
        is_overview = slide["id"] == "overview"
        if is_overview:
            title = lesson["title"]
            slide_file_name = "index.md"
            slide_id = None
        else:
            slide_id = slide["id"]
            title = slide["title"]
            slide_file_name = slide["id"] + ".md"

        output_file_md = os.path.join(lesson_path, slide_file_name)
        input_file_xml = os.path.join(LESSONS_DIR, lesson["id"], slide["id"])
        save_lesson_slide(output_file_md, title, input_file_xml)
        return slide_id
    elif slide["type"] == "code":
        slide_file_name = slide["id"] + ".md"
        title = slide["title"]

        # Variables for input/output paths
        # Path to scaffold directory
        scaffold_path = os.path.join(LESSONS_DIR, lesson["id"], slide["id"], "scaffold")

        # Path to directory to store copied code files
        code_dir_path = os.path.relpath(lesson_path, start=OUTPUT_DIR)
        code_dir_path = os.path.join(CODE_DIR, code_dir_path, slide["id"])

        # Ensure the directory exists
        pathlib.Path(code_dir_path).mkdir(parents=True, exist_ok=True)

        # Make a copy of the starter files in the code directory
        shutil.copytree(scaffold_path, code_dir_path, dirs_exist_ok=True)

        # Make a test directory in the scaffold directory for the test-runner
        test_input_path = os.path.join(
            LESSONS_DIR, lesson["id"], slide["id"], "testbase"
        )
        if os.path.exists(test_input_path):
            test_output_path = os.path.join(code_dir_path, "test")
            shutil.copytree(test_input_path, test_output_path, dirs_exist_ok=True)

        # Coding challenges have a passage file with the problem text
        output_file_md = os.path.join(lesson_path, slide_file_name)
        input_file_xml = os.path.join(LESSONS_DIR, lesson["id"], slide["id"], "passage")

        # Make URL to download ZIP
        zip_url = os.path.join(lesson_path, slide["id"] + ".zip")
        zip_url = os.path.relpath(zip_url, start=OUTPUT_DIR)
        sub_heading_text = "{download}`Download starter code </" + zip_url + ">`"

        save_lesson_slide(
            output_file_md, title, input_file_xml, sub_heading_text=sub_heading_text,
        )
        return slide["id"]
    elif slide["type"] == "jupyter":
        # Start by getting the ID for this slide by getting the name of the .ipynb
        # file in this scaffold.
        scaffold_path = os.path.join(LESSONS_DIR, lesson["id"], slide["id"], "scaffold")

        notebook_name = [f for f in os.listdir(scaffold_path) if f.endswith(".ipynb")]
        assert len(notebook_name) == 1, notebook_name
        notebook_name = notebook_name[0]

        # Note that we don't want the .ipynb in the slide_id
        slide_id = os.path.join(slide["id"], pathlib.Path(notebook_name).stem)

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

        return slide_id
    elif slide["type"] == "quiz":
        title = slide["title"]

        # Read passage file and save it as the start of the quiz page
        input_file_xml = os.path.join(LESSONS_DIR, lesson["id"], slide["id"], "passage")
        output_file_md = os.path.join(lesson_path, slide["id"] + ".md")

        save_lesson_slide(output_file_md, title, input_file_xml)

        # Read the questions (JSON) file to save each question
        input_file_json = os.path.join(
            LESSONS_DIR, lesson["id"], slide["id"], "questions"
        )
        questions = json.load(open(input_file_json, "r"))
        save_questions(output_file_md, questions)
        return slide["id"]


def generate_lesson(module_path, lesson):
    if "lesson" in lesson["id"] and lesson["id"] not in IGNORE_LESSONS:
        # Make a folder for each lesson
        lesson_path = os.path.join(module_path, lesson["id"])
        pathlib.Path(lesson_path).mkdir(exist_ok=True)

        # Load lesson metadata
        with open(os.path.join(LESSONS_DIR, lesson["id"], "toc.yaml")) as f:
            slide_info = yaml.safe_load(f)

        # Process each slide in the lesson
        slide_ids = []
        for slide in slide_info:
            slide_id = generate_slide(lesson, slide, lesson_path)
            if slide_id:
                slide_ids.append(slide_id)

        # For the main page of the lesson, save a table of contents
        lesson_index_file = os.path.join(lesson_path, "index.md")
        if os.path.exists(lesson_index_file):
            with open(lesson_index_file, "a") as f:
                f.write("\n")
                f.write("\n")
                f.write("## Table of Contents\n")
                f.write("\n")

                write_toc(f, slide_ids, max_depth=1)

        return lesson["id"]


def generate_module(module):
    # Make module folder
    module_path = os.path.join(OUTPUT_DIR, slugify(module["name"]))
    pathlib.Path(module_path).mkdir(exist_ok=True)

    # Process each lesson in this module
    lesson_ids = []
    for lesson in module["lessons"]:
        lesson_id = generate_lesson(module_path, lesson)
        if lesson_id:
            lesson_ids.append(lesson_id)

    # Write a table of contents for the module page
    with open(os.path.join(module_path, "index.md"), "w") as f:
        f.write(f"# {module['name']}\n")

        write_toc(f, [l + "/index" for l in lesson_ids])


def main():
    if REGENERATE_PAGES:
        with open(os.path.join(LESSONS_DIR, "modules.yaml")) as f:
            modules = yaml.safe_load(f)

        for module in modules["modules"]:
            generate_module(module)

    if REGENERATE_ZIPS:
        # Zip up all the files in the code folder
        # Kind of weird but we do this step last so we could potentially make edits and still run this script
        make_all_scaffold_zips()


if __name__ == "__main__":
    main()
