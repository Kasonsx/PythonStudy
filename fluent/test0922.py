#构造一个1, 3, 5, 7, ..., 99的列表
# 1.使用循环
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
# 2.列表生成式
print([i for i in range(1,100) if i%2!=0])
# 3.切片
print(list(range(1,100))[::2])

# 4.tuple和字符串也可以做切片操作
print((0, 1, 2, 3, 4, 5)[:3])
print('akjshdkahd'[::2])

# 判断一个对象是否为可迭代对象
from collections import Iterable
print(isinstance((x for x in range(10)), Iterable))#True
print(isinstance('abc', Iterable))#True
print(isinstance([1,2,3], Iterable))#True
print(isinstance(123, Iterable))#False

# 对list实现类似Java的下标循环
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

#
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))#True
print(isinstance([], Iterator))#False
print(isinstance({}, Iterator))#False
print(isinstance('abc', Iterator))#False
