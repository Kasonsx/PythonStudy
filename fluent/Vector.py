from math import hypot

class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):# 字符串表示形式，str.format
		return 'Vector(%r, %r)' % (self.x, self.y)
	# __str__：在str()中被使用，或是在用print函数打印一个对象时才被调用
	# 如果没有__str__函数，，解释器会用__repr__替代

	def __abs__(self):
		return hypot(self.x, self.y)

	def __bool__(self):
		#return bool(abs(self))
		return bool(self.x or self.y)

	def __add__(self, other):# +加法
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):# *乘法
		return Vector(self.x*scalar, self.y*scalar)