import numpy as np
import pandas as pd
from  pandas import DataFrame,Series


df1 = np.random.randint(10,size=[3,3])
df2 = np.random.randint(10,21,size=[3,3])
df3 = np.concatenate([df1,df2]) #axis选择连接的方式 （横 竖）
print(df3)
print()
s1 =Series(range(1,4),index=[list("ABC")])
s2 =Series(range(4,6),index=[list("XY")])
s3 =pd.concat([s1,s2],axis=1)   #会变成dataframe
pd.concat([s1,s2])
print(s3)

df_1 = DataFrame(np.random.rand(4,3),columns=[list("ABC")])
df_2 = DataFrame(np.random.rand(4,3),columns=[list("DEF")])

print(df_1)
print(df_2)
df_3 =pd.concat([df_1,df_2])
print(df_3)

'''
          A         B         C         D         E         F
0  0.460542  0.544242  0.099766       NaN       NaN       NaN
1  0.472233  0.549252  0.494030       NaN       NaN       NaN
2  0.504547  0.213874  0.004701       NaN       NaN       NaN
3  0.505980  0.955772  0.551005       NaN       NaN       NaN
0       NaN       NaN       NaN  0.809402  0.880922  0.578099
1       NaN       NaN       NaN  0.717568  0.655426  0.402512
2       NaN       NaN       NaN  0.421490  0.801598  0.192797
3       NaN       NaN       NaN  0.195390  0.791668  0.545790

'''

s_1 =Series([2,np.nan,4,np.nan])
s_2 =Series(range(1,5))
s_3 =s_1.combine_first(s_2) #用s_2填充s_1相印的NaN
print(s_3)


dff1 =DataFrame(
    {
        'x':[1,np.nan,2,np.nan],
        'y':[4,np.nan,5,np.nan],
        'z':[7,np.nan,8,np.nan]
    }
)
dff2 =DataFrame(
        {
        'A':[np.nan,2,np.nan,3],
        'z':[np.nan,8,np.nan,9]
    }
)
print(dff1)
print(dff2)
dff3 = dff1.combine_first(dff2)
print(dff3)


d1 = DataFrame(np.random.rand(3,4),columns=list("ASDF"),index=list("ERT"))
d2 = DataFrame(np.random.rand(3,4),columns=list("ASDF"),index=list("ERI"))
print(d1)
print(d2)
d3 = d1.combine_first(d2)   #2填充1
print(d3)
d3 =pd.concat([d1,d2],axis=1)      #2与1合并
print(d3)
