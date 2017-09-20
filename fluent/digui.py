# -*- coding: utf-8 -*-
# def func(n):
# 	if n == 1:
# 		return 1
# 	return n*func(n-1)
# print(func(1000))

def fact(n):
	return fact_iter(n,1)

def fact_iter(num, summ):
	if num == 0:
		return
	elif num == 1:
		return summ
	else:
		return fact_iter(num-1, num * summ)

fact(1000)

