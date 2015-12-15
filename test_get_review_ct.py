from unittest import TestCase

from WordCloudGenerator import get_review_ct


class TestGet_review_ct(TestCase):
    def test_get_review_ct(self):
        """
            Check if there is no negative number of reviews
        """
        counter = get_review_ct("pj0vl4DIlDCChe80Df40Yw")
        self.assertTrue(counter >= 0)
