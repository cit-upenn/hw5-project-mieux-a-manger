from unittest import TestCase

from summarizer import get_idf

class TestGet_idf(TestCase):
    def test_get_idf(self):
        """
          Simple test of whether the idf calculation worked
        """
        results = get_idf([["test"]])
        self.assertTrue(results["test"] == 0)

    def test_empty_input(self):
        """
            Test an edge case of empty input
        """
        results = get_idf([[]])
        self.assertTrue(len(results.keys()) == 0)