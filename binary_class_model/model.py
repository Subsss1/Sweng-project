from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
import numpy as np
import csv


def load_dummy_data():
    with open(r'dummy_data.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        #print(data_reader)
        properties = next(data_reader)[:6]
        #print(properties)
        data = []
        author = []
        for row in data_reader:
            #print(row)
            stats = row[:6]
            #print(features)
            lable = row[6] #index to whichever column indicates machine/human generated
            #print(label)
            data.append([float(num) for num in stats])
            #print(data)
            author.append(int(lable))
            #print(author)

        data = np.array(data)
        #print(data)
        author = np.array(author)
        #print(author)
    return Bunch(data=data, author=author, properties=properties)


dummy = load_dummy_data()
prop = dummy['properties']
print("prop: ", prop)
data = dummy['data']
print("data: ", data)
auth = dummy['author']
print("auth: ", auth)