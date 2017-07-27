import itchat
import requests
#from itchat.content import *

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
		code = r.get('code')
		if code == 100000: #文本类 "text"就是回复内容
			result = r.get('text')
		elif code == 200000: #链接类 实际内容在"url"中
			result = "{0}\n{1}".format(r.get('text'),r.get('url'))
		return result
	except:
		print('server has encountered a problem.')

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
	default_reply = 'I received:' + msg['Text']
	print(msg['FromUserName'],':',msg['Text'])
	reply = response(msg['Text'])
	return reply or default_reply

def lc():#loginCallback
	print('login successfully!')

def ec():#exitCallback
	print('exit!')

itchat.auto_login(hotReload=True)
itchat.run()
