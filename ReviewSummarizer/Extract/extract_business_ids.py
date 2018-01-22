import pandas as pd
import json
import csv

PATH='../../Data/Orig/yelp_academic_dataset_business.json'
DEST_PATH='../../Data/bus_id_name.csv'

def create_bus_id_name_csv(min_num_of_reviews, max_num_of_businesses):
    eligible_restaurants = []
    df = pd.read_json(PATH, lines=True)
    df = json.loads(df.to_json(orient='index'))
    for key in df:
        if df[key]['review_count'] > min_num_of_reviews:
            rest = {}
            rest['id'] = df[key]['business_id']
            rest['name'] = df[key]['name']
            rest['num_of_reviews'] = df[key]['review_count']
            eligible_restaurants.append(rest)
            if(len(eligible_restaurants) == max_num_of_businesses):
                break

    keys = eligible_restaurants[0].keys()
    with open(DEST_PATH, "w", encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(eligible_restaurants)

create_bus_id_name_csv(500, 100)