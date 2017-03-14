import requests
from lxml import etree
url = 'https://www.zhihu.com/#signin'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
z = requests.get(url, headers=headers)
html = etree.HTML(z.content)
_xsrf = html.xpath('//input[@name="_xsrf"]/@value')[0]
print(_xsrf)
loginurl = 'https://www.zhihu.com/login/email'
formdata = {
	'_xsrf' : _xsrf,
	'password' : 'mendosai89757',
	'captcha_type' : 'cn',
	'email' : 'sxk644653293@163.com'
}
response = requests.post(url=loginurl, data=formdata, headers=headers)
print(response.status_code)
print(response.content)
print(response.json()['msg'])