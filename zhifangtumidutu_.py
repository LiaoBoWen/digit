import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series


s1 = Series(np.random.randn(1000))
# a = plt.hist(s1,rwidth=0.5,bins=50,color='r') #rwidth间隔,bins是直方图的条数，        是一个tuple类型
# print(a[0],a[1],a[2])   #a[0]是频率，a[1]是间隔，a[2]是图

# a = Series(np.arange(10))
# plt.hist(a,rwidth=0.4)

s1.plot(kind="kde")
plt.show()
