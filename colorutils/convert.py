#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A collection of color-space conversion functions.
"""
from __future__ import division
from static import web_colors
from exceptions import *


# --------------------
# Conversions from RGB
# --------------------


def rgb_to_hex(rgb):
    """
    Convert an RGB color representation to a HEX color representation.

    (r, g, b) :: r -> [0, 255]
                 g -> [0, 255]
                 b -> [0, 255]

    :param rgb: A tuple of three numeric values corresponding to the red, green, and blue value.
    :return: HEX representation of the input RGB value.
    :rtype: str
    """
    r, g, b = rgb
    return "#{0}{1}{2}".format(hex(int(r))[2:].zfill(2), hex(int(g))[2:].zfill(2), hex(int(b))[2:].zfill(2))


def rgb_to_web(rgb):
    """
    Convert an RGB color representation to a WEB color representation.

    (r, g, b) :: r -> [0, 255]
                 g -> [0, 255]
                 b -> [0, 255]

    :param rgb: A tuple of three numeric values corresponding to the red, green, and blue value.
    :return: WEB representation of the input RGB value.
    :rtype: str
    """
    try:
        return web_colors[rgb]
    except KeyError:
        return rgb_to_hex(rgb)


def rgb_to_yiq(rgb):
    """
    Convert an RGB color representation to a YIQ color representation.

    (r, g, b) :: r -> [0, 255]
                 g -> [0, 255]
                 b -> [0, 255]

    :param rgb: A tuple of three numeric values corresponding to the red, green, and blue value.
    :return: YIQ representation of the input RGB value.
    :rtype: tuple
    """
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    y = (0.299 * r) + (0.587 * g) + (0.114 * b)
    i = (0.596 * r) - (0.275 * g) - (0.321 * b)
    q = (0.212 * r) - (0.528 * g) + (0.311 * b)
    return round(y, 3), round(i, 3), round(q, 3)


def rgb_to_hsv(rgb):
    """
    Convert an RGB color representation to an HSV color representation.

    (r, g, b) :: r -> [0, 255]
                 g -> [0, 255]
                 b -> [0, 255]

    :param rgb: A tuple of three numeric values corresponding to the red, green, and blue value.
    :return: HSV representation of the input RGB value.
    :rtype: tuple
    """
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    _min = min(r, g, b)
    _max = max(r, g, b)
    v = _max
    delta = _max - _min

    if _max == 0:
        return 0, 0, v

    s = delta / _max

    if delta == 0:
        delta = 1

    if r == _max:
        h = 60 * (((g - b) / delta) % 6)

    elif g == _max:
        h = 60 * (((b - r) / delta) + 2)

    else:
        h = 60 * (((r - g) / delta) + 4)

    return round(h, 3), round(s, 3), round(v, 3)


# --------------------
# Conversions from HEX
# --------------------


def hex_to_rgb(_hex):
    """
    Convert a HEX color representation to an RGB color representation.

    hex :: hex -> [000000, FFFFFF]

    :param _hex: The 3- or 6-char hexadecimal string representing the color value.
    :return: RGB representation of the input HEX value.
    :rtype: tuple
    """
    _hex = _hex.strip('#')
    n = len(_hex) // 3
    if len(_hex) == 3:
        r = int(_hex[:n] * 2, 16)
        g = int(_hex[n:2 * n] * 2, 16)
        b = int(_hex[2 * n:3 * n] * 2, 16)
    else:
        r = int(_hex[:n], 16)
        g = int(_hex[n:2 * n], 16)
        b = int(_hex[2 * n:3 * n], 16)
    return r, g, b


def hex_to_web(_hex):
    """
    Convert a HEX color representation to a WEB color representation.

    hex :: hex -> [000000, FFFFFF]

    :param _hex: The 3- or 6-char hexadecimal string representing the color value.
    :return: WEB representation of the input HEX value.
    :rtype: str
    """
    try:
        return web_colors[hex_to_rgb(_hex)]
    except KeyError:
        return _hex


def hex_to_yiq(_hex):
    """
    Convert a HEX color representation to a YIQ color representation.

    hex :: hex -> [000000, FFFFFF]

    :param _hex: The 3- or 6-char hexadecimal string representing the color value.
    :return: YIQ representation of the input HEX value.
    :rtype: tuple
    """
    return rgb_to_yiq(hex_to_rgb(_hex))


def hex_to_hsv(_hex):
    """
    Convert a HEX color representation to an HSV color representation.

    hex :: hex -> [000000, FFFFFF]

    :param _hex: The 3- or 6-char hexadecimal string representing the color value.
    :return: HSV representation of the input HEX value.
    :rtype: tuple
    """
    return rgb_to_hsv(hex_to_rgb(_hex))


# --------------------
# Conversions from WEB
# --------------------


def web_to_rgb(web):
    """
    Convert a WEB color representation to an RGB color representation.

    web :: web -> [000000, FFFFFF]
                | in static.web_colors

    :param web: The WEB string representation of a color.
    :return: RGB representation of the input WEB value.
    :rtype: tuple
    """
    try:
        return web_colors[web.lower()]
    except KeyError:
        return hex_to_rgb(web)


def web_to_hex(web):
    """
    Convert a WEB color representation to a HEX color representation.

    web :: web -> [000000, FFFFFF]
                | in static.web_colors

    :param web: The WEB string representation of a color.
    :return: HEX representation of the input WEB value.
    :rtype: str
    """
    try:
        return rgb_to_hex(web_colors[web])
    except KeyError:
        return web


def web_to_yiq(web):
    """
    Convert a WEB color representation to a YIQ color representation.

    web :: web -> [000000, FFFFFF]
                | in static.web_colors

    :param web: The WEB string representation of a color.
    :return: YIQ representation of the input WEB value.
    :rtype: tuple
    """
    return rgb_to_yiq(web_to_rgb(web))


def web_to_hsv(web):
    """
    Convert a WEB color representation to an HSV color representation.

    web :: web -> [000000, FFFFFF]
                | in static.web_colors

    :param web: The WEB string representation of a color.
    :return: HSV representation of the input WEB value.
    :rtype: tuple
    """
    return rgb_to_hsv(web_to_rgb(web))


# --------------------
# Conversions from YIQ
# --------------------


def yiq_to_rgb(yiq):
    """
    Convert a YIQ color representation to an RGB color representation.

    (y, i, q) :: y -> [0, 1]
                 i -> [-0.5957, 0.5957]
                 q -> [-0.5226, 0.5226]

    :param yiq: A tuple of three numeric values corresponding to the luma and chrominance.
    :return: RGB representation of the input YIQ value.
    :rtype: tuple
    """
    y, i, q = yiq
    r = y + (0.956 * i) + (0.621 * q)
    g = y - (0.272 * i) - (0.647 * q)
    b = y - (1.108 * i) + (1.705 * q)

    r = 1 if r > 1 else max(0, r)
    g = 1 if g > 1 else max(0, g)
    b = 1 if b > 1 else max(0, b)

    return round(r * 255, 3), round(g * 255, 3), round(b * 255, 3)


def yiq_to_hex(yiq):
    """
    Convert a YIQ color representation to a HEX color representation.

    (y, i, q) :: y -> [0, 1]
                 i -> [-0.5957, 0.5957]
                 q -> [-0.5226, 0.5226]

    :param yiq: A tuple of three numeric values corresponding to the luma and chrominance.
    :return: HEX representation of the input YIQ value.
    :rtype: str
    """
    return rgb_to_hex(yiq_to_rgb(yiq))


def yiq_to_web(yiq):
    """
    Convert a YIQ color representation to a WEB color representation.

    (y, i, q) :: y -> [0, 1]
                 i -> [-0.5957, 0.5957]
                 q -> [-0.5226, 0.5226]

    :param yiq: A tuple of three numeric values corresponding to the luma and chrominance.
    :return: WEB representation of the input YIQ value.
    :rtype: str
    """
    return rgb_to_web(yiq_to_rgb(yiq))


def yiq_to_hsv(yiq):
    """
    Convert a YIQ color representation to an HSV color representation.

    (y, i, q) :: y -> [0, 1]
                 i -> [-0.5957, 0.5957]
                 q -> [-0.5226, 0.5226]

    :param yiq: A tuple of three numeric values corresponding to the luma and chrominance.
    :return: HSV representation of the input YIQ value.
    :rtype: tuple
    """
    return rgb_to_hsv(yiq_to_rgb(yiq))


# --------------------
# Conversions from HSV
# --------------------


def hsv_to_rgb(hsv):
    """
    Convert an HSV color representation to an RGB color representation.

    (h, s, v) :: h -> [0, 360)
                 s -> [0, 1]
                 v -> [0, 1]

    :param hsv: A tuple of three numeric values corresponding to the hue, saturation, and value.
    :return: RGB representation of the input HSV value.
    :rtype: tuple
    """
    h, s, v = hsv
    c = v * s
    h /= 60
    x = c * (1 - abs((h % 2) - 1))
    m = v - c

    if h < 1:
        res = (c, x, 0)
    elif h < 2:
        res = (x, c, 0)
    elif h < 3:
        res = (0, c, x)
    elif h < 4:
        res = (0, x, c)
    elif h < 5:
        res = (x, 0, c)
    elif h < 6:
        res = (c, 0, x)
    else:
        raise ColorException("Unable to convert from HSV to RGB")

    r, g, b = res
    return round((r + m)*255, 3), round((g + m)*255, 3), round((b + m)*255, 3)


def hsv_to_hex(hsv):
    """
    Convert an HSV color representation to a HEX color representation.

    (h, s, v) :: h -> [0, 360)
                 s -> [0, 1]
                 v -> [0, 1]

    :param hsv: A tuple of three numeric values corresponding to the hue, saturation, and value.
    :return: HEX representation of the input HSV value.
    :rtype: str
    """
    return rgb_to_hex(hsv_to_rgb(hsv))


def hsv_to_web(hsv):
    """
    Convert an HSV color representation to a WEB color representation.

    (h, s, v) :: h -> [0, 360)
                 s -> [0, 1]
                 v -> [0, 1]

    :param hsv: A tuple of three numeric values corresponding to the hue, saturation, and value.
    :return: WEB representation of the input HSV value.
    :rtype: str
    """
    return rgb_to_web(hsv_to_rgb(hsv))


def hsv_to_yiq(hsv):
    """
    Convert an HSV color representation to a YIQ color representation.

    (h, s, v) :: h -> [0, 360)
                 s -> [0, 1]
                 v -> [0, 1]

    :param hsv: A tuple of three numeric values corresponding to the hue, saturation, and value.
    :return: YIQ representation of the input HSV value.
    :rtype: tuple
    """
    return rgb_to_yiq(hsv_to_rgb(hsv))