#!/usr/bin/env python

from setuptools import setup
import os
import colorutils


if os.path.exists('README.rst'):
    description_long = open('README.rst').read()
else:
    description_long = """ A utility which allows you to work with colors in Python. """


setup(
    name='colorutils',
    packages=['colorutils'],
    version=colorutils.__version__,
    license=colorutils.__license__,
    description=colorutils.__description__,
    long_description=description_long,
    author=colorutils.__author__,
    author_email=colorutils.__email__,
    url='https://github.com/edaniszewski/colorutils',
    download_url='https://github.com/edaniszewski/colorutils/releases/tag/0.1',
    keywords=['color', 'color manipulation', 'color conversion', 'color tools'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
)