__author__ = 'ryu'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')

states = ['Ohio', 'Texas', 'California']
frame = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'c', 'd'], columns=states)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame3 = frame.reindex(columns=['Texas', 'Utah', 'California'])
frame4 = frame.reindex(index=['a', 'b', 'c', 'd'], columns=['Texas', 'Utah', 'California'], method='ffill')
frame5 = frame.ix[['a', 'b', 'c', 'd'], states]
print frame5

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop(['d', 'c'])

data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data.drop(['Colorado', 'Ohio'])
data.drop(['two', 'four'], axis=1)

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print obj[['a', 'd']], obj[obj < 2], obj[[1, 3]], obj[1:3], obj['a':'c']
obj['b':'c'] = 5


data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print data['two'], data[['three', 'one']], data[:2], data[data['three'] > 5]
print data < 5
data[data < 5] = 0
print data.ix[2], data.ix[[1, 3], [3, 0, 1]], data.ix[['Colorado', 'Utah'], ['two', 'three']]
print data.ix[data.three > 5, :3]



