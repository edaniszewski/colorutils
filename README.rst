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
represented in ``RGB``, ``HEX``, and ``WEB`` formats.

0. Installation
===============

``colorutils`` can be installed from pypi::

    pip install colorutils
    
to update an existing installation from pypi to the latest version::

    pip install colorutils --upgrade


1. Current Features
===================

**v0.2** (in development)

- Color objects can be treated as iterables
- Implementation of color runs
- Addition of pre-defined color palettes
- Package restructuring

**v0.1** (released)

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

There are multiple ways to instantiate a ``Color``. The possibilities for Cyan, for example::

    Color((0, 255, 255))
    Color(green=255, blue=255)
    Color(rgb=(0, 255, 255))
    Color(hex='#00FFFF')
    Color(hex='00ffff')
    Color(hex='#0ff')
    Color(hex='0ff')
    Color(web='cyan')
    Color(web='Cyan')
    Color(web='#00ffff')
    Color(web='#0ff')

``Color`` objects can also take the color from other ``Color`` objects::

    >>> Color(Color((255, 255, 255)))
    <Color (255, 255, 255)>

    >>> Color(Color(Color(Color((255, 255, 255)))))
    <Color (255, 255, 255)>

3.2 Color Conversion
--------------------
The current color models supported by ``colorutils`` are: ``RGB``, ``HEX``, and ``WEB``. Each instantiated ``Color`` object has properties which will automatically perform the required conversions::

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
* ``hex_to_rgb()``
* ``hex_to_web()``
* ``web_to_rbg()``
* ``web_to_hex()``


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


3.4 Color Palettes
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

