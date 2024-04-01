import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# Load data
def load_data(datasets: list[str]):
  dataset_files = map(pd.read_csv, datasets)
  return pd.concat(dataset_files, ignore_index=True)


# Preprocess and split data
def preprocess_data(data: pd.DataFrame, test_size: float = 0.2, seed: int = 42):
  # Drop irrelevant columns
  data = data.drop(['number'], axis=1)

  # Split the data into features and target variable
  X = data.drop('human', axis=1)
  Y = LabelEncoder().fit_transform(data['human'])

  # Split the data into training and test sets
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

  return X_train, X_test, Y_train, Y_test


# Dump model
def dump_model(model, path: str = './model.pkl'):
  joblib.dump(model, path)
  print(f"Model dumped to {path}")


# Train Logistic Regression
def train_LR(data: pd.DataFrame, test_size: float = 0.2, seed: int = 42):
  X_train, X_test, Y_train, Y_test = preprocess_data(data, test_size, seed)

  model = LogisticRegression(max_iter=10000)
  model.fit(X_train, Y_train)

  Y_pred = model.predict(X_test)
  accuracy = accuracy_score(Y_test, Y_pred)
  print(f"Accuracy on test set: {accuracy}")

  return model

# Train K-Nearest Neighbors
def train_KNN(data: pd.DataFrame, test_size: float = 0.2, seed: int = 42):
  X_train, X_test, Y_train, Y_test = preprocess_data(data, test_size, seed)

  model = KNeighborsClassifier()
  model.fit(X_train, Y_train)

  Y_pred = model.predict(X_test)
  accuracy = accuracy_score(Y_test, Y_pred)
  print(f"Accuracy on test set: {accuracy}")

  return model


# Train Decision Tree Classifier
def train_DTC(data: pd.DataFrame, test_size: float = 0.2, seed: int = 42):
  X_train, X_test, Y_train, Y_test = preprocess_data(data, test_size, seed)

  model = DecisionTreeClassifier()
  model.fit(X_train, Y_train)

  Y_pred = model.predict(X_test)
  accuracy = accuracy_score(Y_test, Y_pred)
  print(f"Accuracy on test set: {accuracy}")

  return model


# Train Random Forest Classifier
def train_RFC(data: pd.DataFrame, test_size: float = 0.2, seed: int = 42):
  X_train, X_test, Y_train, Y_test = preprocess_data(data, test_size, seed)

  model = RandomForestClassifier(n_estimators=16, max_depth=20, random_state=seed)
  model.fit(X_train, Y_train)

  Y_pred = model.predict(X_test)
  accuracy = accuracy_score(Y_test, Y_pred)
  print(f"Accuracy on test set: {accuracy}")

  return model


if __name__ == '__main__':
  datasets = [
    './datasets/1.csv',
    './datasets/2.csv',
    './datasets/3.csv',
    './datasets/4.csv',
    './datasets/5.csv'
  ]

  data = load_data(datasets)

  models = { 
    'LR': train_LR,
    'KNN': train_KNN,
    'DTC': train_DTC,
    'RFC': train_RFC
  }

  print(f"Loaded {len(data)} samples from {len(datasets)} datasets")

  for model_name, train_model in models.items():
    print(f"\nTraining {model_name} model...")
    model = train_model(data)
    dump_model(model, f'./dumps/{model_name}_model.pkl')
