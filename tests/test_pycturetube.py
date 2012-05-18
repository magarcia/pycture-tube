import unittest
import sys

sys.path = ['../pycture-tube', './pycture-tube'] + sys.path

import pycturetube
import os

HERE = os.path.dirname(__file__)


class TestPyctureTube(unittest.TestCase):
    """
    Test class for pycture-tube module.
    """

    def setUp(self):
        f = open(os.path.join(HERE, 'octocat.txt'))
        self.rendered = f.read()
        f.close()

    def test_renderify(self):
        img = pycturetube.renderify('https://github.com/magarcia/pycture-tube/raw/master/tests/octocat.png')
        self.assertEqual(self.rendered, img)
