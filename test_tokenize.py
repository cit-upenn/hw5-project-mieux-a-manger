from unittest import TestCase

from summarizer import tokenize


class TestTokenize(TestCase):
    def test_tokenize(self):
        """
          Test if tokenize output is unicode
        """
        for token in tokenize("testing file"):
            self.assertTrue(isinstance(token, str))

    def test_tokenize_results(self):
        """
          Test if tokenize output is what we want
        """
        list_out = tokenize("testing file")
        self.assertTrue(list_out[0] == "testing")
        self.assertTrue(list_out[1] == "file")