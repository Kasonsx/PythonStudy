# 提取火车班次数据
class TrainsCollection:
	header = '车次 始终站 时间 历时 一等 二等 软卧 硬座 无座'.split()

	def __init__(self, available_trains, options):
		"""查询到的火车班次集合
		:param available_trains:火车班次列表，每个火车班次是一个字典
		:param options:查询的选项，如高铁、动车、快车等
		"""
		self.available_trains = available_trains
		self.options = options

	def _get_duration(self, raw_train):
		duration = raw_train.get('lishi').replace(':','小时')+'分'
		if duration.startswith('00'):
			return duration[4:]
		elif duration.startswith('0'):
			return duration[1:]
		return duration

	@property
	def trains(self):
		for raw_train in self.available_trains:
			train_no = raw_train