# json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
# d = {
#     'first_name': 'Yibang',
#     'second_name': 'Chen',
#     'titles': ['Google', 'Developer'],
# }
#
# import json
# parsed_json = json.loads(json_string)
#
# print(parsed_json['first_name'])
# name = d['second_name'] + ', ' +  d['first_name']
# print(name)

import os
import json


biz_spl = 'business_sample.json'
rev_raw = 'yelp_academic_dataset_review.json'
rev_spl = "review_sample.json"
folder = "/Users/user/Box Sync/yelp_dataset"

os.chdir(folder)

f = open(rev_spl, "w")
f.truncate()
f.close()

biz_id_list = []
review_num = 0
for line in open(biz_spl, "r"):
    biz_str = json.loads(line)
    biz_id_list.append(biz_str["business_id"])
    review_num += biz_str["review_count"]

print(biz_id_list)
print(review_num)

i = 0
with open(rev_raw, "r") as ds:
    while (i < review_num):
        raw = json.loads(ds.readline())
        if raw['business_id'] in biz_id_list:
            rev_str = '{"business_id": "' + raw['business_id'] + \
                      '", "review_id": "' + raw['review_id'] + \
                      '", "stars": ' + str(raw['stars']) + \
                      ', "user_id": "' + raw['user_id'] + \
                      '", "date": "' + raw['date'] + \
                      '"}'

            rev_json = json.loads(rev_str)
            with open(rev_spl, 'a') as dw:
                json.dump(rev_json, dw)
                dw.write('\n')
            i += 1

