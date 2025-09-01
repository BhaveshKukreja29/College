import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('placement.csv')
data.drop(columns=["College_ID"])

data["Internship_Experience"] = data["Internship_Experience"].map({"Yes": 1, "No": 0})
data["Placement"] = data["Placement"].map({"Yes": 1, "No": 0})

X = data[["CGPA", "Internship_Experience"]].values

def kmeans(X, k=2, max_iters=100):
    np.random.seed(0)
    centroids = X[np.random.choice(len(X), k, replace=False)]
    
    for _ in range(max_iters):
        distances = np.linalg.norm(X[:, None] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        new_centroids = np.array([X[labels == j].mean(axis=0) for j in range(k)])
        
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return labels, centroids
    
labels, centroids = kmeans(X, k=2)

data["Cluster"] = labels
print(data.head())

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", marker="o")
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", marker="x", s=200)
plt.xlabel("CGPA")
plt.ylabel("Internship Experience")
plt.title("K-means Clustering")
plt.show()
