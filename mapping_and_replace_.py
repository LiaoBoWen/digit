import numpy as np
import pandas as pd
from pandas import DataFrame,Series


df1 = DataFrame({'city':['老','白','惠'],'人口':[100,200,300]},index=list('abc'))
print(df1)
df1['GDP'] = Series([10,20,30]) #默认按下标从0开始赋值
print(df1)
print("map:")
map_li = {'老':10,'白':20,'惠':30}
df1['GDP'] = df1['city'].map(map_li)
print(df1)


"""======================"""
s1 = Series(np.arange(10),index=list("asdfghjklp"))
print(s1)
print(s1.replace([1,2,3],[10,20,30]))
