# -*- coding: utf-8 -*-
import web
import MySQLdb
from MySQLdb import cursors

import jieba
import nltk

from selectword import selectword

urls = (
	'/start','start',
	'/input','inputword',
	'/wordcloud','createwordcloud',
	'/test','test',
	'/weibolist','show_weibolist',
	'/relate','relateinfo',
	'/relatedata','create_relatedata',
)
app = web.application(urls, globals())
render = web.template.render('templates')


s = selectword()

class start(object):
	def GET(self):
		print "==========start get"
		return render.start()

	def POST(self):
		print "==========start post"
		return render.hello_form()


# 搜索 建立索引 写如文件 生成字典
class inputword(object):
	def POST(self):
		word =''
		form = web.input()
		word = form['keyword']

		key = ''
		key = '%s%s ' % ( key, word )

		# 以下参数要求bytes编码{'docs': 255034, 'hits': 359007, 'word': '\xe4\xb8\x8a\xe6\xb5\xb7'} 上海
		global s
		s = selectword()
		s.setword(key)

		paramlist = []
		resultlist = []
		result = s.select_word()
		q = result[0]
		res = result[1]
		result_s1 = 'Query \'%s\' retrieved %d of %d matches in %s sec' % (q, res['total'], res['total_found'], res['time'])
		if res.has_key('words'):
			for info in res['words']:
				temps = '\t\'%s\' found %d times in %d documents' % (info['word'], info['hits'], info['docs'])
				resultlist.append(temps)

		s.write_sentence()
		print "==========input  post"

		paramlist.append(q)
		paramlist.append(result_s1)
		paramlist.append(resultlist)
		# print paramlist[0]
		# print paramlist[1]
		# for i in paramlist[2]:
		# 	print i
		return render.selected_word(paramlist)


	def GET(self):
		print "==========input  get"
		return render.hello_form()

# 生成词云
class createwordcloud(object):
	def POST(self):
		print "==========wordcloud post"
		global s
		s.creat_wordcloud()
		return render.wordcloud()
# 文本显示
class show_weibolist(object):
	def POST(self):
		print "==========show_weibolist post"
		return render.weibolist(s.show_text())

	def GET(self):
		print "==========show_weibolist get"

# 相关词排名
class relateinfo(object):
	def POST(self):
		print "==========relateinfo post"
		global s
		return render.relate(s.sort_word_dict(False))



class create_relatedata(object):
	def POST(self):
		print "==========create_relatedata post"
		global s
		relatedatalist =[]
		for i in s.relateruledig():
			stext = ''
			for j in i:
				stext += " %s|" % j
			stext += '\n'
			relatedatalist.append(stext)
		return render.relatedata(relatedatalist)
		
		
class test(object):
	def POST(self):
		f = open('text.txt','r').read().decode('utf8')
		relatedata = []
		for line in f:
			line = line.strip()
			t = tuple(sorted(jieba.cut(line)))
			relatedata.append(t)
		goods_fd = nltk.FreqDist(relatedata)
		return render.test(goods_fd.keys()[:50])
		


if __name__ == "__main__":
    app.run()