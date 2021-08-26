import unittest

# Import the student's find_range function from main.py
from main import find_range


class SimpleTestCase(unittest.TestCase):
    def test_1(self):
        """ #name(Example)"""
        self.assertEqual(find_range([8, 3, 5, 7, 2, 4]), 7)

    def test_2(self):
        """ #name(One Element List)"""
        self.assertEqual(find_range([32, 32]), 1, "What happens when the min and the max is the same number?")

    def test_3(self):
        """ #name(Negative Numbers)"""
        self.assertEqual(find_range([3, 10000000, 5, -29, 4]), 10000030)

