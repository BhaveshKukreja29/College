"""
Read CSV, replace missing with 'N/A',
drop rows with all/any null values
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'David'],
    'age': [25, None, None, 30],
    'city': ['NY', 'LA', None, 'SF']
})

print("\nOriginal DataFrame:\n", df)

df_replaced = df.fillna('N/A')
print("\nAfter fillna('N/A'):\n", df_replaced)

df_all_nulls_dropped = df.dropna(how='all')
print("\nAfter dropna(how='all'):\n", df_all_nulls_dropped)

df_any_nulls_dropped = df.dropna()
print("\nAfter dropna():\n", df_any_nulls_dropped)