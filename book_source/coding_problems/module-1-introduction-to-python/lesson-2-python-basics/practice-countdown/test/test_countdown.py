import io
import unittest
from contextlib import redirect_stdout
from test.grading_utils import error_message

from main import countdown


def capture_output(fun, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fun(*args)
    return buf.getvalue()


def import_module():
    import main


class TestCountdown(unittest.TestCase):
    def _test_countdown(self, n, expected_out_file):
        val = capture_output(countdown, n)

        with open(expected_out_file, "r") as f:
            ans = f.read()

        self.assertEqual(ans.strip(), val.strip(), error_message(ans, val))

    def test_60(self):
        """
        #name(Testing: countdown(60\))
        """
        self._test_countdown(60, "test/expected_out_60.txt")

    def test_15(self):
        """
        #name(Testing: countdown(15\))
        """
        self._test_countdown(15, "test/expected_out_15.txt")

    def test_neg_4(self):
        """
        #name(Testing: countdown(-4\))
        """
        self._test_countdown(-4, "test/expected_out_-4.txt")

    def test_0(self):
        """
        #name(Testing: countdown(0\))
        """
        self._test_countdown(0, "test/expected_out_0.txt")

    def test_uses_main_method_pattern(self):
        """
        #name(Uses main method pattern)
        """
        val = capture_output(import_module)
        ans = ""
        self.assertEqual(ans, val, "Code does not use main method pattern")
