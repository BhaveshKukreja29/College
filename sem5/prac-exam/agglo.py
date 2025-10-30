import numpy as np
import pandas as pd

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def linkage_distance(cluster1, cluster2, X, method):
    distances = [euclidean_distance(X[i], X[j]) for i in cluster1 for j in cluster2]
    if method == 'single':
        return np.min(distances)
    elif method == 'complete':
        return np.max(distances)
    else:
        return np.mean(distances)

def compute_distance_table(clusters, X, method):
    n = len(clusters)
    dist_table = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_table[i][j] = linkage_distance(clusters[i], clusters[j], X, method)
            else:
                dist_table[i][j] = np.inf
    return pd.DataFrame(dist_table)

def hierarchical_clustering(X, method):
    clusters = [[i] for i in range(len(X))]
    step = 1
    while len(clusters) > 1:
        print(f"\nStep {step}:")
        dist_table = compute_distance_table(clusters, X, method)
        print(dist_table)
        
        # find smallest distance
        i, j = np.unravel_index(np.argmin(dist_table.values), dist_table.shape)
        clusters[i] = clusters[i] + clusters[j]
        del clusters[j]
        print(f"Merged clusters {i} & {j} -> New cluster: {clusters[i]}")
        step += 1
    return clusters

# ===== Demo =====
X = np.array([[1, 2], [2, 3], [5, 8], [6, 9]])
hierarchical_clustering(X, 'single')
