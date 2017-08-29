# 切片
# 列表list、元组tuple和字符串str都支持切片操作
# 在切片和区间操作里不包含区间范围的最后一个元素
l = [10, 20, 30, 40, 50, 60]
l[:2] # 在下标2的地方分割
# [10, 20]
l[2:]
# [30, 40, 50, 60]
l[:3] # 在下标3的地方分割
# [10, 20, 30]
l[3:]
# [40, 50, 60]
s = 'bicycle'
s[::3]#'bye'
s[::-1]#'elcycib'
s[::-2]#'eccb'
# 用 s[a:b:c] 的形式对 s 在 a 和 b之间以 c 为间隔取值。
# c 的值还可以为负，负值意味着反向取值。
# a:b:c 这种用法只能作为索引或者下标用在 [] 中来返回一个切片对象：slice(a, b, c)。
#对seq[start:stop:step] 进行求值的时候，Python 会调用
# seq.__getitem__(slice(start, stop, step))。

invoice = """

"""

#多维切片和省略


#二维切片a[m:n, k:l]

#给切片赋值,赋值语句的右侧必须是个可迭代对象
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
l[2:5] = [100]

#对序列使用+和*
l = [1, 2, 3]
# >>> l * 5
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# >>> 5 * 'abcd'
# 'abcdabcdabcdabcdabcd'

mylist = [[]]*3
print(mylist)
# result: [[], [], []]
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O'#指向同一对象的引用
print(weird_board)

# 序列的增量赋值
# +=的对应特殊方法为__iadd__
# *=对应__imul__
l = [1,2,3]
print(id(l))
l*=2
print(l,':',id(l))#id不变，新元素直接追加到列表上
t = (1,2,3)
print(id(t))
t*=2
print(t,':',id(t))#ID改变，新的元组被创建

#一个关于+=的谜题
t = (1,2,[30,40])
#t[2] += [50,60]
#a. t 变成 (1, 2, [30, 40, 50, 60])。
#b. 因为 tuple 不支持对它的元素赋值，所以会抛出 TypeError 异常。

#注意：
#1.不要把可变对象放在元组里
#2.增量赋值不是一个原子操作
#3.查看字节码？
#4.对Python运行原理进行可视化（http://www.pythontutor.com）

#排序list.sort()和sorted()
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)#直接返回排序结果，原列表不变
fruits.sort()#对原列表直接排序，返回None，原列表改变
#二者都有reverse和key两个关键字参数
#当列表元素比较结果相同时，相对位置与原列表里一致
sorted(fruits, key=len)
#result：['grape', 'apple', 'banana', 'raspberry']
sorted(fruits, key=len, reverse=True)
#result：['raspberry', 'banana', 'grape', 'apple']
