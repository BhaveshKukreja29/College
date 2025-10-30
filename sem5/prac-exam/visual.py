import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple DataFrame (a table in Python)
data = {'CGPA': [8.5, 9.1, 7.8, 6.5, 8.8, 9.5, 4.2, 7.1, 8.9],
        'IQ': [110, 120, 105, 100, 115, 125, 80, 108, 118]}
df = pd.DataFrame(data)

# --- 1. Visualization ---
# A box plot is perfect because it shows the data's spread and helps with outlier analysis.
print("--- Displaying Box Plot for Outlier Detection ---")
sns.boxplot(y=df['CGPA'])
plt.title('Box Plot of CGPA')
plt.show()

# --- 2. Outlier Analysis ---
# We calculate the IQR to find outliers mathematically.
print("\n--- Outlier Analysis ---")
Q1 = df['CGPA'].quantile(0.25)
Q3 = df['CGPA'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the DataFrame to find rows that are outliers.
outliers = df[(df['CGPA'] < lower_bound) | (df['CGPA'] > upper_bound)]
print(f"The outlier(s) found are:\n{outliers}")

# --- 3. Discretization ---
# We use pd.cut() to easily create categories (bins) for the CGPA.
print("\n--- Discretization ---")
df['CGPA_Category'] = pd.cut(
    df['CGPA'], 
    bins=[0, 7, 9, 10], 
    labels=['Low', 'Medium', 'High'] # Names for our new categories
)
print("CGPA column after being discretized into categories:")
print(df[['CGPA', 'CGPA_Category']])