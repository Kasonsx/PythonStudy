import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9023'
response = requests.get(url, verify=False)
#print(response.text)
#test = '@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|2@bjn|北京南|VNP|beijingnan|bjn|3@bjx|北京西|BXP|beijingxi|b'
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)
#print(dict(stations))