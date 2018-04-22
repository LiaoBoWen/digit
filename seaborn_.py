import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame,Series

s1 = Series(np.random.randn(1000))
sns.distplot(s1,hist=True,kde=True,rug=True)    #rug下方的线代表密度
sns.kdeplot(s1,shade=True)  #shade 填充
