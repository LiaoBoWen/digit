import numpy as np
import pandas as pd
from pandas import DataFrame, Series


indb = pd.read_csv("reader.csv")
print(indb)
print(indb.shape)   #查看大小
print(indb.head())  #默认返回前五行
print(indb.tail())  #默认返回后五行
print(indb.head(2)) #设置返回行数
print(indb[['Mar','Change']])   #注意有两个括号
print('===================')
indb1 = indb.iloc[2:5,2:4]#这个是利用下标查询的
print(indb1)
print(indb1.loc[2:3,'2018':'Mar.1'])    #这个是利用名称（lable)查询的
