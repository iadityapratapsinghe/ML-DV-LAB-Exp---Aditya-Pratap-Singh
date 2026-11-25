"""Experiment 8: Gaussian Naive Bayes using the Wine dataset."""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Gaussian Naive Bayes")
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions, target_names=wine.target_names))
