#内存视图memoryview
import array
numbers = array.array('h', [-2,-1,0,1,2])#16位二进制整数
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
mem_oct = memv.cast('B')#将memv里的内容转换成'B'类型，即无符号字符
print(mem_oct.tolist())
mem_oct[5] = 4
print(numbers)

#NumPy
import numpy
a = numpy.arange(12)
print(a)
print(type(a))#<class 'numpy.ndarray'>
print(a.shape)
a.shape = 3,4
print(a)
print(a[2])
print(a[2,1])
print(a[:,1])#把第一列打印出来
print(a.transpose())#把行和列交换

#floats = numpy.loadtxt('xxx.txt')

#双向队列collections.deque
# 是一个线程安全、可以快速从两端添加或删除元素的数据类型
from collections import deque
dq = deque(range(10),maxlen=10)
print(dq)
#rotate(n):旋转操作，当n>0时队列最右边的n个元素会被移动到队列的左边
# 当n<0时最左边的n个元素会被移动到右边
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
#当对一个已满的队列做添加操作时，会按照添加方向挤掉队头后队尾的元素
dq.appendleft(-1)
print(dq)
dq.extend([11,22,33])
print(dq)
# extendleft会逐个添加元素到队列
dq.extendleft([10,20,30,40])
print(dq)