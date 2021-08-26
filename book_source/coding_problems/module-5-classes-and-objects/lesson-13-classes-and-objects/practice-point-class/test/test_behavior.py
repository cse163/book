import unittest

# Import the student's factorial function from main.py
from point import Point


class SimpleTestCase(unittest.TestCase):
    def test_get(self):
        """
        #name(Call get_x(\) and get_y(\) on Point(4, 5\))
        """
        p = Point(4, 5)
        self.assertEqual(4, p.get_x())
        self.assertEqual(5, p.get_y())


    def test_getx_after_setx(self):
        """
        #name(Call get_x(\) after calling set_x(\))
        """
        p = Point(4, 3)
        p.set_x(7)
        self.assertEqual(7, p.get_x())

    def test_gety_after_setx(self):
        """
        #name(Call get_y(\) after calling set_x(\))
        """
        p = Point(4, 3)
        p.set_x(7)
        self.assertEqual(4, p.get_y())

    def test_gety_after_sety(self):
        """
        #name(Call get_y(\) after calling set_x(\))
        """
        p = Point(4, 3)
        p.set_y(7)
        self.assertEqual(7, p.get_y())

    def test_gety_after_setx(self):
        """
        #name(Call get_y(\) after calling set_x(\))
        """
        p = Point(4, 3)
        p.set_x(7)
        self.assertEqual(3, p.get_y())

    def test_display(self):
        """
        #name(Call p.display())
        """
        p = Point(4, 3)
        self.assertEqual('(4, 3)', p.display())

    def test_display_after_setx(self):
        """
        #name(Call p.display() after set_x)
        """
        p = Point(4, 3)
        p.set_x(2)
        self.assertEqual('(2, 3)', p.display())


    def test_display_after_setx(self):
        """
        #name(Call p.display() after set_x)
        """
        p = Point(4, 3)
        p.set_x(2)
        self.assertEqual('(2, 3)', p.display())

