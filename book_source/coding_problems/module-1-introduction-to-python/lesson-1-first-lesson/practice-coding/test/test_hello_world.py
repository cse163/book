import io
import unittest
from contextlib import redirect_stdout
from test.grading_utils import error_message


def capture_output(fun, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fun(*args)
    return buf.getvalue()


class TestHelloWorld(unittest.TestCase):
    def test_pass(self):
        """
        #name(Testing: This is a test that always passes)
        """
        self.assertTrue(True)

    def test_hello_world(self):
        """
        #name(Testing: Hello world)
        """

        # Define function to run student's code
        # Since there is no main method, runs on import
        def run_main():
            import main

        val = capture_output(run_main)
        val = val.strip()  # Remove extra whitespace

        # Get the expected output
        with open("test/expected_output.txt", "r") as f:
            ans = f.read().strip()

        # Compare student's answer to expected output
        self.assertEqual(ans, val, error_message(ans, val))
