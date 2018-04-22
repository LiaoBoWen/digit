import numpy as np
import  pandas as pd
from pandas import DataFrame,Series

#Series的排序
df = np.random.randn(10)
s1= Series(df)
print(s1,'\n',s1.values)
print(s1.index)
s2 = s1.sort_values()    #降序排序
print(s2)

#Dataform的排序
df = DataFrame(np.random.randint(20,size=[4,5]),columns=list('ABCDE'))
print(df)
print(df['A'].sort_values())
print(df.sort_values('A'))
print('sort_values:')
print(df.sort_values('A').sort_index())




import numpy as np
import pandas as pd
from pandas import DataFrame,Series

csv_open = pd.read_csv("...")
csv_open.head().[['name','title','score']].sort_values('score',ascending=False)
