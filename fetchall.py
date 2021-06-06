
import pymysql
connectDB = pymysql.connect(host='localhost',
                      user='root',
                      password='root',
                      database='projectdatabase')
 
with connectDB: 
 
    cur = connectDB.cursor()
    cur.execute("SELECT * FROM users")
 
    rows = cur.fetchall() #Извлекает все строки результата запроса
 
    for row in rows:
        print("{0} {1}".format(row[0], row[1]))