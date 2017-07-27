import itchat
import requests
#from itchat.content import *

API_KEY = 'd1cfba0fde3c44208c1973cb4b88ab51'

def response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key':API_KEY,
		'info':msg,
		'userid':'robot'
	}
	try:
		r = requests.post(apiUrl, data=data).json()
		return r.get('text')
		#return r
	except:
		print('server has encountered a problem.')

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
	default_reply = 'I received:' + msg['Text']
	print(msg['FromUserName'],':',msg['Text'])
	reply = response(msg['Text'])
	code = reply.get('code')
	if code == 100000 #文本类
		pass
	elif code == 200000 #链接类
		pass
	elif code == 302000 #新闻类
		pass
	elif code == 308000 #菜谱类
	    pass
	return reply or default_reply

def lc():#loginCallback
	print('login successfully!')

def ec():#exitCallback
	print('exit!')

itchat.auto_login(hotReload=True)
itchat.run()
