# services/model_trainer.py
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn import svm, neighbors
from collections import Counter
import numpy as np


class ModelTrainer:
    def train_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42
        )
        X_train = np.reshape(X_train, (-1, 1))
        X_test = np.reshape(X_test, (-1, 1))
        y_train = np.reshape(y_train, (-1, 1))
        y_test = np.reshape(y_test, (-1, 1))

        clf = KNeighborsClassifier(n_neighbors=3)
        voting_model = VotingClassifier(
            [
                ("lvsc", svm.LinearSVC()),
                ("knn", neighbors.KNeighborsClassifier()),
                ("rfor", RandomForestClassifier()),
            ]
        )
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        print("Predicted Spread:", Counter(y_pred))
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
