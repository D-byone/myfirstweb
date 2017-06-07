# -*- coding: utf-8 -*-



class param(object):
	"""docstring for param"""
	def __init__(self):
		self.database = "sinaweibo_tweets"
		self.table = "information"
		self.maxlimit = 16777216
		self.limit = 1000
		self.mode = SPH_MATCH_PHRASE
		self.addre = ""

	def setparam(self, db, table, maxli, li, mode, addre):
		self.database = db
		self.table = table
		self.maxlimit = maxli
		self.limit = li
		self.mode = mode
		self.addre = addre

	def getparam(self):
		l = []
		l.append(self.database)
		l.append(self.table)
		l.append(self.maxlimit)
		l.append(self.limit)
		l.append(self.mode)
		l.append(self.addre)
		return l
