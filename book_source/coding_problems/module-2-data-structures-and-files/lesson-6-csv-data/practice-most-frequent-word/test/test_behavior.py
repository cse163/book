import unittest

import main

class Test(unittest.TestCase):
    def test_example(self):
        """
        #name(Test Green Eggs and Yam example)
        """
        word_counts = {'green': 2, 'eggs': 6, 'and': 3, 'yam': 2}
        val = main.most_frequent(word_counts)
        self.assertEquals('eggs', val, f'Expected eggs, but received {val}')

    def test_single_count(self):
        """
        #name(Test example with only one word)
        """
        word_counts = {'green': 2}
        val = main.most_frequent(word_counts)
        self.assertEquals('green', val, f'Expected green, but received {val}')

    def test_empty_dict(self):
        """
        #name(Test empty dict)
        """
        word_counts = {}
        val = main.most_frequent(word_counts)
        self.assertEquals(None, val, f'Expected None, but received {val}')
