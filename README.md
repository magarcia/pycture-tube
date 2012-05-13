[![Build Status](https://secure.travis-ci.org/magarcia/pycture-tube.png?branch=master)](http://travis-ci.org/magarcia/pycture-tube)
Picture-tube
============

*This is a python version from [picture-tube](https://github.com/substack/picture-tube)*

Render images on the terminal with xterm 256 colors.

Example
=======

Command
-------

![pycturetube octocat](https://github.com/magarcia/pycture-tube/raw/master/screenshots/octocat.png)
Code
----

    import pycturetube
    buf = picturetube.renderify('/path/to/image.png')
    print buf


Usage
=====

    Usage: pycture-tube [options]

    Options:
      -h, --help            show this help message and exit
      -c COLS, --cols=COLS  Set the columns to print



Methods
=======

pycturetube.renderify(filename, cols=80)
-------------------------------------

Return a string with the image rendered for terminal x256 colors.


Install
=======

    pip install -e git://github.com/magarcia/python-x256.git#egg=x256
    python setup.py install


License
=======

Copyright (c) 2012 Martin Garcia (newluxfero@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.