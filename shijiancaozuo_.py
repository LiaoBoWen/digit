import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from datetime import datetime

t1 = datetime(2018,3,21)
print(t1)

datelist = [
    datetime(2012,3,4),
    datetime(2312,4,1),
    datetime(4324,3,5),
    datetime(3254,12,1),
    datetime(4312, 1, 1)
]
print(datelist)
s1 = Series(np.random.randn(5),index=datelist)
print(s1)
print()
print(s1.values)
print(s1.index)
print(s1[1])
print(s1[datetime(2312,4,1)])


# print(s1['2312-04-01'])
# print(s1['2012-03'])
# print(s1['2312'])

datelist_new = pd.date_range('2016-01-01',periods=100,freq='5H')    #freq步长”W'周日开始‘W-MON'从周一开始，5H 以五小时为间隔 start开始时间   end结束时间 periods 长度
# print(datelist_new)
s2 = Series(np.random.rand(100),index=datelist_new)
print(s2)

dateli = pd.date_range('2134-01-01','2200-01-01',freq='W')
print(dateli)
s = Series(np.random.rand(len(dateli)),index=dateli)
print(s.head())
print()
print(s['2134-1'])
