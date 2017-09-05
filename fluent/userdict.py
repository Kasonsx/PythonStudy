#字典的变种
import collections
ct = collections.Counter('abracadabra')
print(ct)
ct.update('zzzaaaaa')
print(ct)
print(ct.most_common(2))

#UserDict继承于MutableMapping
class StrKeyDict(collections.UserDict):
	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		return self[str(key)]

	def __contains__(self, key):
		return str(key) in self.data

	def __setitem__(self, key, item):
		self.data[str(key)] = item

#不可变映射类型
#用MappingProxyType获取字典的只读实例mappingproxy
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
d_proxy[2] = 'x'#报错，不能修改
d[2] = 'B'
print(d_proxy)