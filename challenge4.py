from urllib.request import urlopen
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"
# response = urlopen(url+nothing)
# print(response.read())
count = 1
while nothing:
	#try:
		response = urlopen(url+nothing,timeout=60)
		html = response.read()

		nothing = ''.join(re.findall("[0-9]+"),html)
		print(count,"\n",url+nothing)
		count += 1
	# except:
	# 	print(html)