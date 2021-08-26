"""
Start file to run all tests in the test directory
"""

import unittest


def main():
    test_loader = unittest.TestLoader()
    tests = test_loader.discover("test")
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)


if __name__ == "__main__":
    main()
