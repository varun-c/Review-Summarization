import pandas as pd
import json
import csv

REVIEWS_PATH='../../Data/Orig/yelp_academic_dataset_review.json'
BUS_ID_PATH='../../Data/bus_id_name.csv'
DEST_PATH = '../../Data/reviews.csv'
def create_reviews(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ):
    extracted_reviews = []
    # Extract list of restaurants
    bus_ids = {}
    reader = csv.reader(open(BUS_ID_PATH))
    bus_ids = {}
    is_key_row = True
    for row in reader:
        if is_key_row:
            for index, key in enumerate(row):
                if key == 'id':
                    key_index = index
                elif key == 'num_of_reviews':
                    val_index = index
            is_key_row = False
        else:
            bus_ids[row[key_index]] = row[val_index]
    count = 0

    with open(REVIEWS_PATH, 'r') as f:
        for line in f:
            count += 1
            print (count)
            j = json.loads(line)
            if j['business_id'] in bus_ids:
                rest = {}
                rest['id'] = j['business_id']
                rest['text'] = j['text']
                rest['stars'] = j['stars']
                extracted_reviews.append(rest)

    keys = extracted_reviews[0].keys()
    with open(DEST_PATH, "w", encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(extracted_reviews)

create_reviews()