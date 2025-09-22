import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv('your_file_path.csv')

numerical_features = df[['IQ', 'CGPA']]
linked = linkage(numerical_features, method='single')

plt.figure(figsize=(12, 6))
dendrogram(linked, labels=df['College_ID'].values)
plt.title('Single Linkage Clustering')
plt.xlabel('College ID')
plt.ylabel('Distance')
plt.show()
