#!/usr/bin/env python
import os
import sys

if sys.version > '3':
    kw = {"dependency_links": ["http://github.com/sloonz/pil-py3k/tarball/master#egg=PIL"]}
else:
    kw = {"install_requires": ["PIL"]}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)

setup(
    name = "pycture-tube",
    version = '0.0.1',
    description = "pycture-tube: Render images on the terminal with xterm 256 colors.",
    author = "Martin Garcia",
    scripts = ['scripts/pycture-tube'],
    author_email = "newluxfero@gmail.com",
    license = "MIT",
    url = "https://github.com/magarcia/pycture-tube",
    packages = ["pycture-tube"],
    platforms = ["POSIX"],
    long_description = open(os.path.join(HERE, "README.md"), "r").read(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    **kw
)
