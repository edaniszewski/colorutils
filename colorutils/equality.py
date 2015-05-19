#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A collection of colorutils-specific equality functions.
"""


## RGB Equalities
RGB_eq = lambda c1, c2: c1.rgb == c2.rgb
RED_eq = lambda c1, c2: c1.red == c2.red
GREEN_eq = lambda c1, c2: c1.green == c2.green
BLUE_eq = lambda c1, c2: c1.blue == c2.blue

## HEX Equalities
HEX_eq = lambda c1, c2: c1.hex == c2.hex

## WEB Equalities
WEB_eq = lambda c1, c2: c1.web == c2.web