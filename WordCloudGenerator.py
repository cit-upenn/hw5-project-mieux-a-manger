import os
import json
import pickle
import summarizer


def get_review_ct(business_id, business_subset="datasets/business_subset.json"):
    """
    Get the number of reviews that a business received
    :param business_subset: where to get all the business information json file
    :param business_id: the unique identifier for each business
    :return: reviews count
    """

    dataset = business_subset

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


def get_reviews(business_id, ds_txt="datasets/review_text.json"):
    """
    Get a string list of all reviews ready to process into the wordcloud.
    :param ds_txt: where to get all review texts
    :param business_id: the unique identifier for each business
    :return: list of all applicable reviews
    """

    reviews = []
    counter = 0
    with open(ds_txt, "r") as ds:
        for line in ds:
            raw = json.loads(line)
            if raw['business_id'] == business_id:
                reviews.append((raw['text']).encode('utf8'))

    return reviews


def generate_wordcloud(business_id, output_addr, ds_txt="datasets/review_text.json",
                       business_subset="datasets/business_subset.json"):
    """
    This function generates word cloud for a particular business
    :param business_subset: business subset to find business information
    :param output_addr: where to save the word cloud
    :param ds_txt: where the consolidated review json is
    :param business_id: the unique identifier for each business
    :return:
    """

    review_ct = get_review_ct(business_id, business_subset)
    reviews = get_reviews(business_id, ds_txt)
    summarizer.run(reviews, 50, output_addr)


if __name__ == "__main__":
    # folder = "/Users/user/Box Sync/yelp_dataset"
    # os.chdir(folder)

    # business_id = "pj0vl4DIlDCChe80Df40Yw"
    # review_ct = get_review_ct(business_id, "datasets/business_subset.json")
    # file = "review_text.json"
    # reviews = get_reviews("pj0vl4DIlDCChe80Df40Yw", get_review_ct("pj0vl4DIlDCChe80Df40Yw"),
    #                       "datasets/review_text.json")
    # print(reviews)

    # generate_wordcloud("pj0vl4DIlDCChe80Df40Yw", output_addr="test.jpg")
    # print get_reviews('pj0vl4DIlDCChe80Df40Yw')
    print "done"
