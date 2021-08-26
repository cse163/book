import unittest

from main import count_words


class SimpleTestCase(unittest.TestCase):
    def test_example1(self):
        """
        #name(song example)
        """
        val = count_words("test/popular_techno_song.txt")
        ans = {
            "dun": 16,
            "err": 1,
            "dundundundundundundundundundun": 1,
            "er": 6,
            "ER": 6,
            "der": 4,
            "derrr": 1,
        }
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")

    def test_example2(self):
        """
        #name(one word file)
        """
        val = count_words("test/one_word.txt")
        ans = {"a": 1}
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")

    def test_example3(self):
        """
        #name(empty file)
        """
        val = count_words("test/empty.txt")
        ans = {}
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")
