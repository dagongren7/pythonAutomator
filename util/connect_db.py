#coding:utf-8
# import MySQLdb.cursors
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import json
class OperationMysql:
	def __init__(self):
		self.conn = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='123456',
			db='test',
			charset='utf8',
			cursorclass=MySQLdb.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		#返回dict字典
		result = self.cur.fetchone()
		#将字典转换成字符串json
		result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select username from user where username='demo'")
	print(res)
