import io
import unittest

from contextlib import redirect_stdout

from pair import Pair

class Test(unittest.TestCase):
    def test_eq(self):
        """
        #name(Test equality)
        """
        p1 = Pair(1, 2)
        p2 = Pair(1, 2)
        p3 = p1
        p4 = Pair(1, 5)

        self.assertTrue(p1 == p2, 'Expected true when pairs have same values')
        self.assertTrue(p1 == p3, 'Expected true if both are same object')
        self.assertFalse(p1 == p4, 'Expected false if pairs store different values')

    def test_repr(self):
        """
        #name(Test print)
        """
        p = Pair(7, 8)
        self.assertEqual(str, type(p.__repr__()), '__repr__ should return a str')
        self.assertEqual('(7, 8)', p.__repr__(), '__repr__ did not return str of expected format')

    def test_get(self):
        """
        #name(Test bracket notation for getting values)
        """
        p = Pair(10, 11)
        self.assertEqual(10, p[0], 'p[0] did not return correct value')
        self.assertEqual(11, p[1], 'p[1] did not return correct value')

    @staticmethod
    def capture_output(fun, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            fun(*args)
        return buf.getvalue()

    def test_set(self):
        """
        #name(Test bracket notation for assigning values)
        """
        p = Pair(1, 2)
        self.assertTrue(hasattr(p, '__setitem__'), 'Should have method for assignment that prints error')

        out = Test.capture_output(p.__setitem__, 0, 14)
        self.assertEqual('Error: Pair is immutable!', out.strip(), 'Did not produce proper error message')

