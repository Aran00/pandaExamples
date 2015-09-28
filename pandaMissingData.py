__author__ = 'ryu'

import numpy as np
import pandas as pd
from numpy import nan as NA
from pandas import Series, DataFrame

string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data[0] = None
print string_data.isnull()
string_data.fillna(0)

data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
data.dropna()
data.dropna(axis=1, how="all")
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.dropna(thresh=2)  # At least how many non NA values

df.fillna({1: 0.5, 3: -1})
df.fillna(method="bfill", limit=2)


data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
              [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print data.index
print data['b'], data['b':'c'], data.ix[['b', 'd']], data[:, 2]
print data.unstack()


frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                  ['Green', 'Red', 'Green']])
print frame
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print frame['Ohio']
pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])

frame.swaplevel('key1', 'key2').sortlevel(0)
frame.sum(level='key2')
frame.sum(level='color', axis=1)

frame2 = frame.set_index(['c', 'd'])
frame.set_index(['c', 'd'], drop=False)

ser3 = Series(range(3), index=[-5, 1, 3])
ser3.iget_value(2)
frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
frame.irow(0)