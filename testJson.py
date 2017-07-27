import json,requests

API_KEY = 'd1cfba0fde3c44208c1973cb4b88ab51'
def response(msg):#robot reply
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key':API_KEY,
		'info':msg,
		'userid':'robot'
	}
	try:
		r = requests.post(apiUrl, data=data).json()
		return r
	except:
		print('server has encountered a problem.')

result = (response("肇庆天气"))
print( "{0}\n{1}".format(result.get('text'),result.get('url')))

# 新闻类 
# {'url': 'http://m.toutiao.com/#channel=', 'code': 200000, 'text': '亲，已帮你找到新闻信息'}
# newsList = result.get('url')
# print(result.get('text')+'\n'+result.get('url'))