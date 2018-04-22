import numpy as np
import pandas as pd
from pandas import DataFrame,Series


s1 =Series(np.random.randn(6),index=[list('111223'),list('abcabc')])
print(s1)
print()
print(s1['1'])
print()
print(s1['1']['a'])
print()
print(s1[:,'a'])
#多级index相当于二维的，所以可以转换成daraform
df = s1.unstack()
print( )
print(df)
print()
print(df.fillna(value="@"))
print()
df2 = DataFrame([s1['1']])
print(df2)
print()
s2 = df2.unstack()
print(s2)
print()
s3 = df.T.unstack()
print(s3)

df = DataFrame(np.arange(16).reshape(4,4),index=[list('aabb'),list('1122')],columns=[list('BBJJ'),list('8989')])
print('df')
print(df)
print("df['B']")
print(df['B'])
print(df['B']['8'])


d1 = Series(np.random.rand(4),index=[list("AASS"),list("VBVB")])
print(d1)
print(d1.unstack())
