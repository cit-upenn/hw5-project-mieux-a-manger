from unittest import TestCase

from WordCloudGenerator import get_review_ct
from WordCloudGenerator import get_reviews


class TestGet_reviews(TestCase):
    def test_get_review_ct(self):
        """
            Check if the reviews are loaded
        """
        counter = get_review_ct("pj0vl4DIlDCChe80Df40Yw")
        reviews = get_reviews("pj0vl4DIlDCChe80Df40Yw", "datasets/review_text.json")
        self.assertTrue(isinstance(reviews, list))
        self.assertTrue(len(reviews) > 0)