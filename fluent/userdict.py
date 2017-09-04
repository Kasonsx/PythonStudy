#字典的变种
import collections
ct = collections.Counter('abracadabra')
print(ct)
ct.update('zzzaaaaa')
print(ct)
print(ct.most_common(2))

class StrKeyDict(collections.UserDict):
	def __