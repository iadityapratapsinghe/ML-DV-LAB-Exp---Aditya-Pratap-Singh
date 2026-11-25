"""Experiment 5: PCA dimensionality reduction using the Digits dataset."""
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X, y = load_digits(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)

print("PCA Dimensionality Reduction")
print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total explained variance:", pca.explained_variance_ratio_.sum())
