import joblib
from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import csv


def load_data():
    with open(r'output.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        properties = next(data_reader)[:8]
        data = []
        author = []

        #with open("regex.txt","r") as f:
        #    regexes = [line.split("~") for line in f.read().split("\n")]
        for row in data_reader:
        #    row[1] = 6
        #    if row[8] == 'TCP':
        #        row[8] = 6
        #    elif row[8] == 'UDP':
        #        row[8] = 17
        #    else:
        #        row[8] = 252

            #for regex, category in regexes:
            #    if re.match(rf"{regex}", row[6]):
            #        row[6] = category
            #        break

            label = row[8] #index to whichever column indicates machine/human generated
            stats = row[:8]
            data.append([float(num) for num in stats])
            author.append(int(label))

    return Bunch(data=data, author=author, properties=properties)


kb = load_data()
prop = kb['properties']
data = kb['data']
auth = kb['author']

print("Splitting training and testing data...")
training_data, testing_data, training_labels, testing_labels = train_test_split(data, auth, #stratify=auth,
                                                                                test_size=0.2, random_state=1)
print(training_data[:9])
print(testing_data[:9])
print(training_labels[:9])
print(testing_labels[:9])

log_reg = LogisticRegression(max_iter=7943)
model = log_reg.fit(training_data,training_labels)
test_results = log_reg.predict_proba(testing_data)
print(test_results)

pred = log_reg.predict(testing_data)
score = accuracy_score(testing_labels, pred)
joblib.dump(model, 'model.pkl')
print("score: ", score)