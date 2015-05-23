#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A Color Utility Library
-----------------------
colorutils provides utilities for working with colors, which are abstractly modeled by the Color class. The Color class
currently uses an internal RGB representation, but has allowances for RGB, HEX, and WEB formats.
"""
from __future__ import division
import random

from static import *
from equality import RGB_eq
from convert import *


class Format:
    """
    Format contains well-known color formats which are supported by the Color class. This class is effectively
    an implementation of Enum for Python 2.7
    """
    RGB, HEX, WEB, YIQ, HSV = range(5)


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
        """ Initialization """
        self.equality_fn = RGB_eq
        self.arithmetic = ArithmeticModel.LIGHT

        if isinstance(color, Color):
            self._color = color._color
        else:
            self._color = color if color else rgb_min

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        """ Equals """
        if isinstance(other, Color):
            return self.equality_fn(self, other)
        return False

    def __ne__(self, other):
        """ Not Equals """
        return not self.__eq__(other)

    def __add__(self, other):
        """ Addition """
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
        """ Subtraction """
        if isinstance(other, Color):
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other.rgb
        elif isinstance(other, tuple) and len(other) == 3:
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other
        else:
            raise TypeError("Unsupported operand type(s) for -: '{0}' and '{1}'".format(type(self), type(other)))

        return Color((max(r1 - r2, rgb_min_val), max(g1 - g2, rgb_min_val), max(b1 - b2, rgb_min_val)))

    def __iter__(self):
        """ Iterator """
        return iter(self._color)

    def __str__(self):
        """ String representation """
        return "{}".format(self._color)

    def __repr__(self):
        """ General representation """
        return "<Color {}>".format(self._color)

    @property
    def red(self):
        """ The red component of the RGB color representation. """
        return self._color[0]

    @red.setter
    def red(self, value):
        self._color[0] = value

    @property
    def green(self):
        """ The green component of the RGB color representation. """
        return self._color[1]

    @green.setter
    def green(self, value):
        self._color[1] = value

    @property
    def blue(self):
        """ The blue component of the RGB color representation. """
        return self._color[2]

    @blue.setter
    def blue(self, value):
        self._color[2] = value

    @property
    def rgb(self):
        """ An RGB representation of the color. """
        return self._color

    @rgb.setter
    def rgb(self, value):
        self._color = value

    @property
    def hex(self):
        """ A 6-char HEX representation of the color, with a prepended octothorpe. """
        return rgb_to_hex(self.rgb)

    @hex.setter
    def hex(self, value):
        self._color = hex_to_rgb(value)

    @property
    def shorthex(self):
        """ The same as Color.hex, however, HEX values that can be minified to 3-char are returned as such. """
        return minify_hex(self.hex)

    @property
    def web(self):
        """ A WEB representation of the color. """
        return rgb_to_web(self.rgb)

    @web.setter
    def web(self, value):
        self._color = web_to_rgb(value)

    @property
    def yiq(self):
        """ A YIQ representation of the color. """
        return rgb_to_yiq(self.rgb)

    @yiq.setter
    def yiq(self, value):
        self._color = yiq_to_rgb(value)

    @property
    def hsv(self):
        """ An HSV representation of the color """
        return rgb_to_hsv(self.rgb)

    @hsv.setter
    def hsv(self, value):
        self._color = hsv_to_rgb(value)


# -----------------------------------------------
# Utility Functions
# -----------------------------------------------

# - - - - - - - - - - - - - - -
# Random Color Functions
# - - - - - - - - - - - - - - -


def random_rgb():
    """
    Generate a uniformly random RGB value.

    :return: A tuple of three integers with values between 0 and 255 inclusive
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_hex():
    """
    Generate a uniformly random HEX value.

    :return: A string representing a random HEX value between 000000 and FFFFFF inclusive
    """
    return rgb_to_hex(random_rgb())


def random_web():
    """
    Generate a uniformly random WEB value.

    :return:
    """
    return rgb_to_web(random_rgb())


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


def color_run(start_color, end_color, step_count, inclusive=True, to_color=True):
    """
    Given a start color, end color, and a number of steps, returns a list of colors which represent a 'scale' between
    the start and end color.

    :param start_color: The color starting the run
    :param end_color: The color ending the run
    :param step_count: The number of colors to have between the start and end color
    :param inclusive: Flag determining whether to include start and end values in run (default True)
    :param to_color: Flag indicating return values should be Color objects (default True)
    :return: List of colors between the start and end color
    :rtype: list
    """
    if isinstance(start_color, Color):
        start_color = start_color.rgb

    if isinstance(end_color, Color):
        end_color = end_color.rgb

    step = tuple((end_color[i] - start_color[i])/step_count for i in range(3))

    add = lambda x, y: tuple(sum(z) for z in zip(x, y))
    mult = lambda x, y: tuple(y * z for z in x)

    run = [add(start_color, mult(step, i)) for i in range(1, step_count)]

    if inclusive:
        run = [start_color] + run + [end_color]

    return run if not to_color else [Color(c) for c in run]


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
        raise ColorException('Unexpected HEX size when minifying: {}'.format(size))
