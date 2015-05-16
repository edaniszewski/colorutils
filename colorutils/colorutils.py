"""
A Color Utility Library
-----------------------
Author: Erick Daniszewski
Version: 0.1

colorutils provides utilities for working with colors, which are abstractly modeled by the Color class. The Color class
currently uses an internal RGB representation, but has allowances for RGB, HEX, and WEB formats.

Current capabilities include:
 * abstract color model
 * color format conversion
 * random color generation
"""
from __future__ import division
import random


class ColorException(Exception):
    """
    General exception thrown for color utils non-exit exceptions.
    """
    pass


class Format:
    """
    Format contains well-known color formats which are supported by the Color class. This class is effectively
    an implementation of Enum for Python 2.7

    The color formats currently supported include:
        RGB : an additive color model using red, green, and blue decimal values
        HEX : the RGB model represented in hexadecimal
        WEB : colors used by web browsers, contains both color names and HEX
    """
    RGB, HEX, WEB = range(3)


class ArithmeticModel:
    """
    ArithmeticModel contains well-known arithmetic models which determine the additive behavior of the Color class. The
    default model is the light model (behaves similar to adding light). The alternative is the blend model, which
    averages the colors. This class is effectively an implementation of Enum for Python 2.7

    Note that Color subtraction happens in the same manner, regardless of the arithmetic model chosen.

    Reference: http://stackoverflow.com/questions/726549/algorithm-for-additive-color-mixing-for-rgb-values
    """
    LIGHT, BLEND = range(2)


