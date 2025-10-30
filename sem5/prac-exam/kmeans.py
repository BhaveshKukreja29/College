import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your data
# This assumes your data has 'CGPA' and 'IQ' columns.
try:
    data = pd.read_csv("college_placement.csv")
except FileNotFoundError:
    print("Error: 'college_placement.csv' not found. Please check the file path.")
    exit()

# 2. Select the features for clustering
# We'll cluster students based on their CGPA and IQ.
features = data[['CGPA', 'IQ']]

# 3. Create and train the K-Means model
# We'll create 3 clusters as specified in the problem.
# 'n_init=10' is standard practice to get more stable results.
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(features)

# 4. Get the results
# Add the cluster labels back to your original dataframe.
data['cluster'] = kmeans.labels_
# Get the coordinates of the final cluster centers.
centroids = kmeans.cluster_centers_

# --- Print the Output ---
print("--- K-Means Final Results ---")
print("Final Centroids (CGPA, IQ):")
print(centroids)
print("\nFirst 10 students with their assigned cluster:")
print(data.head(10))


# 5. Visualize the clusters
# This is required by the guidelines.
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='CGPA', y='IQ', hue='cluster', palette='viridis', s=100, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')
plt.title('K-Means Clustering of Students')
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.legend()
plt.grid(True)
plt.show()