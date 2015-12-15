import json
from unittest import TestCase

from web_builder import write_formatted_list_to_json_str


class TestWrite_formatted_list_to_json_str(TestCase):
    def test_write_formatted_list_to_json_str(self):
        """
        Test if our write_formatted_list_to_json_str indeed outputs a valid json string
        """
        raised = False
        try:
            test = write_formatted_list_to_json_str([['category', '1', 'name', 'picture_addr', '3']])
            json.loads(test)
        except:  # broad exception allowed here
            raised = True
        self.assertFalse(raised, 'Exception raised')
