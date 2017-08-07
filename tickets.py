# -*- coding:utf-8 -*-
"""
Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help	show help menu
	-g 			高铁
	-d 			动车
	-t 			特快
	-k 			快速
	-z 			直达

Example:
	tickets 深圳 广州 2017-07-31
	tickets -dg 成都 南京 2017-07-31
"""
from docopt import docopt
from stations import stations
import requests

def cli():
	"""command-line interface"""
	arguements = docopt(__doc__)
	print(arguements)
	from_station = stations.get(arguements['<from>'])
	to_station = stations.get(arguements['<to>'])
	date = arguements['<date>']
	# request
	url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
		date, from_station, to_station
		)
	#verify为FALSE表示不验证证书
	r = requests.get(url, verify=False)
	#print(r.json())
	available_trains = r.json()['data']
	print(available_trains)

if __name__ == '__main__':
	cli()