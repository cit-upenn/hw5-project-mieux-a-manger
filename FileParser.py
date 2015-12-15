import json
import os
import random


'''
    Helper Function - truncate
'''

def truncate(ds_name):
    """
    This function wipe out data of a particular text file
    :param ds_name: the text file to truncate
    :return:
    """
    f = open(ds_name, "w")
    f.truncate()
    f.close()


'''
    Helper Function - write_file
'''

def write_file(ds_name, str_data):
    """
    This function writes a string to a json file.
    :param ds_name: the text file to write to
    :param str_data: one row of str data to write to json file
    :return:
    """
    json_data = json.loads(str_data)

    with open(ds_name, 'a') as dw:
        json.dump(json_data, dw)
        dw.write('\n')


'''
    Helper Function - get_json
'''

def get_json(ds_name):
    """
    This function turns a JSON object into a list of JSON objects
    :param ds_name: the json file to read
    :return: list of json objects
    """
    json_list = []

    for line in open(ds_name, "r"):
        try:
            json_list.append(json.loads(line))

        except EOFError:
            break

        except ValueError:
            continue

    return json_list

'''
    Helper Function - get_value_list
'''

def get_value_list(ds_list, key):
    """
    This function gets a list of certain value based on the key
    :param ds_list: list of JSON objects
    :param key: the key to find value
    :return: list of mapped values
    """
    value_list = []
    for line in ds_list:
        if key in line.keys():
            value_list.append(line[key])
    return value_list


'''
    Helper Function - get_user_score
'''

def get_user_score (category, user_id, user_data):

    """
    This function calculates the rank score of a user based on restaurant category
    :param category: the type of restaurant
    :param user_id: the user_id to look for in the user data
    :param user_data: a list of
    :return: user_id list of all selected items
    """

    for user in user_data:

        overall_score = 0
        type_score = 0

        if user['user_id'] == user_id:
            overall_score = user['rank_review']
            if category == 'Chinese':
                type_score = user['rank_cn']
            if category == 'Indian':
                type_score = user['rank_in']
            if category == 'Japanese':
                type_score = user['rank_jp']
            if category == 'Korean':
                type_score = user['rank_kr']
            if category == 'Vietnamese':
                type_score = user['rank_vn']
            if category == 'Thai':
                type_score = user['rank_th']

            return overall_score + type_score

    return 0


def getds_business(ds_src, ds_des, min_star, min_review, city, categories):
    """
    This function generate the preliminary business dataset based on raw data.
    :param ds_src: the source dataset name
    :param ds_des: the destination dataset name
    :param min_star: the minimum star rating above which we select
    :param min_review: the review count above which we select
    :param city: the city in which we select business
    :param categories: restaurant categories that we look into
    :return:
    """
    truncate(ds_des)

    with open(ds_src, "r") as ds:
        while True:
            try:
                raw = json.loads(ds.readline())

                for category in categories:
                    if category in raw['categories']:
                        if  raw['review_count'] > min_review and \
                            raw['stars'] >= min_star and \
                            raw['city'] == city and \
                            'Restaurants' in raw['categories']:

                            biz_str = '{"name": "' + raw['name'] + \
                                      '", "business_id": "' + raw['business_id'] + \
                                      '", "review_count": ' + str(raw['review_count']) + \
                                      ', "stars": ' + str(raw['stars']) + \
                                      ', "city": "' + raw['city'] + \
                                      '", "category": "' + category + \
                                      '", "type": "' + raw['type'] + \
                                      '"}'

                            write_file(ds_des, biz_str)

                            break

            except EOFError:
                break

            except ValueError:
                continue

def getds_review(ds_src, ds_des, ds_biz):
    """
    This function generates the preliminary review dataset based on raw data
    :param ds_src: the source dataset name
    :param ds_des: the destination dataset name
    :param ds_biz: the business dataset whose items we look reviews for
    :return:
    """
    truncate(ds_des)

    biz_data = get_json(ds_biz)
    biz_id_list = get_value_list(biz_data, "business_id")

    with open(rev_raw, "r") as ds:
        while True:
            try:
                raw = json.loads(ds.readline())
                if raw['business_id'] in biz_id_list:
                    rev_str = '{"business_id": "' + raw['business_id'] + \
                              '", "review_id": "' + raw['review_id'] + \
                              '", "stars": ' + str(raw['stars']) + \
                              ', "user_id": "' + raw['user_id'] + \
                              '", "text": "' + raw['text'] + \
                              '"}'

                    write_file(ds_des, rev_str)

            except EOFError:
                break

            except ValueError:
                continue


