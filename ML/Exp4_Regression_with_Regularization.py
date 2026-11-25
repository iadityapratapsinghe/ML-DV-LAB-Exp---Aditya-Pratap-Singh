"""Experiment 4: Ridge and Lasso regularization using the Diabetes dataset."""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for name, estimator in (("Ridge", Ridge(alpha=1.0)), ("Lasso", Lasso(alpha=0.1, max_iter=10000))):
    model = make_pipeline(StandardScaler(), estimator)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"{name} MSE: {mean_squared_error(y_test, predictions):.4f}")
