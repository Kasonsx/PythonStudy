# 高阶函数
# -*- coding:utf-8 -*-
def normalize(name):
	return name.title()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod(L):
	return reduce(lambda x,y:x*y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
	pass