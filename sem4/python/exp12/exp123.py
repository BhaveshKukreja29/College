"""
Merge DataFrames on 'id' using different join methods
"""

import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'marks': [80, 85, 90]
})

print("\nInner Join:\n", pd.merge(df1, df2, on='id'))
print("\nLeft Join:\n", pd.merge(df1, df2, on='id', how='left'))
print("\nRight Join:\n", pd.merge(df1, df2, on='id', how='right'))
print("\nOuter Join:\n", pd.merge(df1, df2, on='id', how='outer'))