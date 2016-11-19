"""
one of the most popular python library to manipulate and analyze data
"""

import pandas as pd
import numpy as np

# one of two important data, Series: one dimensional labeled array
# holding data types: str, int, float, python object etc.
# method 1: create from ndarray, if given index,
# index length should be as same as the array length
x = [_ for _ in range(100, 105, 1)]
sr1 = pd.Series(x, name="ID",
                index=['a', 'b', 'c', 'd', 'e'])
print(sr1)

# method 2: create from dict
d = {'a': 0, 'b': 1, 'c': 2, 'd': 3.0}
sr2 = pd.Series(d)
print(sr2)

#  data type changed
d = {'a': 0, 'b': 1, 'c': 'c', 'd': 3.0}
sr3 = pd.Series(d)
print(sr3)

# NaN is standard missing data marker in pandas
# pay attention to the order
sr4 = pd.Series(d, index=['a', 'b', 'c', 'e', 'd'])
print(sr4)

# from scalar value, index must be provided to tell the length
sr5 = pd.Series(2, index=['a', 'b', 'c'], name='scalar')
print(sr5)

# ndarray-like and dict-like, it is mutable,
# and can be manipulated like dict and ndarray
# int type can not manipulate sqrt, exp !!!!
sr3['c'] = 2
print(sr3)
print(sr3[1])
print(sr3+sr3)
print(sr3*3)
# print(np.sqrt(sr3))  raise AttributeError
print(sr3[sr3 >= 2])
print(sr3)
sr3['e'] = 4.0
sr3 = pd.Series(sr3, dtype=float, name='example')
print(sr3)
print(np.sqrt(sr3))
print(sr3.name)
sr6 = sr3.rename("changed")  # after pandas v 18
print(sr6)
print(pd.__version__)
