from collections import Counter
from unittest import TestCase

from summarizer import get_tf


class TestGet_tf(TestCase):
    def test_get_tf(self):
        """
         get_tf method is very straight forward. So we just need to check if the counter worked.
        """
        tf_result = get_tf(["token1", "token2", "token1", "token3"])
        self.assertTrue(tf_result["token1"] == 2)
