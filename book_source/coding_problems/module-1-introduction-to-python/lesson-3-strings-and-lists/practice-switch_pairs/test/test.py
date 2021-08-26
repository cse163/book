import unittest

# Import the student's switch_pairs function from main.py
from main import switch_pairs


class SimpleTestCase(unittest.TestCase):
    def test_1(self):
        """ #name(Empty String)"""
        self.assertEqual(switch_pairs(""), "", "Return an empty string in the case of an empty string")

    def test_2(self):
        """ #name(Length one string)"""
        self.assertEqual(switch_pairs("m"), "m" )

    def test_3(self):
        """ #name(Even length string)"""
        self.assertEqual(switch_pairs("arrgh"), "ragrh")

    def test_4(self):
        """ #name(String with spaces)"""
        self.assertEqual(switch_pairs(" a "), "a  ", "How are you dealing with spaces in the string?")

    def test_5(self):
        """ #name(Example string 1: example)"""
        self.assertEqual(switch_pairs("example"), "xemalpe")

    def test_6(self):
        """ #name(Example string 1: hello there)"""
        self.assertEqual(switch_pairs("hello there"), "ehll ohtree")

