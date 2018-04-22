import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series

df = DataFrame(np.random.randint(20,size=40).reshape(10,4),columns=list("ABCD"))
print(df)
print(df.iloc[5])   #第五行的abcd取值
df.iloc[5].plot()
# df.plot(kind="area",stacked=True)    #stacked 是堆叠参数
for i in df.index:
    df.iloc[i].plot()
# df["A"].plot()
plt.legend()
df.T.plot()
plt.show()
