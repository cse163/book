import unittest

from main import count_unique_words


class SimpleTestCase(unittest.TestCase):
    def test_example1(self):
        """
        #name(song example)
        """
        val = count_unique_words("test/song.txt")
        ans = 14
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")

    def test_example2(self):
        """
        #name(one word file)
        """
        val = count_unique_words("test/one_word.txt")
        ans = 1
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")

    def test_example3(self):
        """
        #name(empty file)
        """
        val = count_unique_words("test/empty.txt")
        ans = 0
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")
