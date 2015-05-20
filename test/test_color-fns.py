import unittest
from colorutils import *

class ColorUtilsTestCase(unittest.TestCase):

    def test_minify_hex(self):
        self.assertEqual('#333', minify_hex('#333'))
        self.assertEqual('#f235aa', minify_hex('#f235aa'))
        self.assertEqual('#fa3', minify_hex('#ffaa33'))


if __name__ == '__main__':
    unittest.main()
