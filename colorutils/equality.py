#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A collection of colorutils-specific equality functions.
"""

# -----------------------------------------------
# RGB Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# red, green, and blue values of each color.
# -----------------------------------------------
RGB_eq = lambda c1, c2: c1.rgb == c2.rgb

# -----------------------------------------------
# RGB-Red Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# red value of the rgb representation of each
# color.
# -----------------------------------------------
RED_eq = lambda c1, c2: c1.red == c2.red

# -----------------------------------------------
# RGB-Green Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# green value of the rgb representation of each
# color.
# -----------------------------------------------
GREEN_eq = lambda c1, c2: c1.green == c2.green

# -----------------------------------------------
# RGB-Blue Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# blue value of the rgb representation of each
# color.
# -----------------------------------------------
BLUE_eq = lambda c1, c2: c1.blue == c2.blue

# -----------------------------------------------
# HEX Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# HEX string representation of each color.
# -----------------------------------------------
HEX_eq = lambda c1, c2: c1.hex == c2.hex

# -----------------------------------------------
# WEB Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# WEB string representation of each color.
# -----------------------------------------------
WEB_eq = lambda c1, c2: c1.web == c2.web

# -----------------------------------------------
# YIQ Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# YIQ representation of each color.
# -----------------------------------------------
YIQ_eq = lambda c1, c2: c1.yiq == c2.yiq

# -----------------------------------------------
# HSV Color Equality
# ...............................................
#
# Given two Colors, test equality between the
# HSV representation of each color.
# -----------------------------------------------
HSV_eq = lambda c1, c2: c1.hsv == c2.hsv