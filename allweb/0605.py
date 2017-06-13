# -*- coding: utf-8 -*-
# from urllib.request import urlopen
# from random import randint




# 利用概率分布进行关联规则挖掘
















# def wordListSum(wordList):
# 	sum=0
# 	for word,value in wordList.items():
# 		sum+=value
# 	return sum

# def retrieveRandomWord(wordList):
# 	randIndex=randint(1,wordListSum(wordList))
# 	for word,value in wordList.items():
# 		randIndex-=value
# 		if randIndex<=0:
# 			return word

# def buildWordDict(text):
# 	# 剔除换行符和引号
# 	text=text.replace("\n"," ")
# 	text=text.replace("\"","")

# 	# 保证每个标点符号都和前面的单词在一起
# 	# 这样不会被剔除，保留在马尔科夫链中
# 	punctuation=[',','.',';',':']
# 	for symbol in punctuation:
# 		text=text.replace(symbol," "+symbol+" ")

# 	words=text.split(" ")
# 	# 过滤空单词
# 	words=[word for word in words if word !=""]

# 	wordDict={}
# 	for i in range(1,len(words)):
# 		if words[i-1] not in wordDict:
# 			# 为单词新建一个字典
# 			wordDict[words[i-1]]={}
# 		if words[i] not in wordDict[words[i-1]]:
# 			wordDict[words[i-1]][words[i]]=0
# 		wordDict[words[i-1]][words[i]]=wordDict[words[i-1]][words[i]]+1
	
# 	return wordDict

# f = open("text.txt",encoding='utf8')
# text = ""
# # text=str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
# text = " %s " % f.read()
# wordDict=buildWordDict(text)

# # 生成链长为100的马尔科夫链
# length=100
# chain=""
# currentWord=""
# for i in range(0,length):
# 	chain += currentWord+" "
# 	currentWord=retrieveRandomWord(wordDict[currentWord])
# print(chain)







# from os import path
# from scipy.misc import imread
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
# import codecs
# import jieba
# import os
# from os import path
# from PIL import Image,ImageDraw,ImageFont
# import nltk

def draw_wordcloud():
	# comment_text = open("text.txt",'r').read()

	# cut_text = " ".join(jieba.cut(comment_text))
	# print cut_text.encode('utf8')
	# d = path.dirname(__file__)
	# color_mask = imread("timg.jpg")
	# cloud = WordCloud(
	# 		font_path = "hanyi.ttf",
	# 		background_color="white",
	# 		mask = color_mask,
	# 		max_words = 1000,
	# 		max_font_size = 40)
	# word_cloud = cloud.generate(cut_text)
	# word_cloud = WordCloud().generate(cut_text)
	# word_cloud.to_file("test_ciyun.jpg")
	# plt.imshow(word_cloud)
	# plt.axis('off')
	# plt.show()
	f = open('text.txt','r').read().decode('utf8')
	relatedata = []
	for line in f:
		line = line.strip()
		t = tuple(sorted(jieba.cut(line)))
		print t
		relatedata.append(t)
	goods_fd = nltk.FreqDist(relatedata)
	print goods_fd[:50]
	print "========="
	print goods_fd[-10:]


import re
def filterSpecialSymbol(s):
	# speciaSym = re.compile('[^\u4E00-\u9FA5A-Za-z0-9]|[/\.！\@]+$')
	r1 = u'[！’!"#$%&\'\s()*+,-./:;<=>?@，。￥?★、…【】《》？“”‘’！[\]^_`{|}~]+'
	r2 = u'[\]'
	# speciaSym = re.compile('[^\u4e00-\u9fa5_a-zA-Z0-9]')
	tem = re.sub(r1,'',s)
	print tem
	# twm = re.sub(r2,'',tem)
	# print twm



if __name__ == '__main__':
	# draw_wordcloud()
	s = u'ahjkfashfkja798sh王飞龙fajdlc123\.！@#的￥%……&**'
	filterSpecialSymbol(s)









# from os import path
# from scipy.misc import imread
# import matplotlib.pyplot as plt

# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# # 获取当前文件路径
# # __file__ 为当前文件, 在ide中运行此行会报错,可改为
# # d = path.dirname('.')
# d = path.dirname(__file__)


# text = open(path.join(d, 'text.txt')).read()

# # read the mask / color image
# # taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
# # 设置背景图片
# alice_coloring = imread(path.join(d, "timg.jpg"))

# wc = WordCloud(background_color="white", #背景颜色max_words=2000,# 词云显示的最大词数
# 				mask=alice_coloring,#设置背景图片
# 				stopwords=STOPWORDS.add("said"),
# 				max_font_size=40, #字体最大值
# 				random_state=42)
# # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
# # wc.generate(text)
# wc.generate_from_frequencies(txt_freq)
# # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# # 从背景图片生成颜色值
# image_colors = ImageColorGenerator(alice_coloring)

# # 以下代码显示图片
# plt.imshow(wc)
# plt.axis("off")
# # 绘制词云
# plt.figure()
# # recolor wordcloud and show
# # we could also give color_func=image_colors directly in the constructor
# plt.imshow(wc.recolor(color_func=image_colors))
# plt.axis("off")
# # 绘制背景图片为颜色的图片
# plt.figure()
# plt.imshow(alice_coloring, cmap=plt.cm.gray)
# plt.axis("off")
# plt.show()
# # 保存图片
# wc.to_file(path.join(d, "名称.png"))



















