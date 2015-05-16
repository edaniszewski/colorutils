==========
colorutils
==========

A library which provides utilities for working with colors in Python. Colors are modeled by the ``Color`` class and can be
represented in ``RGB``, ``HEX``, and ``WEB`` formats.


Current Features
================

**v0.1**

- A versatile abstract color model which allows color addition and subtraction
- Conversions between: ``RGB`` tuples, 6-character ``HEX`` strings, 3-character ``HEX`` strings, and ``WEB`` representations of color.
- Random color generation


Reporting Bugs / Requesting Features
====================================

To report a bug or request a feature for colorutils, please open a new issue here: https://github.com/edaniszewski/colorutils/issues


Example Usage
=============

Instantiating a ``Color``
-------------------------

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

``Color`` objects can also take the color from other ``Color``s::

    >>> Color(Color((255, 255, 255)))
    <Color (255, 255, 255)>

    >>> Color(Color(Color(Color((255, 255, 255)))))
    <Color (255, 255, 255)>

``Color`` Addition and Subtraction
----------------------------------

Although the addition and subtraction of color does not always make sense, the ability to do so is supported. There are two additive models currently supported: ``LIGHT`` and ``BLEND``.

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

There is currently only one subtractive model, the equivalent to the inverse of the ``LIGHT`` additive model. There is no model representing the inverse of ``BLEND``, since the inverse average does not really make sense.::

    >>> Color((100, 100, 100)) - Color((0, 75, 200))
    <Color (100, 25, 0)>


``Color`` objects can also be added and subtracted from 3-tuples, which represent an ``RGB`` value::

    >>> Color((50, 50, 50)) + (20, 20, 20)
    <Color (70, 70, 70)>
    >>> Color((50, 50, 50)) - (20, 20, 20)
    <Color (30, 30, 30)>
