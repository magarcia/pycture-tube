#! /usr/bin/env python

from x256 import x256
from optparse import OptionParser
import Image
import sys

if sys.version > '3':
    from io import BytesIO as StringIO
    import urllib.request as urllib
else:
    import urllib
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO


def renderify(filename, cols=80):
    """
    Render images on the terminal with xterm 256 colors.
    """
    try:
        url = urllib.urlopen(filename)
        im = StringIO(url.read())
        im = Image.open(im)
        url.close()
    except:
        im = Image.open(filename)

    im.mode == 'RGBA'
    width, height = im.size
    dx = float(width) / cols
    dy = 2 * dx
    pixels = im.load()

    buff = ''
    y = 0
    while (y < height):
        x = 0
        while (x < width):
            i = round(x - 0.5) if x != 0 else x
            j = round(y - 0.5) if y != 0 else y
            if (len(pixels[i, j]) == 3) or (pixels[i, j][3] > 0):
                color = x256.from_rgb(list(pixels[i, j])[0:3])
                buff += '\033[48;5;%dm \033[0m' % color
            else:
                buff += ' '
            x += dx
        buff += '\n'
        y += dy
    return buff


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-c", "--cols", default=80, type="int", dest="cols",
                      help="Set the columns to print")

    (options, args) = parser.parse_args()

    if len(args) >= 1:
        for i in args:
            print(renderify(i, options.cols))
