# 0926
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]
L2 = sorted(L, key=by_name)
print(L2)

# 0927 装饰器

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

# now = log(now)
#@log
# now = log('execute')(now)
@log2('execute')
def now():
	print('2017-09-27')

now()

import functools
def log3(func):
	@functools.wraps(func)#保持原来的函数签名，相当于wrapper.__name__ = func.__name__
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return fnc(*args, **kw)
	return wrapper

def log4(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

def log5(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call %s()' % func.__name__)
		result = func(*args, **kw)
		print('end call %s()' % func.__name__)
		return result
	return wrapper

@log5
def test():
	print('this is the test function')

test()

def log6(arg):
	if callable(arg):#为函数
		@functools.wraps(arg)
		def wrapper(*args, **kw):
			print('call %s()' % arg.__name__)
			a = arg(*args, **kw)
			print('end call')
			return a
		return wrapper
	else:
		#字符串参数
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('call %s_%s' % (func.__name__, arg))
				f = func(*args, **kw)
				print('end call')
				return f
			return wrapper
		return decorator
@log6
def test2():
	print('this is the test2')
test2()
@log6('execute')
def test3():
	print('this is the test3')
test3()