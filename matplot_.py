import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import cmath


a = [1,2,3]
b = [4,5,6]
c = [10,8,6]
d =[1,8,3]
x = np.arange(0,2,0.1)
y = [cmath.e**i for i in x ]
# t = np.arange(0,10,0.000001)
# s = 3*np.sin(t*np.pi)
plt.plot(c,d,"r--",label='qqq')       #第三个参数是颜色第一个字母加先线的形状
plt.plot(x*2,y,"y--",label='iii')
plt.plot(x,y,"g--",label='ii')
plt.title("ada")
plt.xlabel("x:")
plt.ylabel("y:")
plt.legend()        #显示样例
plt.show()





x = np.linspace(0.0,5.0)
y1 = np.sin(np.pi*x)
y2 = np.sin(np.pi*x*2)
plt.plot(x,y1,"bo",label="y1")
plt.plot(x,y2,"r-",label="y2")
plt.title(" text ")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
