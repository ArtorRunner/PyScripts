
import pymysql
connectDB = pymysql.connect(host='localhost',
                      user='root',
                      password='root',
                      database='projectdatabase',
                      cursorclass=pymysql.cursors.DictCursor) #Обращение по названию столбцов

with connectDB:
    
    cur = connectDB.cursor() #Перемещает записи из набора результата
    cur.execute("SELECT * FROM news")

    rows = cur.fetchall()

    for row in rows:
        print(row["id"], row["title"], row["description"])