import unittest
import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

class TestModel(unittest.TestCase):
    def setUp(self):
        # Load the iris dataset
        iris = datasets.load_iris()
        iris_X = iris.data
        iris_y = iris.target

        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            iris_X,iris_y,test_size=0.3)

        # Train the KNN classifier
        self.knn = KNeighborsClassifier()
        self.knn.fit(self.X_train, self.y_train)

        # Save the trained model
        joblib.dump(self.knn, 'svm_model.pkl')


    def test_model_prediction(self):
        # Load the trained model
        loaded_model = joblib.load('svm_model.pkl')

        # Predict using the loaded model
        predicted_labels = loaded_model.predict(self.X_test)

        # Check if the predicted labels have the correct shape
        self.assertEqual(predicted_labels.shape, self.y_test.shape)

    def test_model_accuracy(self):
        loaded_model = joblib.load('svm_model.pkl')
        predicted_labels = loaded_model.predict(self.X_test)

        # Calculate accuracy
        accuracy = accuracy_score(self.y_test, predicted_labels)

        # Check if the accuracy is within an acceptable range (e.g., 0.9)
        self.assertGreaterEqual(accuracy, 0.9)

        print(accuracy)

    def test_model_persistence(self):
        loaded_model = joblib.load('svm_model.pkl')

        # Check if the loaded model is an instance of KNeighborsClassifier
        self.assertIsInstance(loaded_model, KNeighborsClassifier)

    def test_train_test_split(self):
        # Check if the shapes of the training and testing data are correct
        self.assertEqual(self.X_train.shape[0], len(self.y_train))
        self.assertEqual(self.X_test.shape[0], len(self.y_test))

    def test_saved_model_existence(self):
        # Check if the saved model file exists
        import os
        self.assertTrue(os.path.exists('svm_model.pkl'))

if __name__ == '__main__':
    unittest.main()
                        
                         
        
