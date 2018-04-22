import numpy as np
import pandas as pd
from pandas import DataFrame,Series
'''
df = pd.read_csv(".....csv")
print(df.head())
print(df.size)

#有一个    A  列
df["A"] = df["A"].apply(str.upper)  #A 列的所有元素被大写
#还有一个   data  列
def foo(line):
    item = line.strip().split(' ')
    return Series(item[1],item[3],item[5])
df_tmp = df["data"].apply(foo)
df_tmp.rename(columns={0:'Symbol',1:'Sepno',2:"Price"}).head()  #head()去掉
df_new = df.combine_first(df_tmp)
del df_new["data"]  #删除data列
del df_new["A"]  #删除 A 列
df_new.to_csv(".....csv")
'''

def f(l):
    return ("@")
data = DataFrame(np.random.randn(30).reshape(5,6),index=list("ABCDE"),columns=list('ABCDEF'))
print(data)
data = data.rename(index=dict(zip(list("ABCDE"),list("12345"))),columns=dict(zip(list("ABFE"),list("!@#$"))))
print(data)
del data['C']
da = data.T
da['1'] = da['1'].apply(f)
print(da)
data = da.T
data['@'] =data["@"].apply(f)
print(data)
