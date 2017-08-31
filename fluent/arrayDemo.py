# 数组array
# 示例：创建一个有1000万个随机浮点数的数组，将数组存放到文件
# 再从文件读取数组
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))#d为双精度浮点数类型码
print(floats[-1])
with open('floats.bin','wb') as f:#写入到二进制文件
	floats.tofile(f)

floats2 = array('d')
with open('floats.bin','rb') as f2:
	floats2.fromfile(f2, 10**7)
print(floats2[-1])
print(floats2 == floats)
