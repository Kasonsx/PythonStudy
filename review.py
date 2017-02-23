# num = [1,2,3,4,5,6,7,8]
# newnum = []
# #for n in num[:]:
# for n in num:
# 	if n == 4:
# 		n += 4
# 	newnum.append(n)

# for n in newnum:
# 	print(n)

# a=[[1,2,3],4,5,6]
# b=a[:]
# b[0].pop()
# print(a)
# print(b)
# b.pop()
# print(a)
# print(b)

# words = ['a','Bb','cCc','dDdd']
# for w in words[:]:
# 	if len(w) > 3:
# 		words.insert(0,w)
# 		print('loop')

# for i in range(2,2):
# 	print(2%i)

# a = [1,2,3,4]
# b = [5,6,7]
# for x in zip(a,b):
# 	print(x)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
# 	print(f)
# number = 0

# class Person:

# 	def __init__(self, name, sex):
# 		self.name = name
# 		self.sex = sex

# 	def add_person(self):

# p1 = Person('K', 'male')
# p2 = Person('S', 'female')
# print(p2.number)

# with open('article.txt','r', encoding='utf-8', errors='ignore') as f:
# 	for word in f:
# 		print(word, end=' ')

# brief tour of the standard library

import os
# print(os.getcwd())
# os.chdir('/test') #改变当前工作目录
# os.system('mkdir today') # 运行命令

import shutil
# shutil.copyfile('test.txt','tst.db')
# shutil.move('/build/executables', 'installdir')

import glob
# print(glob.glob('*.py')) # 列出适配条件的文件列表

import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))
# print(random.randrange(6))
# print(random.randint(0,6))

import statistics
# data = [1,2,3,4,5,6,7]
# # 平均数
# print(statistics.mean(data))
# # 中值
# print(statistics.median(data))
# # 方差
# print(statistics.variance(data))

# 网络操作
from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
# 	for line in response:
# 		line = line.decode('utf-8')
# 		if 'EST' in line or 'EDT' in line:
# 			print(line)

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
'''def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'sxk644653293@163.com'
password = input('Password:')
to_addr = '895969293@qq.com'
stmp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = format_addr('发送测试 <%s>' % from_addr)
msg['To'] = format_addr('接收测试 <%s>' % to_addr)
msg['Subject'] = Header('Python SMTP发送', 'utf-8').encode()

server = smtplib.SMTP(stmp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()'''

# 时间
from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%Y %b %d %A"))

# birthday = date(1994, 2, 2)
# age = now - birthday
# print(age.days)

# 数据压缩
import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(t)
# zlib.decompress(t)

# 性能测量
from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a, b = b, a', 'a=1; b=2').timeit())

import doctest
# def average(values):
# 	"""Computes the arithmetic mean of a list of numbers. 

# 	>>> print(average([20, 30, 70])) 
# 	40.0 
# 	"""
# 	return sum(values)/len(values)

# doctest.testmod()

import unittest
# class TestStatisticalFunctions(unittest.TestCase):
# 	def test_average(self):
# 		self.assertEqual(average([20,30,70]),40.0)
# 		self.assertEqual(round(average([1,5,7]), 1),4.3)
# 		with self.assertRaises(ZeroDivisionError):
# 			average([])
# 		with self.assertRaises(TypeError):
# 			average(20,30,70)
# unittest.main()

# xmlrpc.client

from array import array
