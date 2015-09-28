__author__ = 'ryu'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print s1 + s2

df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
print df1
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print df2
print df1 + df2
print df1.add(df2, fill_value=0)

arr = np.arange(12.).reshape((3, 4))
print arr - arr[0]

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]
series2 = Series(range(3), index=['b', 'e', 'f'])
print frame + series2

series3 = frame['d']
print frame.sub(series3, axis=0)
series4 = frame.ix['Utah']
print frame.sub(series4, axis=1)