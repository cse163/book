import unittest

import main


class Test(unittest.TestCase):
    def helper(self, start, stop, solution):
        result = main.fun_numbers(start, stop)
        self.assertEquals(result, solution)

    def test_example_1(self):
        """
        #name(fun_numbers(2, 16\))
        """
        self.helper(2, 16, [2, 4, 5, 6, 8, 10, 12, 14, 15])

    def test_example_2(self):
        """
        #name(fun_numbers(5, 5\))
        """
        self.helper(5, 5, [])

    def test_example_3(self):
        """
        #name(fun_numbers(5, 2\))
        """
        self.helper(5, 2, [])
