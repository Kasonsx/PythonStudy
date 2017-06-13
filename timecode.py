import timeit

L = [1,2,3,4,5,6]
def fun(x):
	return x*x
def is_even(x):
	return x%2==0

s = timeit.default_timer()
print(map(fun,L))
print(filter(is_even, L))
e = timeit.default_timer()
print(e-s)

s2 = timeit.default_timer()
print([x*x for x in L])
print([x for x in L if x%2==0])
e2 = timeit.default_timer()
print(e2-s2)