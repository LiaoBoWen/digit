import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series


s1 = Series(np.random.randn(1000)).cumsum() #cumsum起累加的作用
s2 = Series(np.random.randn(1000)).cumsum() #cumsum起累加的作用
print(s1)
s1.plot(kind='line',grid=True,label='s1',title="this is s1",style='ro--')    #grid是否显示方格
s2.plot(kind='line',grid=True,label='s2',title="this is s2",style='--')    #grid是否显示方格
plt.legend()
# plt.show()
figure, ax =plt.subplots(2,1)
s1[:10].plot(ax=ax[0],label="s1",kind="bar")
s2.plot(ax=ax[1],label='s2')
plt.show()