def getds_user(ds_src, ds_des, ds_rev):
    """
    This function generates preliminary user dataset based on raw data
    :param ds_src: the source dataset name
    :param ds_des: the destination dataset name
    :param ds_rev: the review dataset whose items we look unique users for
    :return:
    """
    truncate(ds_des)

    user_data = get_json(ds_rev)
    user_list = get_value_list(user_data, "user_id")

    i = 0
    with open(use_raw, "r") as ds:
        while (i < len(user_list)):
            try:
                raw = json.loads(ds.readline())
                if raw['user_id'] in user_list:

                    use_str = '{"user_id": "' + raw['user_id'] + \
                              '", "name": "' + raw['name'] + \
                              '", "review_count": ' + str(raw['review_count']) + \
                              ', "average_stars": ' + str(raw['average_stars']) + \
                              ', "type": "' + raw['type'] + \
                              '"}'

                    write_file(ds_des, use_str)
                    i += 1

            except EOFError:
                break

            except ValueError:
                continue


def rank_user(ds_name):
    """
    This function provides rank scores of each restaurant category for each user
    :param ds_name: the user dataset to rank
    :return:
    """

    lines = []
    for line in open(ds_name, "r"):
        lines.append(json.loads(line))
    lines.sort(key = lambda k: (k['review_count']))

    truncate(ds_name)

    rand_ls_cn = list(range(len(lines)))
    rand_ls_in = list(range(len(lines)))
    rand_ls_jp = list(range(len(lines)))
    rand_ls_kr = list(range(len(lines)))
    rand_ls_vn = list(range(len(lines)))
    rand_ls_th = list(range(len(lines)))

    random.shuffle(rand_ls_cn)
    random.shuffle(rand_ls_in)
    random.shuffle(rand_ls_jp)
    random.shuffle(rand_ls_kr)
    random.shuffle(rand_ls_vn)
    random.shuffle(rand_ls_th)

    rank_review = 0
    with open(ds_name, 'a') as dw:
        for raw in lines:
            rank_cn = rand_ls_cn.pop()
            rank_in = rand_ls_in.pop()
            rank_jp = rand_ls_jp.pop()
            rank_kr = rand_ls_kr.pop()
            rank_vn = rand_ls_vn.pop()
            rank_th = rand_ls_th.pop()

            use_str =   '{"user_id": "' + raw['user_id'] + \
                        '", "name": "' + raw['name'] + \
                        '", "review_count": ' + str(raw['review_count']) + \
                        ', "average_stars": ' + str(raw['average_stars']) + \
                        ', "rank_review": ' + str(rank_review) + \
                        ', "rank_cn": ' + str(rank_cn) + \
                        ', "rank_in": ' + str(rank_in) + \
                        ', "rank_jp": ' + str(rank_jp) + \
                        ', "rank_kr": ' + str(rank_kr) + \
                        ', "rank_vn": ' + str(rank_vn) + \
                        ', "rank_th": ' + str(rank_th) + \
                        ', "type": "' + raw['type'] + \
                        '"}'

            write_file(ds_name, use_str)
            rank_review += 1


def update_business_score(ds_biz, ds_rev, ds_user):
    """
    This function updates the score of each business based on rank score of users who reviewed them
    :param ds_biz: the business dataset to update
    :param ds_rev: the reviews dataset that the selected business received
    :param ds_user: the user dataset who provided reviews for each business
    :return:
    """

    biz_list = get_json(ds_biz)
    rev_list = get_json(ds_rev)
    use_list = get_json(ds_user)

    truncate(biz_sub)

    for biz in biz_list:

        biz_id = biz['business_id']
        category = biz['category']
        review_ct = biz['review_count']

        rank_score = 0

        for rev in rev_list:
            if rev['business_id'] == biz_id:
                review_score = rev['stars']
                user_id = rev['user_id']

                user_score = get_user_score(category, user_id, use_list)
                if user_score ==0:
                    print("not found")

                rank_score += review_score*user_score

        rank_score = rank_score/review_ct

        biz_str = '{"name": "' + biz['name'] + \
                  '", "business_id": "' + biz['business_id'] + \
                  '", "review_count": ' + str(biz['review_count']) + \
                  ', "stars": ' + str(biz['stars']) + \
                  ', "rank_score": ' + str(rank_score) + \
                  ', "city": "' + biz['city'] + \
                  '", "category": "' + category + \
                  '", "type": "' + biz['type'] + \
                  '"}'

        write_file(biz_sub, biz_str)


