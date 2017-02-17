from urllib.request import urlopen
# with open('chanllenge7.txt','wb') as f:
# 	f.write(urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read())
from PIL import Image
import re
img = Image.open('oxygen.png')
data = [chr(img.getpixel((i,50))[0]) for i in range(0,609,7)]
print(''.join(data))
result = re.findall('[0-9]+',''.join(data))
print(result)
print(''.join([chr(int(i)) for i in result]))