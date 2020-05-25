

conn = s.connect(host='localhost', user='root',
                       password='zaiguru39@', db='my_db', charset='utf8')
curs = conn.cursor()
sql = "select * from test"
curs.execute(sql)

data = curs.fetchall()
print(data) #첫번째 row



sql = "INSERT INTO test (username, adress, contents) VALUES (%s,%s,%s)"
val = ("jin tae","test@naver.com","제품문의 드립니다. ")
curs.execute(sql, val)


print(curs.rowcount, "record inserted.")

conn.commit()
print(1)
conn.close()