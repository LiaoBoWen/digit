import numpy as np
import pandas as pd
from pandas import DataFrame,Series

n = np.nan
print(type(n))
print(1+n)


s1 =Series([1,2,n,3,4],index=list('ABCDE'))
print(s1)
print(s1.isnull(),s1.notnull())

s1 = s1.dropna()
print(s1)
#Series里面的isnull,notnull,dropna都适用于DataFrame
df = DataFrame([[1,2,n],[1,n,3],[n,n,3],[n,n,n]])
print(df)
print(df.isnull(),df.notnull())
print(df.dropna(axis=0,how='all',thresh=1))    #axis=0按照行,how=‘any’凡是那一列（hang)有NaN就删除，=‘all'只有那一行（lie)都是NaN才删除,thresh=1 那一列（行）的NaN大于一个就删除
df2 = df.fillna(value={0:'A',1:'B',2:'C',3:"D"})      #第0列的NaN填充为A，……
print(df2)
