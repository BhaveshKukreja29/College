import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("college_placement.csv")
features = data[['CGPA', 'IQ']].values
K = 3

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2)**2))

centroids = features[np.random.choice(features.shape[0], K, replace=False)]
clusters = np.zeros(len(features))

for _ in range(10): 
    for i, point in enumerate(features):
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        clusters[i] = np.argmin(distances)

    for i in range(K):
        points_in_cluster = features[clusters == i]
        if len(points_in_cluster) > 0:
            centroids[i] = np.mean(points_in_cluster, axis=0)

colors = ['r', 'g', 'b']
for i in range(K):
    points = features[clusters == i]
    plt.scatter(points[:, 0], points[:, 1], c=colors[i], label=f'Cluster {i+1}')

plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='black', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.legend()
plt.grid(True)
plt.show()