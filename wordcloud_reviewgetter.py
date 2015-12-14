import os
import json
import pickle


def get_review_ct (business_id):

    """
    Get the number of reviews that a business received
    :param business_id: the unique identifier for each business
    :return: reviews count
    """

    dataset = "business_subset.json"

    with open(dataset, "r") as db:
        while True:
            try:
                doc = json.loads(db.readline())
                if doc['business_id'] == business_id:
                    return doc['review_count']

            except EOFError:
                return 0

            except ValueError:
                return 0

def get_reviews (business_id, review_ct):

    """
    Get a string list of all reviews ready to process into the wordcloud.
    :param business_id: the unique identifier for each business
    :param review_ct: count of reviews of a particular business
    :return: list of all applicable reviews
    """

    reviews = []

    dataset = "review_subset_test.json"

    i = 0
    with open(dataset, "r") as ds:
        while i < review_ct:
            raw = json.loads(ds.readline())
            reviews.append(raw['text'])
            i += 1

    pickle.dump(reviews, open("reviews_1.p", "wb"))

    return reviews

if __name__ == "__main__":

    folder = "/Users/user/Box Sync/yelp_dataset"
    os.chdir(folder)

    business_id = "pj0vl4DIlDCChe80Df40Yw"
    review_ct = get_review_ct(business_id)
    print (business_id, review_ct)