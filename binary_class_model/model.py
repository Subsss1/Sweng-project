from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
import csv


def load_data():
    with open(r'human_update_EXAMPLE.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        properties = next(data_reader)[:9]
        print(properties)
        data = []
        author = []
        for row in data_reader:
            stats = row[:9]
            label = row[9] #index to whichever column indicates machine/human generated
            data.append([num for num in stats])
            author.append(int(label))

        #data = np.array(data)
        #author = np.array(author)
    return Bunch(data=data, author=author, properties=properties)


dummy = load_data()
prop = dummy['properties']
print("prop: ", prop)
data = dummy['data']
auth = dummy['author']
print("auth: ", auth[:10])

training_data, testing_data, training_labels,  testing_labels = train_test_split(data, auth, stratify=auth,
                                                                                test_size=0.2, random_state=1)
print(training_data[:9])
print(testing_data[:9])
print(training_labels[:9])
print(testing_labels[:9])

gauss = GaussianNB()
model = gauss.fit(training_data,training_labels)
test_results = gauss.predict(testing_data)
print(test_results)

score = accuracy_score(testing_labels,test_results)
print(score)