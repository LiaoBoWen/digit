import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import webbrowser

link =  'https://projects.fivethirtyeight.com/flights/'
webbrowser.open(link)

df = pd.read_csv("....")
#航班实战
df = df.sort_values("arr_delay",ascending=False)[:10] #按照降序排列的前十名
#延误与非延误的比例
bili = df.['cancelled'].value_counts()#延误的sum与非延误的sum
df['delayed'] = df['arr_delay'].apply(lambda x : x>0)   #df['delayed'] 的值是True或False
bili = df['delayed'].value_counts()
bili =bili[0]/bili[0]+bili[1]
#每一个航空公司延误的情况
delay_group =df.groupby(['unique_carrier','delayed'])
print(delay_group.size)
