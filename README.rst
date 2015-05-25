==========
colorutils
==========

.. image:: https://pypip.in/license/colorutils/badge.svg
    :target: https://pypi.python.org/pypi/colorutils/
    :alt: License
    
.. image:: https://pypip.in/version/colorutils/badge.svg
    :target: https://pypi.python.org/pypi/colorutils/
    :alt: Latest Version
    
.. image:: https://pypip.in/download/colorutils/badge.svg
    :target: https://pypi.python.org/pypi//colorutils/
    :alt: Downloads

A library which provides utilities for working with colors in Python. Colors are modeled by the ``Color`` class and can be
represented in ``RGB``, ``HEX``, ``WEB``, and ``YIQ`` formats.

0. Installation
===============

``colorutils`` can be installed from pypi::

    pip install colorutils
    
to update an existing installation from pypi to the latest version::

    pip install colorutils --upgrade


1. Current Features
===================

**v0.2.1** (released 05/25/2015)

- Bug fix for pip install on Windows for unfound packages

**v0.2** (released 05/23/2015)

- Add HSV color representation and conversions
- Add YIQ color representation and conversions
- Color objects can be treated as iterables
- Implementation of color runs
- Addition of pre-defined color palettes
- Package restructuring

**v0.1** (released 05/16/2015)

- A versatile abstract color model which allows color addition and subtraction
- Conversions between: ``RGB`` tuples, 6-character ``HEX`` strings, 3-character ``HEX`` strings, and ``WEB`` representations of color.
- Random color generation


2. Reporting Bugs / Requesting Features
=======================================

To report a bug or request a feature for colorutils, please open a new issue_

 .. _issue: https://github.com/edaniszewski/colorutils/issues


3. Usage
========

3.1 Instantiating a ``Color``
-----------------------------

The basic way to instantiate a ``Color``::

    >>> from colorutils import Color
    >>> c = Color((255, 255, 255))
    >>> c
    <Color (255, 255, 255)>

By default, the Color object expects an ``RGB`` 3-tuple, but there are multiple ways to instantiate a ``Color``. The possibilities for Cyan, for example::

    Color((0, 255, 255))
    Color(green=255, blue=255)
    Color(rgb=(0, 255, 255))
    Color(hex='#00FFFF')
    Color(hex='00ffff')
    Color(hex='#0ff')
    Color(hex='0ff')
    Color(web='cyan')
    Color(web='Cyan')
    Color(web='CYAN')
    Color(web='#00ffff')
    Color(web='#0ff')
    Color(yiq=(0.701, -0.596, -0.217))
    Color(hsv=(180, 1, 1))

``Color`` objects can also take the color from other ``Color`` objects::

    >>> Color(Color((255, 255, 255)))
    <Color (255, 255, 255)>

    >>> Color(Color(Color(Color((255, 255, 255)))))
    <Color (255, 255, 255)>

3.2 Color Conversion
--------------------
The current color models supported by ``colorutils`` are: ``RGB``, ``HEX``, ``WEB``, ``YIQ``, and ``HSV``. Each instantiated ``Color`` object has properties which will automatically perform the required conversions::

    >>> c = Color((46, 139, 87))

    >>> c.red
    46

    >>> c.green
    139

    >>> c.blue
    87

    >>> c.rgb
    (46, 139, 87)

    >>> c.hex
    '#2e8b57'

    >>> c.shorthex
    '#2e8b57'

    >>> c.web
    'SeaGreen'

    >>> c.yiq
    (0.413, -0.152, -0.143)

    >>> c.hsv
    (146.452, 0.669, 0.545)

If the color were such that the ``HEX`` representation could be captured as a 3-char hex::

    >>> c = Color((0, 0, 0))

    >>> c.hex
    '#000000'

    >>> c.shorthex
    '#000'

The web representation will return the hex value if the color is not a well-known named web color::

    >>> c = Color((1, 243, 77))

    >>> c.hex
    '#01f34d'

    >>> c.web
    '#01f34d'

These same conversions can be done without instantiating a ``Color`` object by using the static methods:

* ``rgb_to_hex()``
* ``rgb_to_web()``
* ``rgb_to_yiq()``
* ``rgb_to_hsv()``
* ``hex_to_rgb()``
* ``hex_to_web()``
* ``hex_to_yiq()``
* ``hex_to_hsv()``
* ``web_to_rbg()``
* ``web_to_hex()``
* ``web_to_yiq()``
* ``web_to_hsv()``
* ``yiq_to_rgb()``
* ``yiq_to_hex()``
* ``yiq_to_web()``
* ``yiq_to_hsv()``
* ``hsv_to_rgb()``
* ``hsv_to_hex()``
* ``hsv_to_web()``
* ``hsv_to_yiq()``

