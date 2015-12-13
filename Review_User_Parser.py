import os
import json


user_sub = 'user_subset.json'
rev_raw = 'yelp_academic_dataset_review.json'
rev_sub_u = "review_user_subset.json"
folder = "/Users/ecuser/Downloads/yelp_dataset"

os.chdir(folder)

f = open(rev_sub_u, "w")
f.truncate()
f.close()

user_id_list = []
# review_num = 0
for line in open(user_sub, "r"):
    use_str = json.loads(line)
    user_id_list.append(use_str["user_id"])
    # review_num += biz_str["review_count"]

with open(rev_raw, "r") as ds:
    while True:
        try:
            raw = json.loads(ds.readline())
            if raw['user_id'] in user_id_list:
                rev_str = '{"business_id": "' + raw['business_id'] + \
                          '", "review_id": "' + raw['review_id'] + \
                          '", "stars": ' + str(raw['stars']) + \
                          ', "user_id": "' + raw['user_id'] + \
                          '", "date": "' + raw['date'] + \
                          '"}'

                rev_json = json.loads(rev_str)
                with open(rev_sub_u, 'a') as dw:
                    json.dump(rev_json, dw)
                    dw.write('\n')

        except EOFError:
            break

        except ValueError:
            break