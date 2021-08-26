import unittest

# Import the student's find_range function from main.py
from main import count_votes


class SimpleTestCase(unittest.TestCase):
    def test_1(self):
        """ #name(Example)"""
        self.assertEqual(count_votes([1, 0, 1, 1, 2, 0]), [2, 3, 1])

    def test_2(self):
        """ #name(Only one vote)"""
        self.assertEqual(count_votes([1]), [0, 1, 0])

    def test_3(self):
        """ #name(Empty lists)"""
        self.assertEqual(count_votes([]), [0, 0, 0])
