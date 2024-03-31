import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
datasets = [
  pd.read_csv('dataset1.csv'),
  pd.read_csv('dataset2.csv'),
  pd.read_csv('dataset3.csv'),
  pd.read_csv('dataset4.csv'),
  pd.read_csv('dataset5.csv'),
]
data = pd.concat(datasets, ignore_index=True)

# Drop unnecessary columns
data = data.drop(['number'], axis=1)

print(data)

# Encode the 'human' column
label_encoder = LabelEncoder()
data['human'] = label_encoder.fit_transform(data['human'])

# Split the data into features and target variable
X = data.drop('human', axis=1)
y = data['human']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_prob = model.predict_proba(X_test)
y_pred = (y_prob[:, 1] >= 0.5).astype(int)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test set: {accuracy}")

joblib.dump(model, './model.pkl')
print(f"Model dumped to ./model.pkl")
