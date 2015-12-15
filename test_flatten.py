from unittest import TestCase

from summarizer import flatten


class TestFlatten(TestCase):
    def test_flatten(self):
        """
        Flatten makes 2d list list into 1d. Here we are checking if it worked (so every element is str not list).
        """
        testing_list = [["list 1"], ["list 2"]]
        result_list = flatten(testing_list)
        for item in result_list:
            self.assertTrue(isinstance(item, str))

    def test_flatten_result(self):
        """
        Make sure flatten returns the right number of items
        """
        testing_list = [["list 1", "list 1"], ["list 2"]]
        result_list = flatten(testing_list)

        self.assertTrue(len(result_list) == 3)