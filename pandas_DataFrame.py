"""
Dataframe is 2-D labeled data structure with different types.
"""

import pandas as pd
import numpy as np
import random

# one of two important data, DataFrame: 2-D labeled data structure
# create from dict
df1 = pd.DataFrame({'id': [100, 101, 102], 'color': ['red', 'blue', 'green']})
print('--------------df1-------------')
print(df1)
# the dict no order, to want the column ordered,
# column and index label argument can be used to be signed
df2 = pd.DataFrame({'id': [100, 101, 102],
                    'color': ['red', 'blue', 'green']},
                   columns=['id', 'color'],
                   index=['a', 'b', 'c'])
print('--------------df2-------------')
print(df2)

# create from list of lists,
# default index and column name will start from 0
df3 = pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'green']])
print('--------------df3-------------')
print(df3)
df4 = pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'green']],
                   columns=['id', 'color'],
                   index=['a', 'b', 'c'])
print('--------------df4-------------')
print(df4)

# create from ndarry
arr = np.random.rand(4, 2)  # create 4*2 ndarry random numbers
print('--------------arr-------------')
print(arr)
df5 = pd.DataFrame(arr, columns=['one', 'two'])
print('--------------df5-------------')
print(df5)

df6 = pd.DataFrame({'Id': np.arange(100, 110, 1),
                    'scores': np.random.randint(60, 101, 10)})
print('--------------df6-------------')
print(df6)
# to reset the index
df7 = df6.set_index('Id')
print('--------------df7-------------')
print(df7)
# to drop index name
df8 = df7.rename_axis(None)
print('--------------d8-------------')
print(df8)

# create from structured or record array
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f8'), ('C', 'a10')])
# i4--int32, f8--float64, a10--10 char string
print('--------------data-------------')
print(data)
data[:] = [(1, 2, 'Hello'), (3, 4., 'World')]
print('--------------revised data-------------')
print(data)
df9 = pd.DataFrame.from_records(data, index='C')
print('--------------df9-------------')
print(df9)

# column selection, addition, deletion
print('------DataFrame column Selection-------')
print(df9['A'])
print(df9.B)  # can not be used if white_space in column name
df9['D'] = [2, 3.5]
df9['E'] = df9.A * df9.B
print('------DataFrame column addition-------')
print(df9)
del df9['B']
df9.pop('A')
print('------DataFrame column deletion-------')
print(df9)
