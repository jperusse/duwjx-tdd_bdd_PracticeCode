""" Module to test increment/decreement """

import unittest   # The test framework
import inc_dec    # The code to test

class TestIncrementDecrement(unittest.TestCase):
    """ Test class to verify increment/decrement """

    def test_increment(self):
        """ Test increment """
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        """ Test decrement """
        self.assertEqual(inc_dec.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()
    