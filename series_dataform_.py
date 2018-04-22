import numpy as np
import pandas as pd
from pandas import DataFrame,Series

s1 = Series([1,2,3],index=list('ABC'))
print(s1)
s2 = Series([4,5,6,7],index=list('BCDE'))
print(s1+s2)


df = DataFrame(np.random.randint(10,size=[2,2]),index=list('AB'),columns=list("JK"))
df1 = DataFrame(np.random.randint(10,size=[3,3]),index=list('ABC'),columns=list("JKL"))
print(df)
print(df1+df)
df2 = DataFrame([[1,2,3],[4,np.nan,5],[7,8,9]],index=list("ABC"),columns=list('#$%'))
print(df2)
print()
print(df2.sum(axis=1))    #返回series  列的结果   求和是NaN会被忽略
print(df.min())         #max同理
print()
print(df2.describe())
