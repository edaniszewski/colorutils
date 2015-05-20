import unittest
from colorutils import *


class ColorUtilsTestCase(unittest.TestCase):

    def test_rgb_to_web(self):
        # Black
        self.assertEqual("Black", rgb_to_web((0, 0, 0)))

        # White
        self.assertEqual("White", rgb_to_web((255, 255, 255)))

        # Red
        self.assertEqual("Red", rgb_to_web((255, 0, 0)))

        # Lime
        self.assertEqual("Lime", rgb_to_web((0, 255, 0)))

        # Blue
        self.assertEqual("Blue", rgb_to_web((0, 0, 255)))

        # Yellow
        self.assertEqual("Yellow", rgb_to_web((255, 255, 0)))

        # Cyan
        self.assertEqual("Cyan", rgb_to_web((0, 255, 255)))

        # Magenta
        self.assertEqual("Magenta", rgb_to_web((255, 0, 255)))

        # Silver
        self.assertEqual("Silver", rgb_to_web((192, 192, 192)))

        # Gray
        self.assertEqual("Gray", rgb_to_web((128, 128, 128)))

        # Maroon
        self.assertEqual("Maroon", rgb_to_web((128, 0, 0)))

        # Olive
        self.assertEqual("Olive", rgb_to_web((128, 128, 0)))

        # Green
        self.assertEqual("Green", rgb_to_web((0, 128, 0)))

        # Purple
        self.assertEqual("Purple", rgb_to_web((128, 0, 128)))

        # Teal
        self.assertEqual("Teal", rgb_to_web((0, 128, 128)))

        # Navy
        self.assertEqual("Navy", rgb_to_web((0, 0, 128)))

        self.assertEqual("#0d9f40", rgb_to_web((13, 159, 64)))
        self.assertEqual("#4302d5", rgb_to_web((67, 2, 213)))
        self.assertEqual("#2f2f2f", rgb_to_web((47, 47, 47)))

    def test_web_to_rgb(self):
        # Black
        self.assertEqual((0, 0, 0), web_to_rgb('black'))

        # White
        self.assertEqual((255, 255, 255), web_to_rgb('White'))

        # Red
        self.assertEqual((255, 0, 0), web_to_rgb('red'))

        # Lime
        self.assertEqual((0, 255, 0), web_to_rgb('Lime'))

        # Blue
        self.assertEqual((0, 0, 255), web_to_rgb('blue'))

        # Yellow
        self.assertEqual((255, 255, 0), web_to_rgb('Yellow'))

        # Cyan
        self.assertEqual((0, 255, 255), web_to_rgb('cyan'))

        # Magenta
        self.assertEqual((255, 0, 255), web_to_rgb('Magenta'))

        # Silver
        self.assertEqual((192, 192, 192), web_to_rgb('silver'))

        # Gray
        self.assertEqual((128, 128, 128), web_to_rgb('GRAY'))

        # Maroon
        self.assertEqual((128, 0, 0), web_to_rgb('maroon'))

        # Olive
        self.assertEqual((128, 128, 0), web_to_rgb('Olive'))

        # Green
        self.assertEqual((0, 128, 0), web_to_rgb('green'))

        # Purple
        self.assertEqual((128, 0, 128), web_to_rgb('Purple'))

        # Teal
        self.assertEqual((0, 128, 128), web_to_rgb('teal'))

        # Navy
        self.assertEqual((0, 0, 128), web_to_rgb('Navy'))

        self.assertEqual((13, 159, 64), web_to_rgb("#0d9f40"))
        self.assertEqual((67, 2, 213), web_to_rgb("#4302d5"))
        self.assertEqual((47, 47, 47), web_to_rgb("#2f2f2f"))

    def test_rgb_to_hex(self):
        # Black
        self.assertEqual("#000000", rgb_to_hex((0, 0, 0)))

        # White
        self.assertEqual("#ffffff", rgb_to_hex((255, 255, 255)))

        # Red
        self.assertEqual("#ff0000", rgb_to_hex((255, 0, 0)))

        # Lime
        self.assertEqual("#00ff00", rgb_to_hex((0, 255, 0)))

        # Blue
        self.assertEqual("#0000ff", rgb_to_hex((0, 0, 255)))

        # Yellow
        self.assertEqual("#ffff00", rgb_to_hex((255, 255, 0)))

        # Cyan
        self.assertEqual("#00ffff", rgb_to_hex((0, 255, 255)))

        # Magenta
        self.assertEqual("#ff00ff", rgb_to_hex((255, 0, 255)))

        # Silver
        self.assertEqual("#c0c0c0", rgb_to_hex((192, 192, 192)))

        # Gray
        self.assertEqual("#808080", rgb_to_hex((128, 128, 128)))

        # Maroon
        self.assertEqual("#800000", rgb_to_hex((128, 0, 0)))

        # Olive
        self.assertEqual("#808000", rgb_to_hex((128, 128, 0)))

        # Green
        self.assertEqual("#008000", rgb_to_hex((0, 128, 0)))

        # Purple
        self.assertEqual("#800080", rgb_to_hex((128, 0, 128)))

        # Teal
        self.assertEqual("#008080", rgb_to_hex((0, 128, 128)))

        # Navy
        self.assertEqual("#000080", rgb_to_hex((0, 0, 128)))

    def test_hex_to_rgb(self):
        # Black
        self.assertEqual((0, 0, 0), hex_to_rgb("#000000"))

        # White
        self.assertEqual((255, 255, 255), hex_to_rgb("#ffffff"))

        # Red
        self.assertEqual((255, 0, 0), hex_to_rgb("#ff0000"))

        # Lime
        self.assertEqual((0, 255, 0), hex_to_rgb("#00ff00"))

        # Blue
        self.assertEqual((0, 0, 255), hex_to_rgb("#0000ff"))

        # Yellow
        self.assertEqual((255, 255, 0), hex_to_rgb("#ffff00"))

        # Cyan
        self.assertEqual((0, 255, 255), hex_to_rgb("#00ffff"))

        # Magenta
        self.assertEqual((255, 0, 255), hex_to_rgb("#ff00ff"))

        # Silver
        self.assertEqual((192, 192, 192), hex_to_rgb("#c0c0c0"))

        # Gray
        self.assertEqual((128, 128, 128), hex_to_rgb("#808080"))

        # Maroon
        self.assertEqual((128, 0, 0), hex_to_rgb("#800000"))

        # Olive
        self.assertEqual((128, 128, 0), hex_to_rgb("#808000"))

        # Green
        self.assertEqual((0, 128, 0), hex_to_rgb("#008000"))

        # Purple
        self.assertEqual((128, 0, 128), hex_to_rgb("#800080"))

        # Teal
        self.assertEqual((0, 128, 128), hex_to_rgb("#008080"))

        # Navy
        self.assertEqual((0, 0, 128), hex_to_rgb("#000080"))


if __name__ == '__main__':
    unittest.main()
