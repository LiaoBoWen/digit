import  numpy as np
import pandas as pd
from pandas import Series,DataFrame
import webbrowser
#
# link = 'https://www.tiobe.com/tiobe-index/'
# # webbrowser.open(link)
# df = pd.read_clipboard()    #获取粘贴板
# print(df)
# print(type(df))
# print(df.columns)   #获取有哪些列？
# # print(df.Ratings)
# df_new = DataFrame(df,columns=['Programming Language ','Ratings '])
# print(df_new)
# print(df['Ratings '])
# print(type(df['Ratings ']))
# df_new = DataFrame(df,columns=['Programming Language ','Rat ']) #不存在就NaN
# df_new['Rat '] = np.arange(6)
# print(df_new)
# df_new['Rat '] = pd.Series([100,200],index=[1,2])
# print(df_new)

data = {"Country":['liao','bo','wen'],'Captical':['li','b','we']}
print(DataFrame(data,columns=['country','Captical']))
print(pd.Series(data))
s1 = pd.Series(data["Country"]) #每一列都是series类型
s2 = pd.Series(data["Captical"])
print(s1,s1.index,'==========================')
df2 = DataFrame([s1,s2],index=['L','B'])
df2 = df2.T
print(df2,'================')

df1 = DataFrame(data)
print(df1)
for row in df1.iterrows():
    print(row,type(row),len(row),row[0],row[1],sep='\n')     ##每一行都是一个name和一个series类型组成
