from unittest import TestCase

from summarizer import get_stopwords


class TestGet_stopwords(TestCase):
    census_last_name = "census-dist-2500-last.txt"
    census_first_female = "census-dist-female-first.txt"
    census_first_male = "census-dist-male-first.txt"

    def test_get_stopwords(self):
        """
            Check robustness of the stop list by check some typical stop words
        """

        stop_list = get_stopwords(self.census_last_name, self.census_first_female, self.census_first_male)

        # Manually define some stop words to test the robustness. Must be lowercase
        test_list = ["restaurant", "the", "is", "smith"]
        for stop_word in test_list:
            self.assertTrue(stop_word in stop_list)

    def test_dups(self):
        """
            Make sure there is no duplicates in the stop list.
        """
        results = get_stopwords(self.census_last_name, self.census_first_female, self.census_first_male)
        delta = len(results) - len(set(results))
        self.assertTrue(delta == 0)