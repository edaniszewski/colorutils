import unittest
from colorutils import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_text_color(self):
        # Black background
        background = (0, 0, 0)
        self.assertEqual((255, 255, 255), text_color(background))

        # White background
        background = (255, 255, 255)
        self.assertEqual((0, 0, 0), text_color(background))

        # Cyan background
        background = (0, 255, 255)
        self.assertEqual((0, 0, 0), text_color(background))

        # Yellow background
        background = (255, 255, 0)
        self.assertEqual((0, 0, 0), text_color(background))

        # Olive background
        background = (128, 128, 0)
        self.assertEqual((255, 255, 255), text_color(background))

        # Magenta background
        background = (255, 0, 255)
        self.assertEqual((255, 255, 255), text_color(background))

        # Navy background
        background = (0, 0, 128)
        self.assertEqual((255, 255, 255), text_color(background))

        # Dark gray background
        background = (75, 75, 75)
        self.assertEqual((255, 255, 255), text_color(background))


if __name__ == '__main__':
    unittest.main()
