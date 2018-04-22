import numpy as np
import pandas as pd
from pandas import DataFrame,Series
'''
#首先获取数据列表
df = pd.read_csv("../***.csv")
g = df.groupby('……')
print(g.groups)
bj = g.get_group('BJ')
print(bj)
print(bj.mean())    #求平均值
print(g.mean())
list(g)
print(dict(list(g))['BJ'])
'''

d1 = DataFrame(np.random.rand(4,5),index=list("ASDF"),columns=list("ZXCVB"))
print(d1)
df = d1.groupby('X')
g = df.get_group("X")
print(g)
print(df.mean())    #分组回计算得到后返回dataframe
