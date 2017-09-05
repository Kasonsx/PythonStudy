#Only english
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import jieba, codecs
import numpy as np
#读取文本
filename = 'asongoficeandfire5.txt'
with codecs.open(filename,'r','utf8') as f:
	sourcetext = f.read()
#图片背景
background = np.array(Image.open("cover.jpeg"))
#排除词汇
stopwords = set(STOPWORDS)
commonwords = ['said', 'one', 'will', 'might', 'back', 'men', 'hand', 'well',
	'even', 'man', 'never', 'made', 'us', 'two'
]
stopwords = set(commonwords)|stopwords
#stopwords.add('')
wc = WordCloud(
		background_color="white",
		mask=background,
		stopwords=stopwords,
	).generate(sourcetext)
#create coloring from image
image_colors = ImageColorGenerator(background)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
# recolor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(background, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()