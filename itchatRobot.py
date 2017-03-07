import itchat
import requests

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
	except:
		print('server has encountered a problem.')

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
	default_reply = 'I received:' + msg['Text']
	print(msg['Text'])
	reply = response(['Text'])
	return reply or default_reply


itchat.auto_login(hotReload=True)
itchat.run()
