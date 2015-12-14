import json
import os
import random


'''
    Helper Function - truncate
'''

def truncate(ds_name):
    """
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
    :param ds_name: the text file to write to
    :param str_data: one row of str data to write to json file
    :return:
    """
    json_data = json.loads(str_data)
    with open(ds_name, 'a') as dw:
        json.dump(json_data, dw)
        dw.write('\n')


'''
    Helper Function - get_biz_list
'''

def get_biz_list(ds_name):
    """
    :param ds_name: the text file to read
    :return: business_id list of all selected items
    """
    biz_id_list = []

    for line in open(ds_name, "r"):
        try:
            str = json.loads(line)
            biz_id_list.append(str["business_id"])

        except EOFError:
            break

        except ValueError:
            continue

    return biz_id_list


'''
    Helper Function - get_user_list
'''

def get_user_list(ds_name):
    """
    :param ds_name: the text file to read
    :return: user_id list of all selected items
    """

    user_list = []

    for line in open(ds_name, "r"):
        try:
            raw = json.loads(line)
            user_list.append(raw['user_id'])

        except EOFError:
            break

        except ValueError:
            continue

    user_list = list(set(user_list))

    return user_list



def getds_business(ds_src, ds_des, min_star, min_review, city, categories):
    """
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
    :param ds_src: the source dataset name
    :param ds_des: the destination dataset name
    :param ds_biz: the business dataset whose items we look reviews for
    :return:
    """
    truncate(ds_des)

    biz_id_list = get_biz_list(ds_biz)

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
    :param ds_src: the source dataset name
    :param ds_des: the destination dataset name
    :param ds_rev: the review dataset whose items we look unique users for
    :return:
    """
    truncate(ds_des)

    user_list = get_user_list(ds_rev)

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
    :param ds_name: the user dataset to rank
    :return:
    """

    lines = []
    for line in open(ds_name, "r"):
        lines.append(json.loads(line))
    lines.sort(key = lambda k: (k['review_count']), reverse = True)

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


if __name__ == '__main__':

    """
    Get all three datasets
    """
    folder = "/Users/user/Box Sync/yelp_dataset"
    os.chdir(folder)

    biz_raw = "yelp_academic_dataset_business.json"
    biz_sub = 'business_subset.json'
    rev_raw = 'yelp_academic_dataset_review.json'
    rev_sub = "review_subset.json"
    use_raw = 'yelp_academic_dataset_user.json'
    use_sub = "user_subset.json"

    categories = ['Chinese', 'Indian', 'Japanese', 'Korean', 'Vietnamese', 'Thai']
    city = 'Las Vegas'

    getds_business(biz_raw, biz_sub, 4.0, 100, city, categories)
    getds_review(rev_raw, rev_sub, biz_sub)
    getds_user(use_raw, use_sub, rev_sub)
    rank_user(use_sub)
