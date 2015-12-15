from unittest import TestCase

from summarizer import build_vector


class TestBuild_vector(TestCase):
    def test_build_vector(self):
        """
            Test if stop words are correctly removed from results
        """
        corpus = ["Testing corpus."]
        stoplist = ["corpus"]
        results = build_vector(corpus, stoplist)
        for stop_word in stoplist:
            self.assertTrue(stop_word not in results.keys())

    def test_result(self):
        """
            Check if the vector contains all given tokens.
        """
        corpus = ["Again corpus."]
        stoplist = []
        results = build_vector(corpus, stoplist)

        self.assertTrue(len(results.keys()) == 2)