def get_top_biz (top_num, categories, ds_biz, ds_outcome):
    """
    This function ranks selected businesses and generate a new JSON file with ranked business of each category
    :param top_num: how many restaurants of each category to keep
    :param categories: lis of restaurant categories
    :param ds_biz: business dataset
    :param ds_outcome: new JSON file to store ranked restaurants
    :return:
    """

    biz_list = get_json(ds_biz)
    cat_biz = []

    truncate(ds_outcome)

    for category in categories:
        for biz in biz_list:
            if 'category' in biz.keys():
                if biz['category'] == category:
                    cat_biz.append(biz)
        cat_biz.sort(key = lambda k: (k['rank_score']), reverse = True)

        for i in range(top_num):
            biz = cat_biz[i]
            biz_str = '{"name": "' + biz['name'] + \
                  '", "business_id": "' + biz['business_id'] + \
                  '", "rank_score": ' + str(biz['rank_score']) + \
                  ', "category": "' + category + \
                  '"}'

            write_file(ds_outcome, biz_str)
        cat_biz = []



def get_text_review (ds_biz, rev_raw, ds_txt):
    """
    This function gets all text reviews received for ranked restaurants; will use later for word cloud
    Data errors of json.decoder.JSONDecodeError or ValueError are ignored at this stage of project
    :param ds_biz: business dataset
    :param rev_raw: raw review dataset
    :param ds_txt: new JSON file to store text reviews
    :return:
    """

    biz_data = get_json(ds_biz)
    biz_id_list = get_value_list(biz_data, "business_id")

    truncate(ds_txt)

    with open(rev_raw, "r") as ds:
        while True:
            try:
                raw = json.loads(ds.readline())

                if 'business_id' in raw.keys():
                    if raw['business_id'] in biz_id_list:
                        rev_str = '{"business_id": "' + raw['business_id'] + \
                                  '", "text": "' + raw['text'] + \
                                  '"}'

                        write_file(ds_txt, rev_str)

            except EOFError:
                break

            except ValueError:
                continue

            except json.decoder.JSONDecodeError:
                continue


if __name__ == '__main__':

    # """
    # Get all three datasets
    # """
    # folder = "/Users/user/Box Sync/yelp_dataset"
    # os.chdir(folder)
    #
    # biz_raw = "yelp_academic_dataset_business.json"
    # biz_sub = 'business_subset.json'
    # rev_raw = 'yelp_academic_dataset_review.json'
    # rev_sub = "review_subset.json"
    # use_raw = 'yelp_academic_dataset_user.json'
    # use_sub = "user_subset.json"
    # rank_outcome = "rank_outcome.json"
    # rev_txt = "review_text.json"
    #
    # categories = ['Chinese', 'Indian', 'Japanese', 'Korean', 'Vietnamese', 'Thai']
    # city = 'Las Vegas'
    #
    # getds_business(biz_raw, biz_sub, 4.0, 100, city, categories)
    # print ("Qualified business data parsed to :" + biz_sub)
    #
    # getds_review(rev_raw, rev_sub, biz_sub)
    # print ("Qualified review data parsed to :" + rev_sub)
    #
    # getds_user(use_raw, use_sub, rev_sub)
    # print ("Qualified user data parsed to :" + use_sub)
    #
    # rank_user(use_sub)
    # print ("User data ranked")
    #
    # update_business_score(biz_sub, rev_sub, use_sub)
    #
    # get_top_biz(5, categories, biz_sub, rank_outcome)
    #
    # get_text_review(rank_outcome, rev_raw, rev_txt)
    print "done"