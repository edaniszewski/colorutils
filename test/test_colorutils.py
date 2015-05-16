import unittest
from colorutils.colorutils import *


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

    def test_minify_hex(self):
        self.assertEqual('#333', minify_hex('#333'))
        self.assertEqual('#f235aa', minify_hex('#f235aa'))
        self.assertEqual('#fa3', minify_hex('#ffaa33'))

    def test_color_object_input_param(self):
        _c1 = Color(Color((50, 50, 50)))
        _c2 = Color(Color(Color((25, 25, 25))))
        _c3 = Color(Color(Color(Color((10, 10, 10)))))

        self.assertEqual((50, 50, 50), _c1.rgb)
        self.assertEqual((25, 25, 25), _c2.rgb)
        self.assertEqual((10, 10, 10), _c3.rgb)

    def test_uniform_random_rgb(self):
        for _ in range(10000):
            r, b, g = uniform_random_rgb()
            self.assertTrue(0 <= r <= 255)
            self.assertTrue(0 <= g <= 255)
            self.assertTrue(0 <= b <= 255)

    def test_uniform_random_hex(self):
        test_set = '0123456789abcdef'
        for _ in range(10000):
            for char in uniform_random_hex()[1:]:
                self.assertTrue(char in test_set)

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
