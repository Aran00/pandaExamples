__author__ = 'ryu'

import numpy as np
from pandas import Series, DataFrame

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# numpy function, for each element
np.abs(frame)

# function for 1D arrays
f = lambda x: x.max() - x.min()
frame.apply(f)
frame.apply(f, axis=1)
frame.sum(axis=1)

def func(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(func)

# function for each element
format = lambda x: "%.2f" % x
frame.applymap(format)

# function for Series, element level
frame['e'].map(format)

''' Sort methods '''
obj = Series([4, 7, -3, 2], index=['d', 'a', 'b', 'c'])
obj.sort_index()
obj.order()

frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])

frame.sort_index()
frame.sort_index(axis=1, ascending=False)
frame.sort_index(by=['a', 'b'])

obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print obj['a']
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print df.ix['b']