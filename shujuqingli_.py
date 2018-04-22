import numpy as np
import pandas as pd
from pandas import DataFrame,Series


df =pd.read_csv('....csv')
#删除   unnamed:0  这列
del df["unanmed:0"]
print(df.size)
print(df.head())
print(df["Seqno"].unique())
print(df["Seqno"].duplicated())  #是否有与之前的数据重复的数据，有的话就True  不重复就False
type(df["Seqno"].drop_duplicates())     #返回Sereies类型
df.drop_duplicates()    #返回的可能是为完全清洗的
df.drop_duplicates(["Seqno"],keep="first")   #按照Seqno这一列来对整个表进行清洗       #keep是保留的唯一的元素的位置，如：first，last
