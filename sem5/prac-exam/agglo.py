import numpy as np

def simple_hierarchical_clustering(X, method='single'):
    clusters = [[i] for i in range(len(X))]
    step = 1
    
    while len(clusters) > 1:
        min_distance = float('inf')
        closest_pair = (-1, -1)
        
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                point_distances = []
                for p1_idx in clusters[i]:
                    for p2_idx in clusters[j]:
                        dist = np.sqrt(np.sum((X[p1_idx] - X[p2_idx])**2))
                        point_distances.append(dist)
                
                if method == 'single':
                    current_distance = np.min(point_distances)
                elif method == 'complete':
                    current_distance = np.max(point_distances)
                elif method == 'average':
                    current_distance = np.mean(point_distances)
                else:
                    raise ValueError("Method must be 'single', 'complete', or 'average'")

                if current_distance < min_distance:
                    min_distance = current_distance
                    closest_pair = (i, j)

        i, j = closest_pair
        print(f"Step {step}: Merging clusters {clusters[i]} and {clusters[j]} (Distance: {min_distance:.2f})")
        
        clusters[i].extend(clusters[j])
        del clusters[j]
        
        print(f"Current clusters: {clusters}\n")
        step += 1
        
    print(f"Final Result: {clusters[0]}")
    return clusters

# --- Demo ---
X = np.array([[1, 2], [2, 3], [5, 8], [6, 9]])

print("--- Running SINGLE Linkage Clustering ---")
simple_hierarchical_clustering(X, method='single')

# print("\n--- Running COMPLETE Linkage Clustering ---")
# simple_hierarchical_clustering(X, method='complete')

# print("\n--- Running AVERAGE Linkage Clustering ---")
# simple_hierarchical_clustering(X, method='average')