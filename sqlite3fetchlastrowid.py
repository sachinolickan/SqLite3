import sqlite3
db=sqlite3.connect("mydata") #connection object created
cursor=db.cursor() #cursor object created
cursor.execute("insert into profile values(107,'manu','anju@gmail.com','abc127')")
id1=cursor.lastrowid
print(id1)
db.commit() #to save
db.close()
