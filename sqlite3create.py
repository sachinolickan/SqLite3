import sqlite3
db=sqlite3.connect("mydata") #connection object created
cursor=db.cursor() #cursor object created
cursor.execute("create table profile(id int primary key,name text,username text,password text)")

db.commit() #to save
db.close()
