from unittest import TestCase

from web_builder import format_file_for_web


class TestFormat_file_for_web(TestCase):
    def test_format_file_for_web(self):
        """
            Make sure the output file has the right format - 2d array
        """
        test_file = "datasets/rank_outcome.json"
        output = format_file_for_web(test_file)
        for item in output:
            self.assertTrue(isinstance(item, list))
