from urllib.request import urlopen
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"
# response = urlopen(url+nothing)
# #print(response.info())
# html = response.read()
# s = html.decode(encoding='utf-8')
# print(s)
# tmp = re.findall("[0-9]+",s)
# print(tmp)
count = 1
while nothing:
	try:
		response = urlopen(url+nothing,timeout=60)
		html = response.read()
		s = html.decode(encoding='utf-8')
		print(s)
		nothing = re.findall("[0-9]+",s)
		print(nothing)
		# print(count,"\n",url+nothing)
		count += 1
	except:
		print(html)