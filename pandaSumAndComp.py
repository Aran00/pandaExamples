__author__ = 'ryu'

import numpy as np
import pandas as pd
import pandas.io.data as web
from pandas import Series, DataFrame

'''
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
                index=['a', 'b', 'c', 'd'],
                columns=['one', 'two'])
df.sum()
df.sum(axis=1)
df.mean(axis=1, skipna=False)
df.idxmax()
df.cumsum()
df.describe()
obj = Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()


all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '12/28/2009', '1/1/2010')
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
returns = price.pct_change()
returns.tail()            # The last several rows
returns.MSFT.corr(returns.IBM)
returns.MSFT.cov(returns.IBM)
returns.corr()
returns.cov()
returns.corrwith(returns.IBM)
'''

obj = Series(['c', 'a', 'd', 'b', 'a', 'b', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
print uniques
print obj.value_counts()    # Sort from high frequent value to low frequent value
print obj.values
print pd.value_counts(obj.values, sort=False)
print obj.isin(['b', 'c'])

data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})

