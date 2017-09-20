# 函数de参数
#1.可变参数，参数前加*,*arg传入的参数可为0或任意个，相当于一个元组tuple
def person1(name, age, *arg):
	print('name:',name,'age:',age,'arg',arg)
person1('k', 23)
person1('k', 23 , 'arg')
person1('k', 23 , 1,2,3)
person1('k', 23, [1,2,3])

#2.关键字参数，参数前加**，**kw传入的参数可为0或任意个，相当于一个字典dict
def person2(name, age, **kw):
	print('name:',name,'age:',age,'kw',kw)
person2('k', 23)
person2('k', 23 , kw='dict')#需要传入额外的参数名及其值

#3.命名关键字参数，需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 用于限制关键字参数的名字，比如只接受city和job作为关键字参数
# 并且必须传入参数，否则调用将报错
def person3(name, age, *, city, job):
	print(name,age,city,job)
#person3('k', 23) 会报错
person3('k', 23, city='sz', job='it')

#若函数定义中已有一个可变参数，其后的命名关键字参数就不需要加特殊分隔符*
def person4(name, age, *arg, city, job):
	print(name, age, arg, city, job)
person4('k', 23,city='sz',job='it')

# 参数组合，参数定义顺序应为：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
	pass
def f2(a, b, c=0, *, d, **kw):
	pass
