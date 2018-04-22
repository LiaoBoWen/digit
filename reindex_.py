import numpy as np
import pandas as pd
from pandas import DataFrame,Series

s1 = Series([1,2,3,4],index=list('ABCD'))
print(s1)
s2 = s1.reindex(index=list('ABCDR'),fill_value=5)
print(s2)

s3 = Series(list("ABC"),index=[1,5,10])
print(s3)
s4 = s3.reindex(index=range(15),method='ffill')     #自动填充
print(s4)

df = DataFrame(np.random.randint(20,size=20).reshape(4,5),index=list('ABCD'),columns=['c1','c2','c3','c4','c5'])
print(df)
df1 = df.reindex(index=list("ABCFD"),fill_value='~')
print(df1)      #会有有一行空的NaN
df2 = df1.reindex(columns=['c1','c2','c3','c4','c5','c6'],fill_value='@')
print(df2)
print(df.drop('A',axis=0))  #axis=0 表示按index查找，axis=1表示按colimn查找
print(df.drop('c2',axis=1))



data = DataFrame(np.random.randint(10,200,size=[6,7]),index=list("ASDFHJ"),columns=['0',1,2,3,4,5,6])
print(data)
data = data.reindex(index=list('ASDFH'),fill_value='!')
print(data)
data = data.drop("A",axis=0)
data = data.drop('0',axis=1)
print(data)
