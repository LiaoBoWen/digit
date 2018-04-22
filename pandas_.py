import numpy as np
import pandas as pd


pd_1 = pd.Series([1,2,3,4])
print(pd_1)
values_1 = pd_1.values
print(values_1)
print(pd_1.index)

pd_2 = pd.Series(np.arange(10,21,2))
print(pd_2,pd_2.index)

pd_3 = pd.Series({1:1,2:2,3:3})
print(pd_3,pd_3.index)
# pd_3 = pd_3.to_dict() #变成字典
# print(pd_3)
pd_3 = pd.Series(pd_3,index =[1,2,'f'])  #标号对不上的就是NaN
print(pd_3)
print(pd_3.isnull())
print(pd_3.notnull())
pd_3.name = 'demo'  #命名
print(pd_3)
print(pd_3.values)

pd_4 = pd.Series(range(2,10),index=range(3,11)) #重新设置下标
print(pd_4)


pd1 = pd.Series(np.arange(10))
pd2 = pd.Series(np.arange(4),index=[1,2,3,'5'])
print(pd2)
print(pd2['5']) #pd2[5]错误
