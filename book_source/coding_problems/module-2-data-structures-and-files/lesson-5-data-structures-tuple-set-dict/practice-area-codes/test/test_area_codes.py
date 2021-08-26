import unittest

from main import area_codes


class SimpleTestCase(unittest.TestCase):
    def test_example1(self):
        """
        #name(Provided Example)
        """
        phone_numbers = [
            "123-456-7890",
            "206-123-45676",
            "123-000-0000",
            "425-999-9999",
        ]
        val = area_codes(phone_numbers)
        ans = set(["123", "206", "425"])
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")

    def test_example3(self):
        """
        #name(empty list)
        """
        phone_numbers = []
        val = area_codes(phone_numbers)
        ans = set([])
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")
