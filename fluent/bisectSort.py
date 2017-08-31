# bisect
# 主要有两个函数：bisect和insort，利用二分查找算法
# 1.用bisect来管理已排序的序列
import bisect
import sys
haystack = [1,4,5,6,8,12,15,20,21,23,26,29,30]
needles = [0,1,2,5,8,10,22,23,29,30,31]
row_fmt = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
	for needle in reversed(needles):
		position = bisect_fn(haystack, needle)
		offset = position * '  |'
		print(row_fmt.format(needle, position, offset))

if __name__ == '__main__':
	if sys.argv[-1] == 'left':
		bisect_fn = bisect.bisect_left
	else:
		bisect_fn = bisect.bisect#即bisect_right

	print('DEMO:',bisect_fn.__name__)
	print('haystack ->', ' '.join('%2d' % n for n in haystack))
	demo(bisect_fn)

#示例：根据分数判断成绩
def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)
	return grades[i]
print([grade(score) for score in [33,99,77,70,89,90,100]])

#2.用bisect.insort插入新元素
# insort(seq,item)把变量item插入到序列seq中，并保持seq的升序顺序
import random
SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
	newItem = random.randrange(SIZE*2)
	bisect.insort(my_list, newItem)
	print('%2d - >' % newItem, my_list)