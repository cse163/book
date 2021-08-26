import io
import unittest
from contextlib import redirect_stdout
from test.grading_utils import error_message

import main


def capture_output(fun, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fun(*args)
    return buf.getvalue()


class TestCountdown(unittest.TestCase):
    def test_example(self):
        """
        #name(Testing: Example from spec)
        """
        val = capture_output(main.main)

        with open("test/output.txt", "r") as f:
            ans = f.read()

        self.assertEqual(ans.strip(), val.strip(), error_message(ans, val))
