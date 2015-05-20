import unittest
from colorutils import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_color_addition_success(self):
        _c1 = Color((35, 150, 35))
        _c2 = Color((150, 35, 150))
        self.assertEqual(Color((185, 185, 185)), _c1 + _c2)

        _c1 = Color((0, 0, 0))
        _c2 = Color((100, 50, 25))
        self.assertEqual(_c2, _c1 + _c2)

        _c1 = Color((10, 100, 255))
        _c2 = Color((50, 175, 30))
        self.assertEqual(Color((60, 255, 255)), _c1 + _c2)

        _c1 = Color((10, 10, 10))
        self.assertEqual(Color((30, 30, 30)), _c1 + (20, 20, 20))

    def test_color_addition_exception(self):
        _c1 = Color((35, 150, 35))

        with self.assertRaises(TypeError):
            _c1 + 150

        with self.assertRaises(TypeError):
            _c1 + 'a'

        with self.assertRaises(TypeError):
            _c1 + 13.0

        with self.assertRaises(TypeError):
            _c1 + ['1', '2']

        with self.assertRaises(TypeError):
            _c1 + {1: 'a', 2: 'b'}

    def test_color_subtraction_success(self):
        _c1 = Color((150, 35, 150))
        _c2 = Color((35, 150, 35))
        self.assertEqual(Color((115, 0, 115)), _c1 - _c2)

        _c1 = Color((100, 50, 25))
        _c2 = Color((0, 0, 0))
        self.assertEqual(_c1, _c1 - _c2)

        _c1 = Color((50, 175, 30))
        _c2 = Color((10, 100, 255))
        self.assertEqual(Color((40, 75, 0)), _c1 - _c2)

        _c1 = Color((30, 30, 30))
        self.assertEqual(Color((10, 10, 10)), _c1 - (20, 20, 20))

    def test_color_subtraction_exception(self):
        _c1 = Color((35, 150, 35))

        with self.assertRaises(TypeError):
            _c1 - 150

        with self.assertRaises(TypeError):
            _c1 - 'a'

        with self.assertRaises(TypeError):
            _c1 - 13.0

        with self.assertRaises(TypeError):
            _c1 - ['1', '2']

        with self.assertRaises(TypeError):
            _c1 - {1: 'a', 2: 'b'}


if __name__ == '__main__':
    unittest.main()
