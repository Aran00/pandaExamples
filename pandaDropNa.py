__author__ = 'Aran'

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,3))

df.ix[::4, 1] = np.nan
df.ix[::3, 2] = np.nan

'''
In [26]: df
Out[26]:
          0         1         2
0       NaN       NaN       NaN
1  2.677677 -1.466923 -0.750366
2       NaN  0.798002 -0.906038
3  0.672201  0.964789       NaN
4       NaN       NaN  0.050742
5 -1.250970  0.030561 -2.678622
6       NaN  1.036043       NaN
7  0.049896 -0.308003  0.823295
8       NaN       NaN  0.637482
9 -0.310130  0.078891       NaN
'''

df.dropna()     #drop all rows that have any NaN values

'''
Out[27]:
          0         1         2
1  2.677677 -1.466923 -0.750366
5 -1.250970  0.030561 -2.678622
7  0.049896 -0.308003  0.823295
'''

df.dropna(how='all')     #drop only if ALL columns are NaN

'''
          0         1         2
1  2.677677 -1.466923 -0.750366
2       NaN  0.798002 -0.906038
3  0.672201  0.964789       NaN
4       NaN       NaN  0.050742
5 -1.250970  0.030561 -2.678622
6       NaN  1.036043       NaN
7  0.049896 -0.308003  0.823295
8       NaN       NaN  0.637482
9 -0.310130  0.078891       NaN
'''

df.dropna(thresh=2)   #Drop row if it does not have at least two values that are **not** NaN
'''
          0         1         2
1  2.677677 -1.466923 -0.750366
2       NaN  0.798002 -0.906038
3  0.672201  0.964789       NaN
5 -1.250970  0.030561 -2.678622
7  0.049896 -0.308003  0.823295
9 -0.310130  0.078891       NaN
'''

df.dropna(subset=[1])   #Drop only if NaN in specific column (as asked in the question)

'''
          0         1         2
1  2.677677 -1.466923 -0.750366
2       NaN  0.798002 -0.906038
3  0.672201  0.964789       NaN
5 -1.250970  0.030561 -2.678622
6       NaN  1.036043       NaN
7  0.049896 -0.308003  0.823295
9 -0.310130  0.078891       NaN
'''