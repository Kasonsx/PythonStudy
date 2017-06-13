import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', db='dbop', charset='utf8')
cur = conn.cursor()
cur.execute('USE dbop')

def init_db():
	cur.execute("DROP TABLE IF EXISTS person")
	sql = """CREATE TABLE person (
					id BIGINT(7) NOT NULL AUTO_INCREMENT,
					name VARCHAR(20),
					role VARCHAR(40),
					created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY (id))"""
	cur.execute(sql)

def add(name, role):
	try:
		cur.execute('INSERT INTO person (name, role) values(\"%s\",\"%s\")', (name, role))
		cur.connection.commit()
	except:
		conn.rollback()

def query(col):
	# if col:
	# 	sql = "SELECT {col} FROM person".format(col=col)
	# else:
	# 	sql = "SELECT * FROM person"
	sql = "SELECT * from person"
	try:
		cur.execute(sql)
		results = cur.fetchall()
		for row in results:
			print(row[0],row[1],row[2],row[3],sep=", ")
	except:
		print("Error.")

# def update(name,)

if __name__ == '__main__':
	init_db()
	add('名字', '角色')
	add('kkk', 'coder')
	query("name")
	conn.close()