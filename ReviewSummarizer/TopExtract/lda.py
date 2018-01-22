from nltk.corpus import stopwords
import pandas as pd

def extract_topics():
    DATA = '../../Data/reviews.csv'
    df = pd.read_csv(DATA)
    count = 0
    docs = []
    for index, row in df.iterrows():
        docs.append(row[0])
        count += 1
    print(count)

extract_topics()