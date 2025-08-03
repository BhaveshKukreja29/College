import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/complab304lenovo-neo5pc13/Desktop/college_student_placement_dataset.csv"
df = pd.read_csv(path)

df.loc[5:2, 'IQ'] = np.nan
df.loc[20:4, 'CGPA'] = np.nan

print("\n-----Dataset info-----")
print(df.info())
print("\n---- Descriptive stats-----")
print(df.describe())

# Missing data handling

df['IQ'].fillna(df['IQ'].mean(), inplace=True)
df['CGPA'].fillna(df['CGPA'].mean(), inplace=True)

# outliers

plt.boxplot(df['IQ'])
plt.title("Boxplot of IQ")
plt.ylabel("IQ score")
plt.grid(True)
plt.show()


# 6A. Binning by mean (equal-width)
df['IQ_bin_mean'] = pd.cut(df['IQ'], bins=3, labels=["Low", "Medium", "High"])

# 6B. Binning by boundary
boundaries = [0, 90, 110, 200]
df['IQ_bin_boundary'] = pd.cut(df['IQ'], bins=boundaries, labels=["Low", "Average", "High"])

# 7. Normalization

# 7A. Min-Max Normalization
df['IQ_minmax'] = (df['IQ'] - df['IQ'].min()) / (df['IQ'].max() - df['IQ'].min())

# 7B. Z-score Normalization
df['IQ_zscore'] = (df['IQ'] - df['IQ'].mean()) / df['IQ'].std()

# 7C. Decimal Scaling
j = len(str(int(df['IQ'].abs().max())))
df['IQ_decimal_scaled'] = df['IQ'] / 10**j

# 8. Visualization

# 8A. Histogram
plt.hist(df['IQ'], bins=10, color='orange', edgecolor='black')
plt.title("IQ Distribution")
plt.xlabel("IQ")
plt.ylabel("Number of People")
plt.grid(True)
plt.show()

# 8B. Bar Plot of Binned IQ
df['IQ_bin_boundary'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
plt.title("IQ Categories (Boundary Binning)")
plt.xlabel("IQ Category")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# 8C. Scatter Plot: IQ vs Placement Score
plt.scatter(df['IQ'], df['placement_score'], color='orange')
plt.title("IQ vs Placement Score")
plt.xlabel("IQ")
plt.ylabel("Placement Score")
plt.grid(True)
plt.show()

# 8D. Correlation Matrix + Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()