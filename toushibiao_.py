import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# df = pd.read_csv("……")
# table = pd.pivot_table(df,index=['...','..'],value='..',aggfunc='sum',columns=['>>>'])    #选择聚合的方式（和，平均……）
#有点像小学的课程表




df = DataFrame(np.random.randint(10,size=[20,5]),index=list("AZXSAZXSDCXSAZXBSDCX"),columns=list("HJKLP"))
print(df)
df1 = pd.pivot_table(df,index=['H',"J"],values=["K",'L'],aggfunc="sum",columns="P",fill_value=0)
print(df1)
