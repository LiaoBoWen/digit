import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from datetime import datetime
from matplotlib import pyplot as plt

dateli = pd.date_range('2018-05-20','2018-06-20')
print(dateli)

s1 = Series(np.random.randn(len(dateli)),index=dateli)
print(s1)
print()
# print(s1.tail())
print()
print(s1['2018-05'].mean())        ########################
s1_month = s1.resample("M").mean()  #按月采样
print(s1_month)      ########################
print()
s1_hour = s1.resample("H").ffill()     #按小时采样，但是还要填充    ffill向后填充  与  bfill向前填充
print()
print(s1_hour)




t_range =  pd.date_range('2016-01-01','2016-12-31',freq="H")
print(len(t_range))
print(t_range.size)
stock_df =DataFrame(index=t_range)
stock_df['BABA'] = np.random.randint(80,160,size=len(t_range))
stock_df["Tencent"] = np.random.randint(30,50,size=len(t_range))
print(stock_df.head())
# stock_df.plot()
# plt.show()
week_li = DataFrame()
week_li["BABA"] = stock_df["BABA"].resample("W").mean()
week_li["Tencent"] = stock_df["Tencent"].resample("W").mean()
print(week_li.head())
# week_li.plot()
# plt.show()





datel = pd.date_range('2018-1-1','2018-5-20',freq="W")
print(datel)
s = Series(np.random.rand(len(datel)),index=datel)
m = s.resample("M").mean()
print(m)
t_ran = pd.date_range('2017-4-5','2018-3-12')
ran = ["cleaner",'before-teacher','behind-teacher','real-teacher','dalao']
df = DataFrame(index=t_ran)
df1 = DataFrame()
df[ran[0]] = np.random.randint(50,70,size=len(t_ran))
df1[ran[0]] = df[ran[0]].resample("W").mean()
df[ran[1]] = np.random.randint(40,60,size=len(t_ran))
df1[ran[1]] = df[ran[1]].resample("W").mean()
df[ran[2]] = np.random.randint(30,50,size=len(t_ran))
df1[ran[2]] = df[ran[2]].resample("W").mean()
df[ran[3]] = np.random.randint(20,45,size=len(t_ran))
df1[ran[3]] = df[ran[3]].resample("W").mean()
df[ran[4]] = np.random.randint(10,40,size=len(t_ran))
df1[ran[4]] = df[ran[4]].resample("W").mean()
print(df)
df1.plot()
plt.title("Made By LiaoBoWen")
plt.xlabel('Time')
plt.ylabel("Ying Xiang Fen")
plt.title("")
plt.show()
