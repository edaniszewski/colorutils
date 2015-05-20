import unittest
from colorutils import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_color_object_input_param(self):
        _c1 = Color(Color((50, 50, 50)))
        _c2 = Color(Color(Color((25, 25, 25))))
        _c3 = Color(Color(Color(Color((10, 10, 10)))))

        self.assertEqual((50, 50, 50), _c1.rgb)
        self.assertEqual((25, 25, 25), _c2.rgb)
        self.assertEqual((10, 10, 10), _c3.rgb)

    def test_color_iterable(self):
        _c1 = Color((10, 20, 30))
        expected = [10, 20, 30]

        self.assertEqual(expected, list(_c1))


if __name__ == '__main__':
    unittest.main()
