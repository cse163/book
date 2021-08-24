"""
Hunter Schafer
CSE 163 A

This module shows an example of how to read files from
a directory.
"""

import os


def print_file(file_path):
    """
    Prints the file at the given path.
    Prints each line of the file on its own line of output
    """
    with open(file_path) as f:
        for line in f.readlines():
            print(line.strip())  # To remove extra new-line


def main():
    file_names = os.listdir('people')
    for file_name in file_names:
        print(file_name)
        print_file(file_name)
        print()


if __name__ == '__main__':
    main()
