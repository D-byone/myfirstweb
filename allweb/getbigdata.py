
# -*- coding: utf-8 -*-
import MySQLdb
from MySQLdb import cursors
import threading


weibolist = []



def run(conn,idlist):
	cur = conn.cursor()
	for i in idlist:
		print "===%d" % i
		sql = 'select * from tweets where id="%d"' % i
		cur.execute(sql)
		r = cur.fetchall()
		# s = "%s\n" % r[0][3]
		weibolist.append(r)
	cur.close()
	conn.close()

if __name__ == "__main__":
	conn1 = MySQLdb.connect(host="localhost",
                                user='root',
                                passwd='wangfeilong',
                                db='sinaweibo_tweets',
                                port=3306,
                                charset='utf8')
	conn2 = MySQLdb.connect(host="localhost",
                                user='root',
                                passwd='wangfeilong',
                                db='sinaweibo_tweets',
                                port=3306,
                                charset='utf8')
	conn3 = MySQLdb.connect(host="localhost",
                                user='root',
                                passwd='wangfeilong',
                                db='sinaweibo_tweets',
                                port=3306,
                                charset='utf8')
	conn4 = MySQLdb.connect(host="localhost",
                                user='root',
                                passwd='wangfeilong',
                                db='sinaweibo_tweets',
                                port=3306,
                                charset='utf8')
	l = range(1000)

	# t1 = threading.Thread(target=run,args=(conn1,l))
	t1 = threading.Thread(target=run,args=(conn1,l[0::4]))
	t2 = threading.Thread(target=run,args=(conn2,l[1::4]))
	t3 = threading.Thread(target=run,args=(conn3,l[2::4]))
	t4 = threading.Thread(target=run,args=(conn4,l[3::4]))

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()
	print len(weibolist)