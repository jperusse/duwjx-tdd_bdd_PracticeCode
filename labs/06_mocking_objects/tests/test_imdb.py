"""
Test Cases for Mocking Lab
"""
import json
from unittest import TestCase
from unittest.mock import patch, Mock
from requests import Response
from models import IMDb

IMDB_DATA = {}

class TestIMDbDatabase(TestCase):
    """Tests Cases for IMDb Database"""

    @classmethod
    def setUpClass(cls):
        """ Load imdb responses needed by tests """
        global IMDB_DATA
#        with open('imdb_responses_fred.json',mode='r',encoding='UTF8') as json_data:
#            IMDB_DATA = json.load(json_data)
        file_stream = open('labs/06_mocking_objects/tests/fixtures/imdb_responses.json',mode='r',encoding='UTF8')


    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_hello(self):
        """ Validate test setup """
        self.assertTrue(3==3)
