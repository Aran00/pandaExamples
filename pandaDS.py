__author__ = 'ryu'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
obj = Series([1, 3, 2, 5])
print obj
print obj.index
print obj.values

obj1 = Series([1, 2, 3, 4])
obj2 = obj + obj1
print obj2


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                  index=['one', 'two', 'three', 'four', 'five'])
print frame
print frame['state']
print frame.year
print frame.ix['three']

frame['debt'] = np.arange(1, 6)
print frame

val = Series([-1.2, -1.5, -1.7, 1.3], index=['two', 'four', 'five', 'six'])
frame['debt'] = val
print frame

del frame['debt']  #Can't be frame.debt
print frame.columns

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop, index=[2001, 2002, 2003])
print frame3.T
print frame3.values
print frame3.index
print 'pop' in frame3.columns
'''
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
''' The differences of == and is: http://stackoverflow.com/questions/2988017/string-comparison-in-python-is-vs '''
print obj2.index is index

index1 = pd.Index(np.arange(1, 4))
print index.difference(index1)
print index.append(index1)
print index.intersection(index1)
print index.union(index1)
print index.is_unique
print index.unique()
print index.delete(1)
print index