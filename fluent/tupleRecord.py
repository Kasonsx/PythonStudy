# 元组tuple
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA','31195855'), ('BRA', 'CE342567'), ('ESP','XDA205856')]

for passport in sorted(traveler_ids):
	pass#print('%s/%s' % passport)
# %格式运算符能被匹配到对应的元组元素上
# Result：
# BRA/CE342567
# ESP/XDA205856
# USA/31195855
for country, _ in traveler_ids:
	pass#print(country)
# for循环可以分别提取元组里的元素，也称拆包unpacking
# 因为元组中第二个元素没用，所以赋值“_”占位符
# Result：
# USA
# BRA
# ESP
latitude, longitude = lax_coordinates#元组拆包
#print(latitude)#33.9425,
#print(longitude)#-118.408056

#不使用中间变量交换两个变量的值：
a, b = 1, 2
b, a = a, b
print(a,b)

import os
_, filename = os.path.split('/home/kason/.ssh/idrsa.pub')
print(filename)
# 如果做的是国际化软件，那么 _ 可能就不是一个理想的占位
# 符，因为它也是 gettext.gettext 函数的常用别名。
# 在其他情况下，_ 会是一个很好的占位符。

#用*来处理剩下的元素——平行赋值
a, b, *rest = range(5)
print(a,b,rest)
a, b, *rest = range(2)
print(a,b,rest)
# 在平行赋值中，*前缀只能用在一个变量名前，
# 但这个变量可以在赋值表达式的任意位置
a, *body, c, d = range(5)
*head, b, c, d = range(5)

# 嵌套元组拆包
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)), # ➊
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name, latitude, longitude))

# 具名元组collectons.namedtuple
# Card = collections.namedtuple('Card', ['rank','suit'])
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')#➊
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))#➋
print(tokyo)
# namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
# The field_names are a sequence of strings such as ['x', 'y'].
# Alternatively,field_names can be a single string with each fieldname
# separated by whitespace and/or commas, for example 'x y' or 'x, y'.
#➊可以是由数个字符串组成的可迭代对象，或是由空格分隔开的字段名组成的字符串
#➋注意，元组的构造函数只接受单一的可迭代对象
print(tokyo.population,tokyo[1])
# 可以通过字段名或位置来获取一个字段信息
print(City._fields)
# Result：('name', 'country', 'population', 'coordinates')
# _fields属性是一个包含这个类所有字段名称的元组
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi =City._make(delhi_data)
# 用_make()通过接受一个可迭代对象来生成这个类的一个实例，
# 相当于City(*delhi_data)
print(delhi._asdict())
# Result: OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
# _asdict()把具名元组以collections.OrderedDict的形式返回
for key, value in delhi._asdict().items():
	print(key + ':' , value)

#作为不可变列表的元组