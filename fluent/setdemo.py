#集合set
l = ['spam','sapm','spam','span']
print(set(l))
print(list(set(l)))
# 集合中的元素必须为可散列的，set类型本身是不可散列
# 使用集合去除重复项，通过运算符获得交集
# 如果是空集，必须写成set()的形式
#集合字面量

# dis.dis反汇编函数
from dis import dis
print(dis('{1}'))
print(dis('set([1])'))

frozenset(range(10))

from unicodedata import name#用来获取字符的名字
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
#把编码在32~255之间的字符的名字里有“SIGN”的单词挑出

#中缀运算符需要两侧的被操作对象都是集合类型，但其他的方法只要求传入参数为可迭代对象
#如，求聚合类型a/b/c/d的合集，
#可以用a.union(b,c,d),a必须为set，b、c和d可以是任何类型的可迭代对象