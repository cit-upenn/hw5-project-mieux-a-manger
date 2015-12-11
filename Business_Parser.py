import os
import json

folder = "/Users/user/Box Sync/yelp_dataset"
biz_raw = "yelp_academic_dataset_business.json"
biz_spl = 'business_sample.json'

os.chdir(folder)

with open(biz_raw, "r") as ds:

    f = open(biz_spl, "w")
    f.truncate()
    f.close()

    i = 0
    while (i < 10):
        raw = json.loads(ds.readline())

        if raw['review_count'] > 100 and ('Chinese' in raw['categories']) and ('Restaurants' in raw['categories']):
            biz_str = '{"name": "' + raw['name'] + \
                      '", "business_id": "' + raw['business_id'] + \
                      '", "review_count": ' + str(raw['review_count']) + \
                      ', "stars": ' + str(raw['stars']) + \
                      ', "city": "' + raw['city'] + \
                      '", "category": "' + 'Chinese' + \
                      '", "type": "' + raw['type'] + \
                      '"}'

            biz_json = json.loads(biz_str)

            with open(biz_spl, 'a') as dw:
                json.dump(biz_json, dw)
                dw.write('\n')
            i += 1
