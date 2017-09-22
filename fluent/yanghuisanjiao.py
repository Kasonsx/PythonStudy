# 函数中加入yield关键字，变成generator
# 执行时遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 杨辉三角
def triangles():
	yield [1]
	L = [1,1]
	yield L
	while True:
		L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
		yield L

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break