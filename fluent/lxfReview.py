# liaoxuefeng python review
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
#print(n,'\n',f,'\n',s1,'\n',s2,'\n',s3,'\n',s4)
print(123)
print(456.789)
print("'Hello, world'")
print(r"'Hello, \'Adam\''")
print("r\'Hello, \"Bart\"\'")
print("r\'\'\'Hello,\nLisa!\'\'\'")

r = (85-72)*100/72
print('%.1f%%' % r)

height = 1.66
weight = 65.5
bmi = weight/(height**2)
if bmi < 18.5:
	print('过轻')
elif bmi <= 25:
	print('正常')
elif bmi <= 28:
	print('过重')
elif bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')