import sys
import joblib


loaded_model = joblib.load('svm_model.pkl')


def predict(data):
    return loaded_model.predict([data])[0]

