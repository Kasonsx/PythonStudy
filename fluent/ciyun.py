import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

textSource = open('novel.txt').read()
wordList = jieba.cut(textSource, cut_all=True)
wl_split = " ".join(wordList)

my_wordcloud = WordCloud().generate(wl_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()