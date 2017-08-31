# -*- coding: utf-8 -*-
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}				#姓名字典
relationships = {}		#关系字典
lineNames = []			#每段内人物关系

#文本实体识别
#分词：判断该词的词性是不是人名（nr）
jieba.load_userdict('dict30.txt')		#加载字典
with codecs.open('novel.txt', 'r', 'utf8') as f:
	for line in f.readlines():
		poss = pseg.cut(line) 		#分词并返回该词词性
		lineNames.append([])		# 为新读入的一段添加人物名称列表
		for w in poss:
			if w.flag != 'nr'or len(w.word) < 2: 	#分词长度小于2或词性不为nr时不为人名
				continue
			lineNames[-1].append(w.word)		#为当前段的环境增加一个人物
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1		#人物出现次数+1

# with codecs.open('dict30.txt',"wb","utf8") as f:
# 	for name, times in names.items():
# 		if times >= 30:
# 			f.write(name + " 100 nr\r\n")
#print(name,times)

#根据识别结果构建网络
for line in lineNames:
	for name1 in line:
		for name2 in line:
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:
				relationships[name1][name2] = 1
			else:
				relationships[name1][name2] = relationships[name1][name2] + 1

#过滤冗余边并输出结果
# 将names和relationships输出txt文本，以供gephi可视化处理
# 假设共同出现次数少于3次是冗余边，输出时忽略
# 输出节点集合node.txt，边集合edge.txt
with codecs.open('node.txt','w','gbk') as f:
	f.write("ID Label Weight\r\n")
	for name,times in names.items():
		if times >= 20:
			f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("edge.txt", "w", "gbk") as f:
	f.write("Source Target Weight\r\n")
	for name, edges in relationships.items():
		for v,w in edges.items():
			if w > 10:
				f.write(name + " " + v + " " + str(w) + "\r\n")