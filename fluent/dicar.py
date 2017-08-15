# -*- coding:utf-8 -*-
#
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
#[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
#等价于
for color in colors:
	for size in sizes:
		print((color, size))

#Python会忽略代码中[]、{}和()中的换行
tshirts = [(color, size) for size in sizes
						for color in colors]

#以下为生成器表达式
symbols = '$¢£¥€¤'
t = tuple(ord(symbol) for symbol in symbols)

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
	print(tshirt)
	