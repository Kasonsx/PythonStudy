DIAL_CODES = [
	(86, 'China'),
	(91, 'India'),
	(1, 'United States'),
	(62, 'Indonesia'),
	(55, 'Brazil'),
	(92, 'Pakistan'),
	(880, 'Bangladesh'),
	(234, 'Nigeria'),
	(7, 'Russia'),
	(81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
print({code: country.upper() for country, code in country_code.items() if code < 66})

#用setdefault处理找不到的键
#用d.get(k, default)代替d[k],给找不到的键一个默认的返回值
#d.setdefault(k,[default])若有键k，则把它对应的值设为default。然后
# 返回这个值；若无，则让的d[k]=default，然后返回default

"""创建从一个单词到其出现情况的映射"""
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
	for line_no, line in enumerate(fp,1):
		for match in WORD_RE.findter(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
	print(word, index[word])

