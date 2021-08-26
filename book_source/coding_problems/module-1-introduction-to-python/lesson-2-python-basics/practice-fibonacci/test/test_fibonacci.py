import io
import unittest

from contextlib import redirect_stdout

from test.grading_utils import error_message
from main import fibonacci


def capture_output(fun, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            fun(*args)
        return buf.getvalue()


def import_module():
    import main


class TestFibonacci(unittest.TestCase):
    def _test_fibonacci(self, n, ans):
        val = fibonacci(n)

        self.assertEqual(ans, val, error_message(ans, val))

    def test_3(self):
        """
        #name(Testing: fibonacci(3\))
        """
        self._test_fibonacci(3, 3)

    def test_6(self):
        """
        #name(Testing: fibonacci(6\))
        """
        self._test_fibonacci(6, 5)

    def test_neg_3(self):
        """
        #name(Testing: fibonacci(-2\))
        """
        self._test_fibonacci(-2, 1)

    def test_100(self):
        """
        #name(Testing: fibonacci(100\))
        """
        self._test_fibonacci(100, 89)

    def test_uses_main_method_pattern(self):
        """
        #name(Uses main method pattern)
        """
        val = capture_output(import_module)
        ans = ''
        self.assertEqual(ans, val, 'Code does not use main method pattern')
