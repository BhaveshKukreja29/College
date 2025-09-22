import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv('your_file_path.csv')

df['CGPA_Range'] = pd.cut(df['CGPA'], bins=[0, 6, 8, 10], labels=['Low', 'Medium', 'High'])
df['IQ_Range'] = pd.cut(df['IQ'], bins=[0, 100, 120, 150], labels=['Average', 'High', 'Very_High'])

onehot_df = pd.get_dummies(df[['Internship_Experience', 'Placement', 'CGPA_Range', 'IQ_Range']])

frequent_itemsets = apriori(onehot_df, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print("--- Frequent Itemsets ---")
print(frequent_itemsets.head())
print("\n--- Association Rules ---")
print(rules[['antecedents', 'consequents', 'lift']].head())
