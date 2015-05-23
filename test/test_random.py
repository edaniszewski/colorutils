import unittest
from colorutils import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_uniform_random_rgb(self):
        for _ in range(10000):
            r, b, g = random_rgb()
            self.assertTrue(0 <= r <= 255)
            self.assertTrue(0 <= g <= 255)
            self.assertTrue(0 <= b <= 255)

    def test_uniform_random_hex(self):
        test_set = '0123456789abcdef'
        for _ in range(10000):
            for char in random_hex()[1:]:
                self.assertTrue(char in test_set)


if __name__ == '__main__':
    unittest.main()
