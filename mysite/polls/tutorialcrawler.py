# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 正文抓取
def parse_url2html(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html5lib')
	body = soup.find_all(class_='x-wiki-content')[0]
	html = str(body)
	with open('a.html','wb') as f:
		f.write(html)