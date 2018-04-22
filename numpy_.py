import numpy as np
import pickle

li = [1.0,2.0,3,4]
li_1 = [1,3,5,7]
li_2 = [3,4,6,8]
array = np.array([li,li_1,li_2])
print(array)
print(array.size)
print(array.dtype)
print(array[1,0])
print(array[:2,2:])

array_2 = np.arange(0,10,3)
print(array_2)

array_3 = np.zeros(3)
print(array_3)
array_3 = np.zeros([4,5])
print(array_3)

array_4 = np.eye(7)
print(array_4)

a = np.arange(10)
print(a[0:-3])

import numpy as np
print(np.random.randn(10))
a = np.random.randint(10,size = 20).reshape(4,5)
b = np.random.randint(10,size = 20).reshape(5,4)
c = np.random.randint(10,size = [4,5])
d = np.random.randint(10,size = [4,5])
print(1,np.unique(a))
print(2,sum(a))
print(sum(a[0]))
print(sum(a[:,0]))#表示列
print(a.max())
print(max(a[0]))#表示行

print(a)
print(b)
print(c+d)      #问题待解决
print(c-d)      #问题待解决
print(c*d)      #问题待解决
print(c/d)

#创建矩阵
a = np.mat(a)
print(3,a)
b = np.mat(b)
print(4,b)
aa = a==5
print(a)
a[aa]=100
print(a)
print('+',c+d)
print('-',c-d)
print('*',a*b)  #矩阵的乘法要行数要等于另一个的列数
print('/',c/d)





a = np.arange(10)
b = np.arange(12)
with open ('x.pkl','wb') as f:
    pickle.dump(a,f)    #从哪里跳到哪里
with open ('x.pkl','rb') as f:
     read_1 =pickle.load(f)
print('read_1:',read_1)

np.save('one_array',a)
load_1 = np.load('one_array.npy') #注意文件名 .npy
# print('load_1:',load_1)
np.savez('two_array',a= a ,b= b)
load_2 = np.load('two_array.npz')   #注意文件后缀   .npz
# print('load_2:',load_2['a'],load_2['b'])



a = np.random.randint(7,10,size=[3,4])
b = np.random.randint(1,6,size=[4,2])
# print(a,a.shape)
# print(b,b.shape)
c = np.vstack((a,b.T))
print('=================================================')
print(a)
print(b)
print(c,a.shape,a.flatten())  #降至一维
print('=================================================')
# print(b,b.shape)
# print(a.dot(b))   #矩阵的乘法
c = np.zeros([4,5])
# print(c)




'''============练习部分=============='''
import numpy as np
a = np.random.randint(10,size=40).reshape(5,8)
print(a,sum(a),a.max(),np.unique(a))
np.save('1',a)
read = np.load('1.npy')
# print(read)
zero_ = np.eye(10,dtype=np.int)
print(zero_)


import numpy as np

a1 = np.random.rand(12).reshape(2,6)
a2 = a1.ravel() #用来还原成一维的数组
a3 = a2.reshape(6,2)
a4 = np.random.randint(10,40,size=[6,2])
a5 = np.random.randint(10,40,size=[6,2])
print(a1)
print(a2)
print(a3)
print(a4)
print(sum(a3[:,:]))
print(sum(a3[0]))
print(a3.sum())
print(np.unique(a3))
print(np.vstack((a3,a4)))   #注意里面是元组的形式
print(np.exp(a4))   #e吃米
print(np.sqrt(a4))
print(np.fabs(a4))
print(np.vsplit(a4,3))  #平均切，切完后还要是整数才行
print(np.vsplit(a4,(1,3,4,5)))  #在特定位子切
print(a4.max())
print(a4.max(axis=1))
print(a4.argmax(axis=1))    #最大的下标
print(np.tile(a4,(2,5)))        #复制*行 *列
a = np.random.rand(100)
print(a)
print(np.prod(a))   #求所有元素的积
print(np.percentile(a,q=50))    #50%的元素都是小于要打印的数的
print(np.var(a))    #方差
print(np.std(a))    #标准差
biao = np.random.normal(0,1,size=1000000)  #均值为0,标准差为1
# print(len(biao))
li = []
for i in biao:
    li.append(i)
# print(li)
biao = np.sort(biao)
print(np.min(biao))         #以下对于多维也有效
print(np.argmin(biao))  #获得最小的元素的索引
print(np.argsort(biao)) #排序前的数组中的索引
print(np.partition(biao,3)) #比3小的放在一边，比3大的放在另一边
print(np.argpartition(biao,3))  #同理
aa = np.random.randint(10,size=20)
bb = aa.reshape(4,5)
print(aa,bb)
print(np.sum(bb==4,axis=0))
print(aa==4)
print(np.ones())
