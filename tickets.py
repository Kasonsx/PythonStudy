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

def cli():
	"""command-line interface"""
	arguements = docopt(__doc__)
	print(arguements)

if __name__ == '__main__':
	cli()