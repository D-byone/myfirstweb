# -*- coding: utf-8 -*-
# $Id$
#

from sphinxapi import *
import sys, time
import MySQLdb
from MySQLdb import cursors
import jieba
import random

# 词云生成
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import codecs
import jieba
import os
from os import path
from PIL import Image,ImageDraw,ImageFont 

import nltk


class selectword(object):
	"""docstring for selectword"""
	def __init__(self):
		self.keyword = "微博"
		self.conn = ""
		self.cur  = ""
		self.word_dict = {}
		self.res = ""
		self.weibolist = []


	
	def setword(self,word=""):
		self.keyword = word


	def disconnectdatabase(self):
		self.cur.close()
		self.conn.close()

	def connectdatabase(self):
		self.conn = MySQLdb.connect(host="localhost",
	                                user='root',
	                                passwd='wangfeilong',
	                                db='sinaweibo_tweets',
	                                port=3306,
	                                charset='utf8')
		self.cur = self.conn.cursor()

	def select_word(self):
		print "==========start seclect"
		q = ''
		mode = SPH_MATCH_PHRASE
		host = 'localhost'
		port = 9312
		index = '*'
		maxlimit = 10000000
		limit = 1000

		# do query
		cl = SphinxClient()
		cl.SetServer ( host, port )
		cl.SetMatchMode ( mode )
		cl.SetLimits ( 0, limit, maxlimit)
		q = '%s%s ' % ( q, self.keyword )
		self.res = cl.Query ( q, index )

		if not self.res:
			print 'query failed: %s' % cl.GetLastError()
			sys.exit(1)

		if cl.GetLastWarning():
			print 'WARNING: %s\n' % cl.GetLastWarning()

		print "==========select over"
		print 'Query stats:'
		if self.res.has_key('words'):
			return (self.keyword,self.res)

	def write_sentence(self):
		punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
			﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
			々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
			︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
		print "==========start write sentence and create word_dict"
		if self.res.has_key('matches'):
			self.connectdatabase()
			for match in self.res['matches']:
				sql = 'select * from tweets where id="%d"' % match['id']
				self.cur.execute(sql)
				r = self.cur.fetchall()
				s = "%s\n" % r[0][3]
				self.weibolist.append(s)
				words = jieba.cut( s,cut_all = False)
				for i in words:
					if i not in punct:
						if self.word_dict.has_key(i):
							self.word_dict[i] += 1
						else:
							self.word_dict[i] = 0
			self.disconnectdatabase()
			print "==========write sentence and create word_dict over"

	def show_text(self):
		# if self.res.has_key('words'):
		# 	show_list = []
		# 	for info in self.res['words']:
		# 		temps = '\t\'%s\' found %d times in %d documents' % (info['word'], info['hits'], info['docs'])
		# 		show_list.append(temps)
		return self.weibolist


	# def create_worddic(self):
	# 	punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
	# 		﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
	# 		々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
	# 		︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
	# 	f1 = open('text.txt')
	# 	sentence = f1.read()
	# 	words = jieba.cut( sentence,cut_all = False)
	# 	for i in words:
	# 		if i not in punct:
	# 			if self.word_dict.has_key(i):
	# 				self.word_dict[i] += 1
	# 			else:
	# 				self.word_dict[i] = 0
	# 	f1.close()

	def creat_wordcloud(self):
		word_cloud_list = []
		word_cloud_list = self.sort_word_dict(True)
		print "==========start creat_wordcloud"
		l=['left','right','top','bottom']
		html = '''<!DOCTYPE html><html><head lang="en">
				<meta charset="utf-8"></head><body style="background-color: black"><div>'''
		for w in word_cloud_list:
			color = 'rgb(%s, %s, %s)' % (str(random.randint(0,255)), str(random.randint(0,255)), str(random.randint(0,255)))
			fontsize = int(w[1])
			temp = ';float:%s;\">' % l[random.randint(0,3)]
			html += '<span style=\"font-size:' + str(fontsize) + 'px;color:' + color + temp + "  " + w[0] + "  " + '</span>'

		html += '''</div></body></html>'''
		filename = "wordcloud.html"
		path = "templates\%s" % filename
		with open(path,'wb') as f:
			f.write(html.encode('utf8'))
		print "==========wordcloud over"
		return filename

		# comment_text = open("text.txt",'r').read()
		# cut_text = " ".join(jieba.cut(comment_text))

		# d = path.dirname(__file__)
		# color_mask = imread("timg.jpg")
		# cloud = WordCloud(
		# 		font_path = "hanyi.ttf",
		# 		background_color="white",
		# 		mask = color_mask,
		# 		max_words = 800,
		# 		max_font_size = 40)
		# word_cloud = cloud.generate(cut_text)
		# # word_cloud = cloud.generate_from_frequencies(word_l)
		# word_cloud.to_file("test_ciyun.jpg")

		# plt.imshow(word_cloud)
		# plt.axis('off')
		# plt.show()


	def sort_word_dict(self,flag=False):
		print "==========start key_word sort"
		for w in self.word_dict.keys():
			if self.word_dict[w] == 0:
				del self.word_dict[w]

		word_list = sorted(self.word_dict.items(), key=lambda d:d[1], reverse = True)
		if flag == False:
			param = min(100,len(word_list))
		else:
			param = min(1500,len(word_list))
		relate_word = word_list[:param]
		print "==========key_word sort over"
		return relate_word


	def relateruledig(self):
		print "==========start relateruledig"
		relatedata = []
		for i in self.weibolist:
			t = tuple(sorted(jieba.cut(i)))
			relatedata.append(t)
		show_data = nltk.FreqDist(relatedata)
		print "==========relateruledig over"
		param = min(100,len(show_data.keys()))
		return show_data.keys()[:param]
		
