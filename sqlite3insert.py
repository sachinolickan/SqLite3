import sqlite3
db=sqlite3.connect("mydata") #connection object created
cursor=db.cursor() #cursor object created
cursor.execute("insert into profile values(104,'Fahi','fahi@gmail.com','abc126')")
db.commit() #to save
db.close()

