#3.4 映射的弹性键查询
#defaultdict:处理找不到的键
import sys
import re 
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
#把list构造方法作为default_factory来创建一个defaultdict
with open(sys.argv[1], encoding='utf-8') as fp:
	for line_no, line in enumerate(fp,1):
		for match in WORD_RE.findter(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index[word].append(location)
			#若index没有word的记录，则为index[word]赋值空列表

for word in sorted(index, key=str.upper):
	print(word, index[word])

#特殊方法__missing__,处理找不到的键
#只会被__getitem__调用，而对get或__contains__（in运算符使用方法）没影响


#查询时将非字符串的键转换为字符串
class StrKeyDict(dict):
	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		return self[str(key)]
	def get(self, key, default=None):
		try:
			return self[key]
		except KeyError:
			return default
	def __contains__(self,key):
		return key in self.keys() or str(key) in self.keys()

