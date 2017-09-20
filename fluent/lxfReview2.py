# lxf course Review
# -*- coding: utf-8 -*-
import math 
def quadratic(a,b,c):
	n1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
	n2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
	return n1,n2
# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))
assert quadratic(2,3,1) == (-0.5, -1.0), "正确"
assert quadratic(1,3,-4) == (1.0, -4.0), '正确'

def student(name, sex, addr='SZ', **score):
	print(name,sex,addr,score)

student('k','male', chinese=90, math=98)