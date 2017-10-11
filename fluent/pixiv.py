#pixiv
# -*- coding: utf-8 -*-
#pixiv网下载账号收藏图片爬虫
import requests
from parsel import Selector
import os

url = 'https://www.pixiv.net/bookmark.php'#收藏

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Cookie':'p_ab_id=7; p_ab_id_2=8; _ga=GA1.2.168375158.1505697943; device_token=1b69bf565a154a1b8f0284784a1709bb; login_ever=yes; __utma=235335808.168375158.1505697943.1505697943.1505697943.1; __utmc=235335808; __utmz=235335808.1505697943.1.1.utmcsr=link.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=7424306=1^9=p_ab_id=7=1^10=p_ab_id_2=8=1^11=lang=zh=1; is_sensei_service_user=1; bookmark_tag_type=count; bookmark_tag_order=desc; howto_recent_view_history=64967449%2C65304741; a_type=0; b_type=1; PHPSESSID=7424306_720c4622895bfa72f0a7bb217d1321f6; module_orders_mypage=%5B%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D',
	'Host':'www.pixiv.net',
	'Referer':'https://www.pixiv.net/',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

def url_request(url):
	try:
		response = requests.get(url, headers=headers, timeout=10)
		#print(response.status_code)
		if response.status_code == 200:
			sel = Selector(text=response.text)
			return sel
	except requests.exceptions.ConnectionError:
		print("网络连接失败！")
			
def get_img(url):
	selector = url_request(url)
	imageurls = []
	num = 1
	for img in selector.xpath('//li[@class="image-item"]/a[@style="display:block"]/@href').extract():
		img_url = "https://www.pixiv.net/" + img
		print(num," ",img_url)
		img = url_request(img_url).xpath('//div[@class="_layout-thumbnail ui-modal-trigger"]/img/@src').extract_first()
		if img is not None:
			img = img.replace('c/600x600/img-master', 'img-original')
			img = img.replace('_master1200', '')
			print(img)
			imageurls.append(img)
			
		else:
			multiurls = "https://www.pixiv.net/" + url_request(img_url).xpath('//div[@class="works_display"]/a[@class=" _work multiple "]/@href').extract_first()
			print(multiurls)
			for img_ in url_request(multiurls).xpath('//div[@class="item-container"]/img/@src').extract():
				img_ = img_.replace('img-master', 'img-original')
				img_ = img_.replace('_master1200', '')
				print(img_)
				imageurls.append(img_)
		num += 1
	return imageurls

def saveUrls(imageurls):
	with open('ImageURLs.txt','a+') as f:
		for i in imageurls:
			f.write(i + "\r\n")

def downloadImage(url):
	imageurls = get_img(url)
	#下载图片
	# for img in imageurls:
	# 	try:
	# 		image = requests.get(img, headers=headers, timeout=10)
	# 	except requests.exceptions.ConnectionError:
	# 		img = img.replace('.jpg', '.png')
	# 		image = requests.get(img, headers=headers, timeout=10)
	# 	filename = img.split('/')[-1]
	# 	with open(filename, 'wb') as f:
	# 		f.write(image.content)
	# 	print("已下载好", filename)

if __name__ == '__main__':
	downloadImage(url)
	print('下载完成')

