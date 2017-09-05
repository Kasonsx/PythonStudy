#中文词云
from wordcloud import WordCloud,ImageColorGenerator
import jieba
import codecs
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# 文本
with codecs.open('novel.txt','r','utf8') as f:
	sourcetext = f.read() 
wordList = jieba.cut(sourcetext, cut_all=True)#中文分词
text = " ".join(wordList)
# print(text)
# 排除常见主谓宾表定语
stopwords = set(['我们', '他们', '大人', '没有', '不是', '一个', '什么', 
	'自己', '还有', '可以', '知道', '如果', '你们', '他们', '已经', '就是',
	'一边', '这些', '那些', '有人', '还是', '这个', '那个', '现在', '父亲', 
	'它们', '孩子', '儿子', '告诉', '一样', '不会', '不过', '这里', '不能',
	'的话', '女孩', '女人', '只有', '看到', '这么', '只是', '之后', '这样', 
	'然后', '那么', '然而', '或许', '怎么', '最后', '一起', '男孩', '女儿', 
	'夫人'])
#图片背景
background = np.array(Image.open("cover.jpeg"))
wc = WordCloud(
	background_color = "white",
	mask=background,
	stopwords=stopwords,
	font_path="simhei.ttf").generate(text)
#create coloring from image
image_colors = ImageColorGenerator(background)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
# plt.imshow(background, cmap=plt.cm.gray, interpolation="bilinear")
# plt.axis("off")
plt.show()