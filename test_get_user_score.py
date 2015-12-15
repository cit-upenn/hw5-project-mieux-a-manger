import json

from unittest import TestCase

from FileParser import get_user_score


class TestGet_user_score(TestCase):
  def test_get_user_score(self):
    """
    To ensure that the function returns the sum of 2 ranks
    """
    category = "Chinese"
    user_id = "223ABC"

    user_data = []
    user_data.append(json.loads('{"user_id": "123ABC", "rank_review": 9, "rank_cn":12}'))
    user_data.append(json.loads('{"user_id": "223ABC", "rank_review": 11, "rank_cn":15}'))

    result = get_user_score(category, user_id, user_data)

    self.assertTrue(result == 26)

  def test_get_user_score_unmatched(self):
    """
    To ensure that the function returns 0 when user_id is unmatched
    """
    category = "Chinese"
    user_id = "323ABC"

    user_data = []
    user_data.append(json.loads('{"user_id": "123ABC", "rank_review": 9, "rank_cn":12}'))
    user_data.append(json.loads('{"user_id": "223ABC", "rank_review": 11, "rank_cn":15}'))

    result = get_user_score(category, user_id, user_data)

    self.assertTrue(result == 0)
