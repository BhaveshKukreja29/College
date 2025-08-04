import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    path = "college_student_placement_dataset.csv"
    df = pd.read_csv(path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The file was not found. Please check the path.")
    exit()

# --- Initial Data Exploration ---
print("\n----- 2. Dataset Info -----")
print(df.info())

print("\n----- 3. Descriptive Statistics (Initial) -----")
print(df.describe())

# manually introduce missing values
print("\n----- 4. Data Cleaning -----")
df.loc[5:34, 'IQ'] = np.nan
df.loc[20:79, 'CGPA'] = np.nan
print("\nMissing values introduced into 'IQ' and 'CGPA' columns.")
print("Missing values count before handling:\n", df.isnull().sum())

# handle Missing Values using Mean Imputation
df['IQ'] = df['IQ'].fillna(df['IQ'].mean())
df['CGPA'] = df['CGPA'].fillna(df['CGPA'].mean())
print("\nMissing values filled with the mean.")
print("Missing values count after handling:\n", df.isnull().sum())

# identify and Remove Outliers (using IQR method on 'CGPA')
print("\nIdentifying and removing outliers from 'CGPA'...")
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['CGPA'])
plt.title("Box Plot of CGPA (Before Outlier Removal)")
plt.grid(True)

Q1 = df['CGPA'].quantile(0.25)
Q3 = df['CGPA'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_count = ((df['CGPA'] < lower_bound) | (df['CGPA'] > upper_bound)).sum()
print(f"Number of outliers detected in CGPA: {outliers_count}")

# removing outliers
df_cleaned = df[~((df['CGPA'] < lower_bound) | (df['CGPA'] > upper_bound))]
print(f"Original shape: {df.shape}, Shape after removing outliers: {df_cleaned.shape}")

plt.subplot(1, 2, 2)
sns.boxplot(y=df_cleaned['CGPA'])
plt.title("Box Plot of CGPA (After Outlier Removal)")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n----- 5. Data Discretization on 'IQ'-----")
# binning by mean
df_cleaned['IQ_bin_mean'] = pd.cut(df_cleaned['IQ'], bins=3, labels=["Low", "Medium", "High"])
print("\n'IQ' binned into 3 equal-width bins:\n", df_cleaned['IQ_bin_mean'].value_counts())

# binning by boundary
boundaries = [df_cleaned['IQ'].min()-1, 90, 110, df_cleaned['IQ'].max()+1]
df_cleaned['IQ_bin_boundary'] = pd.cut(df_cleaned['IQ'], bins=boundaries, labels=["Low", "Average", "High"], right=False)
print("\n'IQ' binned by custom boundaries [0-90, 90-110, 110+]:\n", df_cleaned['IQ_bin_boundary'].value_counts())

print("\n----- 6. Data Normalization on 'IQ'-----")


# min-Max Normalization
df_cleaned['IQ_minmax'] = (df_cleaned['IQ'] - df_cleaned['IQ'].min()) / (df_cleaned['IQ'].max() - df_cleaned['IQ'].min())
print("\nMin-Max Normalization of IQ (showing first 5 rows):\n", df_cleaned[['IQ', 'IQ_minmax']].head())

# z-score Normalization
df_cleaned['IQ_zscore'] = (df_cleaned['IQ'] - df_cleaned['IQ'].mean()) / df_cleaned['IQ'].std()
print("\nZ-Score Normalization of IQ (showing first 5 rows):\n", df_cleaned[['IQ', 'IQ_zscore']].head())

# dcimal Scaling
j = len(str(int(df_cleaned['IQ'].abs().max())))
df_cleaned['IQ_decimal_scaled'] = df_cleaned['IQ'] / (10**j)
print(f"\nDecimal Scaling of IQ with j={j} (showing first 5 rows):\n", df_cleaned[['IQ', 'IQ_decimal_scaled']].head())


print("\n----- 7. Generating Visualizations -----")

# Histogram 
plt.figure(figsize=(8, 6))
sns.histplot(df_cleaned['IQ'], bins=20, kde=True, color='skyblue')
plt.title('Histogram of IQ Distribution')
plt.xlabel('IQ Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Bar Graph
plt.figure(figsize=(8, 6))
df_cleaned['Placement'].value_counts().plot(kind='bar', color=['lightgreen', 'salmon'])
plt.title('Bar Graph of Placement Status')
plt.xlabel('Placement')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='IQ', y='CGPA', hue='Placement', data=df_cleaned, palette='viridis')
plt.title('Scatter Plot of CGPA vs. IQ')
plt.xlabel('IQ Score')
plt.ylabel('CGPA')
plt.grid(True)
plt.show()

# 7D. Line Chart
plt.figure(figsize=(8, 6))
plt.plot(df_cleaned['Prev_Sem_Result'].sort_values().values, marker='o', linestyle='-', markersize=3)
plt.title('Line Chart of Sorted Previous Semester Results')
plt.xlabel('Student Index (Sorted)')
plt.ylabel('Previous Semester Result')
plt.grid(True)
plt.show()

# 7E. Heat Map 
numeric_cols = df_cleaned.select_dtypes(include=np.number)
correlation_matrix = numeric_cols.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

print("\nExploratory Data Analysis complete.")