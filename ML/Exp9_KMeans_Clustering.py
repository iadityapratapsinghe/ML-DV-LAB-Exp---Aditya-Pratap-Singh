"""Experiment 9: K-Means clustering using the Iris dataset."""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)
model = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = model.fit_predict(X_scaled)

print("K-Means Clustering")
print("Cluster sizes:", dict(zip(*(__import__('numpy').unique(labels, return_counts=True)))))
print("Inertia:", model.inertia_)
print("Silhouette Score:", silhouette_score(X_scaled, labels))
