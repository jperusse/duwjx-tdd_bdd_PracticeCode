""" Module to test increment/decreement/json """

import unittest     # The test framework

import inc_dec      # The code to test

class TestIncrementDecrementJson(unittest.TestCase):
    """ Test class to verify increment/decrement """

    def test_increment(self):
        """ Test increment """
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        """ Test decrement """
        self.assertEqual(inc_dec.decrement(3), 2)