#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)

setup(name = "pycture-tube",
    version = '0.0.1',
    description = "pycture-tube: Render images on the terminal with xterm 256 colors.",
    author = "Martin Garcia",
    scripts = ['scripts/pycture-tube'],
    author_email = "newluxfero@gmail.com",
    license = "MIT",
    url = "https://github.com/magarcia/pycture-tube",
    packages = ["pycture-tube"],
    platforms = ["POSIX", "Windows"],
    long_description = open(os.path.join(HERE, "README.md"), "r").read(),
    install_requires=["Twisted", "Image"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ],
)
