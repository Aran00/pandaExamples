__author__ = 'ryu'

import pandas as pd
import pandas.io.data as web

pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '5/1/2012', '6/1/2012')) for stk in ['AAPL', 'MSFT', 'DELL']))
pdata = pdata.swapaxes('items', 'minor')
print pdata['Adj Close']

print pdata.ix[:, '6/1/2012', :]
print pdata.ix['Adj Close', '5/22/2012':, :]

stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
print stacked
stacked.to_panel()