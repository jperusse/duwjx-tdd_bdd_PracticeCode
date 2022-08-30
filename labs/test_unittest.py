""" Module to test increment/decreement/json """

import os
import unittest     # The test framework
import json         # json format

import inc_dec      # The code to test

class TestIncrementDecrementJson(unittest.TestCase):
    """ Test class to verify increment/decrement """

    def test_increment(self):
        """ Test increment """
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        """ Test decrement """
        self.assertEqual(inc_dec.decrement(3), 2)

    def test_open_json_file(self):
        """ Test opening a json file """
        account_data_file = 'labs/03_test_fixtures/tests/fixtures/account_data.json'
        with open(account_data_file, encoding='UTF-8') as json_data:
            account_data = json.load(json_data)
            self.assertEqual(len(account_data), 5)

            print('Current working directory: '+os.getcwd())
            print("File: "+account_data_file+" found and the first record is:")
            print(account_data[0])
            json_data.close()
    