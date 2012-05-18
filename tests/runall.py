import unittest

import test_pycturetube


def get_suite():
    suite_p = unittest.defaultTestLoader.loadTestsFromModule(test_pycturetube)
    suite = unittest.TestSuite([suite_p])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='get_suite')
