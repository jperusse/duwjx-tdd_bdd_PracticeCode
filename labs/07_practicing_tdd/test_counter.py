"""
Test Cases for Counter Web Service
"""
from unittest import TestCase
import status
from counter import app

class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        """create an instance of  a test client"""
        self.client = app.test_client()

    def new_counter_name(self, counter_name):
        """format a counter name"""
        new_counter = "/counters/"+counter_name
        return new_counter

    def make_a_counter(self,counter_name):
        """counter creator function"""
        new_counter = self.new_counter_name(counter_name)
        result = self.client.post(new_counter)
        return result

    def test_create_a_counter(self):
        """It should create a counter"""
        counter_name = "foo"
        result = self.make_a_counter(counter_name)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn(counter_name, data)
        self.assertEqual(data[counter_name], 0)


    def test_duplicate_counter(self):
        """It should return an error for duplicates"""
        counter_name = "bar"
        result = self.make_a_counter(counter_name)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        counter_name = "bar"
        result = self.make_a_counter(counter_name)
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """It should update a counter with the given data"""
        counter_name = "baz"

        # create a counter
        result = self.make_a_counter(counter_name)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        baseline = data[counter_name]

        # update the counter
        new_counter = self.new_counter_name(counter_name)
        result = self.client.put(new_counter)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        update = data[counter_name]
        self.assertEqual(update, baseline + 1)

    def test_delete_a_counter(self):
        """It should delete a counter"""
        counter_name = "bum"

        # create a counter
        result = self.make_a_counter(counter_name)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        # delete the counter
        new_counter = self.new_counter_name(counter_name)
        result = self.client.delete(new_counter)
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_missing_counter(self):
        """It should fail with a 404 due to a missing counter"""
        counter_name = "bim"

        # update the counter

        new_counter = self.new_counter_name(counter_name)
        result = self.client.put(new_counter)
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)


    def test_read_a_counter(self):
        """It should read a counter"""
        counter_name = "bang"

        # create a counter
        result = self.make_a_counter(counter_name)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        baseline = data[counter_name]

        # update the counter
        new_counter = self.new_counter_name(counter_name)
        result = self.client.put(new_counter)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        update = data[counter_name]
        self.assertEqual(update, baseline + 1)

        # read the counter
        new_counter = self.new_counter_name(counter_name)
        result = self.client.get(new_counter)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        get = data[counter_name]
        self.assertEqual(get, update)

    def test_read_a_missing_counter(self):
        """It should fail with a 404 due to a missing counter"""
        counter_name = "bummer"

        # read the counter

        new_counter = self.new_counter_name(counter_name)
        result = self.client.put(new_counter)
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
