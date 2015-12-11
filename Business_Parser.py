import os
import json

folder = "/Users/ecuser/Downloads/yelp_dataset"
biz_raw = "yelp_academic_dataset_business.json"
biz_sub = 'business_subset.json'
categories = ['Chinese', 'Indian', 'Japanese', 'Korean', 'Vietnamese', 'Thai']
city = 'Las Vegas'

os.chdir(folder)

i = 0
with open(biz_raw, "r") as ds:

    f = open(biz_sub, "w")
    f.truncate()
    f.close()

    while True:
        try:
            raw = json.loads(ds.readline())

            for category in categories:
                if category in raw['categories']:
                    if  raw['review_count'] > 100 and \
                        raw['stars'] >= 4.0 and \
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

                        biz_json = json.loads(biz_str)

                        with open(biz_sub, 'a') as dw:
                            json.dump(biz_json, dw)
                            dw.write('\n')

                        i += 1
                        break

            print(i + ' business records found')

        except EOFError:
            break

        except ValueError:
            break



