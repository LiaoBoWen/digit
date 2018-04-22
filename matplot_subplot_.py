import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



x = np.linspace(0.0,5.0)
y1 = np.sin(np.pi*x)
y2 = np.sin(np.pi*x*2)
plt.subplot(2,2,1)      #几行几列第几个
plt.plot(x,y1,"b--")
plt.ylabel('y1')
plt.subplot(2,2,2)
plt.plot(x,y2,'y--')
plt.ylabel('y2')
plt.subplot(2,2,3)
plt.plot(x,y1,"b*")
plt.ylabel("y1")
plt.subplot(2,2,4)
plt.plot(x,y1,"r*")
plt.ylabel("y1")
plt.xlabel('x')
plt.legend()
# plt.show()

figure ,ax = plt.subplots()
ax.plot(np.linspace(0,10))
# plt.show()



figure ,ax = plt.subplots(2,2)  #分成两行两列
ax[0][0].plot(x,y1)
ax[0][1].plot(x,y2)
# ax.plot(np.linspace(0,10))
plt.show()
