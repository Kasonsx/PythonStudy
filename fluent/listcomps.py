# listcomps - list comprehension 列表推导
# genexps - generator expression 生成器表达式

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
	codes.append(ord(symbol))
print(codes)
print(symbols)
print([ord(symbol) for symbol in symbols])

#用列表推导和map/filter组合来创建相同的表单
beyond_ascii1 = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii1)

beyond_ascii2 = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii2)

#比较二者的效率
import timeit

TIMES = 10000
SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
	return c>127
"""

def clock(label, cmd):
	res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
	print(label, *('{:.3f}'.format(x) for x in res))

clock('listcomp 	   :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c>127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
#列表推导式最快
# listcomp 	   : 0.015 0.014 0.015
# listcomp + func : 0.021 0.022 0.021
# filter + lambda : 0.023 0.022 0.021
# filter + func   : 0.022 0.021 0.021