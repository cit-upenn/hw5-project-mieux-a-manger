import json

from unittest import TestCase

from FileParser import get_value_list

class TestGet_value_list(TestCase):
  def test_get_value_list_value(self):
    """
    Make sure the function only takes the value of the specified key
    """
    test_data = []
    test_data.append(json.loads('{"name": "Pat"}'))
    test_data.append(json.loads('{"last_name": "Nat"}'))

    key = "name"
    result_list = get_value_list(test_data, key)
    self.assertTrue(result_list == ['Pat'])

  def test_get_value_list_result(self):
    """
    Make sure the function gets all qualified values
    """
    test_data = []
    test_data.append(json.loads('{"name": "Pat"}'))
    test_data.append(json.loads('{"last_name": "Nat"}'))
    test_data.append(json.loads('{"name": "Gwen"}'))

    key = "name"
    result_list = get_value_list(test_data, key)
    self.assertTrue(len(result_list) == 2)