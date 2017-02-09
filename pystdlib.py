import os 
print(os.getcwd())
# print(dir(os))
# print(help(os))

# import shutil
# # 复制文件
# shutil.copyfile('README.md','readme.md.bak')
# # 移动
# shutil.move('/test','readme.md.bak')

s = 'Hello,\n world!'
print(str(s))
print(repr(s))

a = [1,2,3]
b = a
c = a[:]
print(b)
print(c)