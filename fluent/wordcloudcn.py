#中文词云
from wordcloud import WordCloud
import jieba
import codecs
import matplotlib.pyplot as plt

with codecs.open('novel.txt','r','utf8') as f:
	sourcetext = f.read() 

wordList = jieba.cut(sourcetext, cut_all=True)#中文分词
text = " ".join(wordList)
# print(text)
wc = WordCloud(font_path="simhei.ttf").generate(text)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()