Using these static conversion methods, one can chain conversions (due to the in-param and out-param of all multi-value color representations being a tuple), which you are unable to do using the Python default `colorsys`.::

    >>> rgb_to_hex(hex_to_rgb('#808080'))
    '#808080'

Of course, be wary of chaining. Since approximation exists in the conversion algorithms, degradation will occur::

    >>> yiq_to_web(rgb_to_yiq(hex_to_rgb('808080')))
    '#7f807e'

Though, the values will still be close::

    >>> hex(int('80', 16) - int('7f', 16))  # Red difference
    '0x1'

    >>> hex(int('80', 16) - int('80', 16))  # Green difference
    '0x0'

    >>> hex(int('80', 16) - int('7e', 16))  # Blue difference
    '0x2'

3.3 ``Color`` Arithmetic
------------------------

Although the addition and subtraction of color does not always make sense, the ability to do so is supported. There are two additive models currently supported: ``LIGHT`` and ``BLEND``.

3.3.1 Addition
~~~~~~~~~~~~~~

``LIGHT``
    the light model is an additive model, where the rgb components are added, but do not exceed the maximum value, 255. This model is the default model which every ``Color`` is initialized with, unless overridden.

An example of ``LIGHT`` addition::

    >>> Color((0, 100, 200)) + Color((100, 100, 100))
    <Color (100, 200, 255)>

``BLEND``
    the blend model is an averaging model, where each rgb component is averaged.

An example of ``BLEND`` addition::

    >>> Color((0, 100, 200), arithmetic=ArithmeticModel.BLEND) + Color((100, 100, 100))
    <Color (50, 150, 250)>

When assigning models, it is important to note that the arithmetic model for the first object in the operation, e.g. Object1 in 'Object1 + Object2', is the model which will be used when computing the addition.

``Color`` addition can also operate on 3-tuples, which represent an ``RGB`` value::

    >>> Color((50, 50, 50)) + (20, 20, 20)
    <Color (70, 70, 70)>

3.3.2 Subtraction
~~~~~~~~~~~~~~~~~

There is currently only one subtractive model, the equivalent to the inverse of the ``LIGHT`` additive model. There is no model representing the inverse of ``BLEND``, since the inverse average does not really make sense.::

    >>> Color((100, 100, 100)) - Color((0, 75, 200))
    <Color (100, 25, 0)>


``Color`` subtraction can also operate on 3-tuples, which represent an ``RGB`` value::

    >>> Color((50, 50, 50)) - (20, 20, 20)
    <Color (30, 30, 30)>


3.4 Color Equality
------------------

Testing for equality between colors defaults to testing between the equality of the ``RGB`` values::

    >>> c1 = Color((10, 20, 30))
    >>> c2 = Color((10, 20, 30))
    >>> c3 = Color((10, 20, 20))

    >>> c1 == c2
    True

    >>> c1 == c3
    False

Different equality functions can be set, using either the predefined equalities in ``colorutils.equality``, or from a custom equality function::

    >>> from colorutils.equality import *
    >>> c = Color((10, 20, 30), equality_fn=RED_eq)
    >>> c2 = Color((10, 40, 60))

    >>> c == c2
    True

    >>> c2 == c
    False

Notice that in the above example, when checking for red equality, when the color with the ``RED_eq`` equality comes first in the comparison, it
evaluates to ``True``. If it comes second, it evaluates to ``False``.  This is because the equality function of the first ``Color`` instance in
the comparison defines which equality function is used.

The predefined equalities are:

* ``RGB_eq``
* ``RED_eq``
* ``GREEN_eq``
* ``BLUE_eq``
* ``HEX_eq``
* ``WEB_eq``
* ``YIQ_eq``
* ``HSV_eq``

Defining a custom equality would follow the pattern defined by the RGB_eq definition, below::

    RGB_eq = lambda c1, c2: c1.rgb == c2.rgb


3.5 Color Palettes
------------------

A collection of pre-defined color palettes exists for convenience. The palettes which are currently implemented include:

* grayscale
* primary
* rgb
* roygbv
* secondary

Individual named colors can be used from the palettes, or all colors can be retrieved::

    >>> import colorutils.palettes.primary as primary

    >>> primary.red
    <Color (255, 0, 0)>

    >>> primary.yellow
    <Color (255, 255, 0)>

    >>> primary.blue
    <Color (0, 0, 255)>

    >>> primary.all
    [<Color (255, 0, 0)>, <Color (255, 255, 0)>, <Color (0, 0, 255)>]


4. ``colorutils`` vs others
===========================

To see how the ``colorutils`` conversion algorithms compare to other algorithms/provided values, see the comparisons_ wiki page.

 .. _comparisons: https://github.com/edaniszewski/colorutils/wiki/Comparing-Conversion-Algorithms
