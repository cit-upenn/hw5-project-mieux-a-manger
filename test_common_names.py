from unittest import TestCase

from summarizer import common_names


class TestCommon_names(TestCase):
    def test_common_names(self):
        """
            Our model requires that all stop words are lower cased. So these names must be as well.
        """
        for name in common_names("census-dist-2500-last.txt"):
            self.assertTrue(name.islower())

    def test_size(self):
        """
            Check if we have the right census file (to get 2500 last names)
        """
        self.assertTrue(len(common_names("census-dist-2500-last.txt")) == 2500)