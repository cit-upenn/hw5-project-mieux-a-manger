import os
import json

rev_spl = "review_sample.json"
use_spl = "user_sample.json"
use_raw = 'yelp_academic_dataset_user.json'
folder = "/Users/user/Box Sync/yelp_dataset"

os.chdir(folder)

f = open(use_spl, "w")
f.truncate()
f.close()

user_list = []
for line in open(rev_spl, "r"):
    raw = json.loads(line)
    user_list.append(raw['user_id'])
user_list = list(set(user_list))

i = 0
with open(use_raw, "r") as ds:
    while (i < len(user_list)):
        raw = json.loads(ds.readline())
        if raw['user_id'] in user_list:
            with open(use_spl, 'a') as dw:
                json.dump(raw, dw)
                dw.write('\n')
            i += 1
