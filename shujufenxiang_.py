import numpy as np
import pandas as pd
from pandas import DataFrame,Series

score_li = Series(np.random.randint(40,100,size=20))
print(score_li)
print()
bin = [0,59,70,80,100]
score_cat = pd.cut(score_li,bin)
print(score_cat)
print(pd.value_counts(score_cat))

df = DataFrame()
df['score'] = score_li
print(df)
df['studet'] = [pd.util.testing.rands(3) for i in range(20)]
print(df)
df['categories'] = pd.cut(df['score'],bin,labels=['Low','Ok','Good','Great'],)
print(df)


li = [pd.util.testing.rands(7) for i in range(20)]
print(li)
