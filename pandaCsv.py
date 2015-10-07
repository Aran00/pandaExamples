__author__ = 'ryu'

import pandas as pd
import numpy as np
import sys, csv
from pandas import Series

class PandaCsv:
    def __init__(self):
        pass

    def read_csv_data(self):
        pd.read_csv('ch06/ex1.csv')
        pd.read_table('ch06/ex1.csv', sep=',')
        pd.read_csv('ch06/ex2.csv', header=None)
        pd.read_csv('ch06/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
        pd.read_csv('ch06/csv_mindex.csv', index_col=['key1', 'key2'])
        pd.read_csv('ch06/csv_mindex.csv', index_col=['key2', 'key1']).sort_index(0)
'''
result = pd.read_table('ch06/ex3.csv', sep='\s+')
pd.read_csv('ch06/ex4.csv', skiprows=[0, 2, 3])
pd.read_csv('ch06/ex5.csv', na_values=['NULL'])

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('ch06/ex5.csv', na_values=sentinels)
pd.read_csv('ch06/ex6.csv', nrows=5)


chunker = pd.read_csv('ch06/ex6.csv', chunksize=1000)
tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.order(ascending=False)
print tot[:10]


data = pd.read_csv('ch06/ex5.csv')
data.to_csv('ch06/out.csv', na_rep='NULL')
data.to_csv(sys.stdout, sep='|')
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False, cols=['a', 'b', 'c'])

dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
ts.to_csv('ch06/tseries.csv')
Series.from_csv('ch06/tseries.csv', parse_dates=True)

f = open('ch06/ex7.csv')
reader = csv.reader(f)

for line in reader:
    print line
lines = list(csv.reader(open('ch06/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
'''

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_ALL

#reader = csv.reader(f, dialect=my_dialect)
#reader = csv.reader(f, delimiter='|')

with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
