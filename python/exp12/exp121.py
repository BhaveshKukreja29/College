"""
Perform arithmetic & comparison on Series,
convert dict and NumPy array to Series
"""

import pandas as pd
import numpy as np

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("\nAddition:\n", s1 + s2)
print("\nSubtraction:\n", s1 - s2)
print("\nMultiplication:\n", s1 * s2)
print("\nDivision:\n", s1 / s2)

print("\nEqual:\n", s1 == s2)
print("\nGreater:\n", s1 > s2)
print("\nLess:\n", s1 < s2)

data = {'a': 100, 'b': 200, 'c': 300}
dict_series = pd.Series(data)
print("\nDictionary to Series:\n", dict_series)

arr = np.array([7, 14, 21])
np_series = pd.Series(arr)
print("\nNumPy Array to Series:\n", np_series)