class Color(object):
    """
    Color is the model which maintains the information for a color. If no color is specified on class instantiation,
    the color will default to black.

    The color formats which the Color class supports are enumerated in the Format class.

    Color equality defaults to RGB equality testing (where the r, g, and b values of one Color must equal the r, g,
    and b values of a second Color), however different equality functions can be used. Standard equality functions are
    provided by the colorutils package, or custom equality functions can be defined.

    The default additive model for Color instances behaves like the light model. Different additive models may be
    specified. The supported models are found in the ArithmeticModel class.
    """
    def __init__(self, color=None, **kwargs):
        """
        Initialization

        :param color:
        :param kwargs:
        :return:
        """
        self.equality_fn = RGB_eq
        self.arithmetic = ArithmeticModel.LIGHT

        if isinstance(color, Color):
            self._color = color._color
        else:
            self._color = color if color else rgb_min

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        """
        Equals

        :param other:
        :return:
        """
        if isinstance(other, Color):
            return self.equality_fn(self, other)
        return False

    def __ne__(self, other):
        """
        Not Equals

        :param other:
        :return:
        """
        return not self.__eq__(other)

    def __add__(self, other):
        """
        Addition

        :param other:
        :return:
        """
        if isinstance(other, Color):
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other.rgb
        elif isinstance(other, tuple) and len(other) == 3:
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other
        else:
            raise TypeError("Unsupported operand type(s) for +: '{0}' and '{1}'".format(type(self), type(other)))

        if self.arithmetic is ArithmeticModel.LIGHT:
            return Color((min(r1 + r2, rgb_max_val), min(g1 + g2, rgb_max_val), min(b1 + b2, rgb_max_val)))
        else:
            return Color(((r1 + r2 // 2), (g1 + g2 // 2), (b1 + b2 // 2)))

    def __sub__(self, other):
        """
        Subtraction

        :param other:
        :return:
        """
        if isinstance(other, Color):
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other.rgb
        elif isinstance(other, tuple) and len(other) == 3:
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other
        else:
            raise TypeError("Unsupported operand type(s) for -: '{0}' and '{1}'".format(type(self), type(other)))

        return Color((max(r1 - r2, rgb_min_val), max(g1 - g2, rgb_min_val), max(b1 - b2, rgb_min_val)))

    def __str__(self):
        """
        String representation

        :return:
        """
        return "{}".format(self._color)

    def __repr__(self):
        """
        General representation

        :return:
        """
        return "<Color {}>".format(self._color)

    @property
    def red(self):
        """
        The red component of the RGB color representation.
        """
        return self._color[0]

    @red.setter
    def red(self, value):
        self._color = (value,) + self._color[1:]

    @property
    def green(self):
        """
        The green component of the RGB color representation.
        """
        return self._color[1]

    @green.setter
    def green(self, value):
        self._color = self._color[:1] + (value,) + self._color[2:]

    @property
    def blue(self):
        """
        The blue component of the RGB color representation.
        """
        return self._color[2]

    @blue.setter
    def blue(self, value):
        self._color = self._color[:2] + (value,)

    @property
    def rgb(self):
        """
        A 3-tuple containing int values representing red, blue, and green.
        """
        return self._color

    @rgb.setter
    def rgb(self, value):
        self._color = value

    @property
    def hex(self):
        """
        A 6-char hexidecimal string representation of the RGB value, with a prepended octothorpe.
        """
        return rgb_to_hex(self.rgb)

    @hex.setter
    def hex(self, value):
        self._color = hex_to_rgb(value)

    @property
    def shorthex(self):
        """
        The same as Color.hex, however, HEX values that can be minified to 3-char are returned as such.
        """
        return minify_hex(self.hex)

    @property
    def web(self):
        """
        A WEB representation of the RGB color. This could be a well-known color name string or a HEX representation.
        """
        return rgb_to_web(self.rgb)

    @web.setter
    def web(self, value):
        self._color = web_to_rgb(value)

# -----------------------------------------------
# Color Equality
# -----------------------------------------------

## RGB Equalities
RGB_eq = lambda c1, c2: c1.rgb == c2.rgb
RED_eq = lambda c1, c2: c1.red == c2.red
GREEN_eq = lambda c1, c2: c1.green == c2.green
BLUE_eq = lambda c1, c2: c1.blue == c2.blue

## HEX Equalities
HEX_eq = lambda c1, c2: c1.hex == c2.hex

## WEB Equalities
WEB_eq = lambda c1, c2: c1.web == c2.web

# -----------------------------------------------
# Global Declarations
# -----------------------------------------------

web_colors = {
    (255, 192, 203): 'Pink',
    (255, 182, 193): 'LightPink',
    (255, 105, 180): 'HotPink',
    (255, 20, 147): 'DeepPink',
    (219, 112, 147): 'PaleVioletRed',
    (199, 21, 133): 'MediumVioletRed',
    (255, 160, 122): 'LightSalmon',
    (250, 128, 114): 'Salmon',
    (233, 150, 122): 'DarkSalmon',
    (240, 128, 128): 'LightCoral',
    (205, 92, 92): 'IndianRed',
    (220, 20, 60): 'Crimson',
    (178, 34, 34): 'FireBrick',
    (139, 0, 0): 'DarkRed',
    (255, 0, 0): 'Red',
    (255, 69, 0): 'OrangeRed',
    (255, 99, 71): 'Tomato',
    (255, 127, 80): 'Coral',
    (255, 140, 0): 'DarkOrange',
    (255, 165, 0): 'Orange',
    (255, 255, 0): 'Yellow',
    (255, 255, 224): 'LightYellow',
    (255, 250, 205): 'LemonChiffon',
    (250, 250, 210): 'LightGoldenrodYellow',
    (255, 239, 213): 'PapayaWhip',
    (255, 228, 181): 'Moccasin',
    (255, 218, 185): 'PeachPuff',
    (238, 232, 170): 'PaleGoldenrod',
    (240, 230, 140): 'Khaki',
    (189, 183, 107): 'DarkKhaki',
    (255, 215, 0): 'Gold',
    (255, 248, 220): 'Cornsilk',
    (255, 235, 205): 'BlanchedAlmond',
    (255, 228, 196): 'Bisque',
    (255, 222, 173): 'NavajoWhite',
    (245, 222, 179): 'Wheat',
    (222, 184, 135): 'BurlyWood',
    (210, 180, 140): 'Tan',
    (188, 143, 143): 'RosyBrown',
    (244, 164, 96): 'SandyBrown',
    (218, 165, 32): 'Goldenrod',
    (184, 134, 11): 'DarkGoldenrod',
    (205, 133, 63): 'Peru',
    (210, 105, 30): 'Chocolate',
    (139, 69, 19): 'SaddleBrown',
    (160, 82, 45): 'Sienna',
    (165, 42, 42): 'Brown',
    (128, 0, 0): 'Maroon',
    (85, 107, 47): 'DarkOliveGreen',
    (128, 128, 0): 'Olive',
    (107, 142, 35): 'OliveDrab',
    (154, 205, 50): 'YellowGreen',
    (50, 205, 50): 'LimeGreen',
    (0, 255, 0): 'Lime',
    (124, 252, 0): 'LawnGreen',
    (127, 255, 0): 'Chartreuse',
    (173, 255, 47): 'GreenYellow',
    (0, 255, 127): 'SpringGreen',
    (0, 250, 154): 'MediumSpringGreen',
    (144, 238, 144): 'LightGreen',
    (152, 251, 152): 'PaleGreen',
    (143, 188, 143): 'DarkSeaGreen',
    (60, 179, 113): 'MediumSeaGreen',
    (46, 139, 87): 'SeaGreen',
    (34, 139, 34): 'ForestGreen',
    (0, 128, 0): 'Green',
    (0, 100, 0): 'DarkGreen',
    (102, 205, 170): 'MediumAquamarine',
    (0, 255, 255): 'Aqua',
    (0, 255, 255): 'Cyan',
    (224, 255, 255): 'LightCyan',
    (175, 238, 238): 'PaleTurquoise',
    (127, 255, 212): 'Aquamarine',
    (64, 224, 208): 'Turquoise',
    (72, 209, 204): 'MediumTurquoise',
    (0, 206, 209): 'DarkTurquoise',
    (32, 178, 170): 'LightSeaGreen',
    (95, 158, 160): 'CadetBlue',
    (0, 139, 139): 'DarkCyan',
    (0, 128, 128): 'Teal',
    (176, 196, 222): 'LightSteelBlue',
    (176, 224, 230): 'PowderBlue',
    (173, 216, 230): 'LightBlue',
    (135, 206, 235): 'SkyBlue',
    (135, 206, 250): 'LightSkyBlue',
    (0, 191, 255): 'DeepSkyBlue',
    (30, 144, 255): 'DodgerBlue',
    (100, 149, 237): 'CornflowerBlue',
    (70, 130, 180): 'SteelBlue',
    (65, 105, 225): 'RoyalBlue',
    (0, 0, 255): 'Blue',
    (0, 0, 205): 'MediumBlue',
    (0, 0, 139): 'DarkBlue',
    (0, 0, 128): 'Navy',
    (25, 25, 112): 'MidnightBlue',
    (230, 230, 250): 'Lavender',
    (216, 191, 216): 'Thistle',
    (221, 160, 221): 'Plum',
    (238, 130, 238): 'Violet',
    (218, 112, 214): 'Orchid',
    (255, 0, 255): 'Fuchsia',
    (255, 0, 255): 'Magenta',
    (186, 85, 211): 'MediumOrchid',
    (147, 112, 219): 'MediumPurple',
    (138, 43, 226): 'BlueViolet',
    (148, 0, 211): 'DarkViolet',
    (153, 50, 204): 'DarkOrchid',
    (139, 0, 139): 'DarkMagenta',
    (128, 0, 128): 'Purple',
    (75, 0, 130): 'Indigo',
    (72, 61, 139): 'DarkSlateBlue',
    (102, 51, 153): 'RebeccaPurple',
    (106, 90, 205): 'SlateBlue',
    (123, 104, 238): 'MediumSlateBlue',
    (255, 255, 255): 'White',
    (255, 250, 250): 'Snow',
    (240, 255, 240): 'Honeydew',
    (245, 255, 250): 'MintCream',
    (240, 255, 255): 'Azure',
    (240, 248, 255): 'AliceBlue',
    (248, 248, 255): 'GhostWhite',
    (245, 245, 245): 'WhiteSmoke',
    (255, 245, 238): 'Seashell',
    (245, 245, 220): 'Beige',
    (253, 245, 230): 'OldLace',
    (255, 250, 240): 'FloralWhite',
    (255, 255, 240): 'Ivory',
    (250, 235, 215): 'AntiqueWhite',
    (250, 240, 230): 'Linen',
    (255, 240, 245): 'LavenderBlush',
    (255, 228, 225): 'MistyRose',
    (220, 220, 220): 'Gainsboro',
    (211, 211, 211): 'LightGrey',
    (192, 192, 192): 'Silver',
    (169, 169, 169): 'DarkGray',
    (128, 128, 128): 'Gray',
    (105, 105, 105): 'DimGray',
    (119, 136, 153): 'LightSlateGray',
    (112, 128, 144): 'SlateGray',
    (47, 79, 79): 'DarkSlateGray',
    (0, 0, 0): 'Black'
}

# Appends the reverse web_colors dictionary to web_colors, so reverse lookups are allowed
web_colors.update(dict([(v.lower(), k) for k, v in web_colors.items()]))

rgb_min_val = 0
rgb_max_val = 255
rgb_min = (0, 0, 0)
rgb_max = (255, 255, 255)

# -----------------------------------------------
# Conversion Functions
# -----------------------------------------------

def rgb_to_hex(rgb):
    """
    Convert a tuple containing RGB values into a corresponding HEX representation.

    :param rgb:
    :return:
    """
    r, g, b = rgb
    return "#{0}{1}{2}".format(hex(r)[2:].zfill(2), hex(g)[2:].zfill(2), hex(b)[2:].zfill(2))


def rgb_to_web(rgb):
    """
    Convert a RGB color tuple into a WEB color representation, being either a well-known color name if supported, or
    the equivalent HEX value.

    :param rgb:
    :return:
    """
    try:
        return web_colors[rgb]
    except KeyError:
        return rgb_to_hex(rgb)


def hex_to_rgb(_hex):
    """
    Convert a HEX color string into a tuple containing corresponding RGB values.

    :param _hex:
    :type _hex: str
    :return:
    """
    _hex = _hex.strip('#')
    n = len(_hex) // 3
    if len(_hex) == 3:
        r = int(_hex[:n]*2, 16)
        g = int(_hex[n:2 * n]*2, 16)
        b = int(_hex[2 * n:3 * n]*2, 16)
    else:
        r = int(_hex[:n], 16)
        g = int(_hex[n:2 * n], 16)
        b = int(_hex[2 * n:3 * n], 16)
    return r, g, b


def hex_to_web(_hex):
    """
    Convert a HEX color string into a WEB color representation.

    :param _hex:
    :return:
    """
    try:
        return web_colors[hex_to_rgb(_hex)]
    except KeyError:
        return _hex


def web_to_rgb(web):
    """
    Convert a WEB color representation into an RGB color tuple.

    :param web:
    :return:
    """
    try:
        return web_colors[web.lower()]
    except KeyError:
        return hex_to_rgb(web)


def web_to_hex(web):
    """
    Convert a WEB color representation into a HEX color string.

    :param web:
    :return:
    """
    try:
        return rgb_to_hex(web_colors[web])
    except KeyError:
        return web


def rgb_to_yiq(rgb):
    """
    Convert an RGB color tuple into the YIQ color representation.

    :param rgb:
    :return:
    """
    try:
        r, g, b = rgb
        y = (0.299 * r) + (0.587 * g) + (0.114 * b)
        i = (0.596 * r) + (-0.275 * g) + (-0.321 * b)
        q = (0.212 * r) + (-0.528 * g) + (0.311 * b)
        return y, i, q
    except Exception as e:
        raise ColorException('Unable to convert RGB to YIQ: ' + e.message)

# -----------------------------------------------
# Utility Functions
# -----------------------------------------------

# - - - - - - - - - - - - - - -
# Random Color Functions
# - - - - - - - - - - - - - - -

def uniform_random_rgb():
    """
    Generate a uniformly random RGB value.

    :return: A tuple of three integers with values between 0 and 255 inclusive
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def uniform_random_hex():
    """
    Generate a uniformly random HEX value.

    :return: A string representing a random HEX value between 000000 and FFFFFF inclusive
    """
    return rgb_to_hex(uniform_random_rgb())


def uniform_random_web():
    """
    Generate a uniformly random WEB value.

    :return:
    """
    return rgb_to_web(uniform_random_rgb())


def offset_random_rgb(seed, amount=1):
    """
    Given a seed color, generate a specified number of random colors (1 color by default) determined by a randomized
    offset from the seed.

    :param seed:
    :param amount:
    :return:
    """
    r, g, b = seed

    results = []
    for _ in range(amount):
        base_val = ((r + g + b) / 3) + 1  # Add one to eliminate case where the base value would otherwise be 0
        new_val = base_val + (random.random() * rgb_max_val / 5)  # Randomly offset with an arbitrary multiplier
        ratio = new_val / base_val
        results.append((min(int(r*ratio), rgb_max_val), min(int(g*ratio), rgb_max_val), min(int(b*ratio), rgb_max_val)))

    return results[0] if len(results) > 1 else results


def offset_random_hex(seed, amount=1):
    """
    Given a seed color, generate a specified number of random colors (1 color by default) determined by a randomized
    offset from the seed.

    :param seed:
    :param amount:
    :return:
    """
    return rgb_to_hex(offset_random_rgb(seed, amount))


def offset_random_web(seed, amount=1):
    """
    Given a seed color, generate a specified number of random colors (1 color by default) determined by a randomized
    offset from the seed.

    :param seed:
    :param amount:
    :return:
    """
    return rgb_to_web(offset_random_rgb(seed, amount))


# - - - - - - - - - - - - - - -
# Other Color Functions
# - - - - - - - - - - - - - - -

def text_color(background, dark_color=rgb_min, light_color=rgb_max):
    """
    Given a background color in the form of an RGB 3-tuple, returns the color the text should be (defaulting to white
    and black) for best readability. The light (white) and dark (black) defaults can be overridden to return preferred
    values.

    :param background:
    :param dark_color:
    :param light_color:
    :return:
    """
    max_y = rgb_to_yiq(rgb_max)[0]
    return light_color if rgb_to_yiq(background)[0] <= max_y / 2 else dark_color


def minify_hex(_hex):
    """
    Given a HEX value, tries to reduce it from a 6 character hex (e.g. #ffffff) to a 3 character hex (e.g. #fff).
    If the HEX value is unable to be minified, returns the 6 character HEX representation.

    :param _hex:
    :return:
    """
    size = len(_hex.strip('#'))
    if size == 3:
        return _hex
    elif size == 6:
        if _hex[1] == _hex[2] and _hex[3] == _hex[4] and _hex[5] == _hex[6]:
            return _hex[0::2]
        else:
            return _hex
    else:
        raise ColorException('Unexpected HEX size when minifying.')