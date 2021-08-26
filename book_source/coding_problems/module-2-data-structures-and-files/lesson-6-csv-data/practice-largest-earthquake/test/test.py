import unittest

import cse163_utils
import main


class Test(unittest.TestCase):
    def setUp(self):
        self._data = cse163_utils.parse('earthquakes.csv')

    def _test_helper(self, ans, *args):
        val = main.largest_magnitude(*args)
        self.assertEquals(ans, val, f'Expected {ans}, but received {val}')

    def test_example(self):
        """
        #name(Test full earthquakes.csv dataset)
        """
        self._test_helper('Northern Mariana Islands', self._data)


    def test_single_row(self):
        """
        #name(Test with subset of earthquakes.csv dataset)
        """
        self._test_helper('California', self._data[:1])

    def test_empty_data(self):
        """
        #name(Test with dataset with no rows)
        """
        self._test_helper(None, self._data[:0])



