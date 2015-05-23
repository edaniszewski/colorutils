import unittest
from colorutils import *
from colorutils.equality import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_rgb_equality_fn(self):
        _c1 = Color((255, 0, 3))
        _c2 = Color((255, 0, 3))
        _c3 = Color((12, 255, 59), equality_fn=RGB_eq)
        _c4 = Color((12, 255, 59))
        self.assertTrue(_c1 == _c2)
        self.assertFalse(_c1 == _c3)
        self.assertTrue(_c3 == _c4)

    def test_red_equality_fn(self):
        _c1 = Color((255, 0, 0), equality_fn=RED_eq)
        _c2 = Color((255, 10, 35))
        _c3 = Color((12, 255, 59), equality_fn=RED_eq)
        _c4 = Color((12, 0, 100))
        self.assertTrue(_c1 == _c2)
        self.assertFalse(_c1 == _c3)
        self.assertTrue(_c3 == _c4)

    def test_green_equality_fn(self):
        _c1 = Color((42, 1, 0), equality_fn=GREEN_eq)
        _c2 = Color((1, 1, 35))
        _c3 = Color((63, 56, 59), equality_fn=GREEN_eq)
        _c4 = Color((122, 56, 100))
        self.assertTrue(_c1 == _c2)
        self.assertFalse(_c1 == _c3)
        self.assertTrue(_c3 == _c4)

    def test_blue_equality_fn(self):
        _c1 = Color((25, 0, 36), equality_fn=BLUE_eq)
        _c2 = Color((33, 210, 36))
        _c3 = Color((60, 55, 201), equality_fn=BLUE_eq)
        _c4 = Color((79, 40, 201))
        self.assertTrue(_c1 == _c2)
        self.assertFalse(_c1 == _c3)
        self.assertTrue(_c3 == _c4)


if __name__ == '__main__':
    unittest.main()
