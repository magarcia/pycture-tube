from twisted.trial import unittest

import pycturetube 
import os

HERE = os.path.dirname(__file__)

class TestPyctureTube(unittest.TestCase):
    """
    Test class for pycture-tube module.
    """

    def setUp(self):
        self.rendered = open(os.path.join(HERE, 'octocat.txt')).read()

    def test_renderify(self):
        img = pycturetube.renderify(os.path.join(HERE, 'octocat.png'))
        self.assertEqual(self.rendered, img)