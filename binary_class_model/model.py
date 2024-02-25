from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import csv
import re


def load_data():
    with open(r'human_update_EXAMPLE.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        properties = next(data_reader)[:9]
        #protocols = []
        #print(properties)
        data = [1]
        author = []
        with open("regex.txt","r") as f:
            regexes = [line.split("~") for line in f.read().split("\n")]
        for row in data_reader:
            if row[4] == 'TCP':
                row[4] = 0
            elif row[4] == 'UDP':
                row[4] = 1
            elif row[4] == 'TLSv1.2':
                row[4] = 2
            elif row[4] == 'DHCP':
                row[4] = 3
            elif row[4] == 'DNS':
                row[4] = 4
            elif row[4] == 'TLSv1.3':
                row[4] = 5
            elif row[4] == 'HTTP':
                row[4] = 6
            elif row[4] == 'OCSP':
                row[4] = 7
            elif row[4] == 'SSDP':
                row[4] = 8
            else:
                row[4] = 9


            for regex, category in regexes:
                if re.match(rf"{regex}", row[6]):
                    row[6] = category
                    break

            #if(not row[6] in protocols):
            #    protocols.append(row[6])

            #print(row[0], " : ", row[6])
            label = row[9] #index to whichever column indicates machine/human generated
            stats = row[:9]
            data.append([float(num) for num in stats])
            author.append(int(label))
        #print(protocols)
    return Bunch(data=data, author=author, properties=properties)


dummy = load_data()
prop = dummy['properties']
data = dummy['data']
data.remove(1)
auth = dummy['author']

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
print("score: ", score)