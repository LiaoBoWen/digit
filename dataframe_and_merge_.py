import numpy as np
import pandas as pd
from pandas import DataFrame,Series

df1 = DataFrame({'key1':[1,2,3],'data':[4,5,6]})
df2 = DataFrame({'key2':[1,2,4],'data':[6,5,9]})
print(df1)
df3 = pd.merge(df1,df2,on='data',how='outer')   #找都有的data列，公共列   how="right"  left  inner
print(df3)

