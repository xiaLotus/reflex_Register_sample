import sqlite3

conn = sqlite3.connect('xia.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        password TEXT
    )
''')


sql_str1 = "insert into users(name, password) values('{}',{});".format('a', '22')
sql_str2 = "insert into users(name, password) values('{}',{});".format('xxx', '655656')

cursor.execute(sql_str1)
cursor.execute(sql_str2)

conn.commit()
conn.close()
