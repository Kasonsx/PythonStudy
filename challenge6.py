# import zipfile
# import re
# file = zipfile.ZipFile('channel.zip','r')
# textfile = '%s.txt'
# nothing = "90052"
# result = open('result6.txt','w')
# while True:
# 	text = file.read(textfile % nothing)
# 	a = re.findall(r'[0-9]+',text.decode())
# 	print(text)
# 	s =file.getinfo(textfile % nothing).comment
# 	result.write(''.join(str(s))
# 	nothing = a[0]
# result.close()

import zipfile  
import re  
file = zipfile.ZipFile('channel.zip','r')  
txtfile = '%s.txt'  
nothing = 90052  
output = open('output6.txt','w')  
while 1>0:  
    text = file.read(txtfile % nothing)  
    a = re.findall(r'(\d+)',text.decode())  
    print(text) 
    s = file.getinfo(txtfile % nothing).comment
    print("s:",s)
    output.write(s.decode("utf-8"))  
    if a == []:  
        break  
    nothing = a[len(a)-1]  
output.close()
# with open('output6.txt','r') as f:
# 	print(f.comment)
