import unittest

import main


class SimpleTestCase(unittest.TestCase):
    def test_run_main(self):
        """
        #name(Fixed crash)
        """
        main.main()
