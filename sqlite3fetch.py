import sqlite3
db=sqlite3.connect("mydata") #connection object created
cursor=db.cursor() #cursor object created
cursor.execute("select * from profile where id=?",(101,)) 
row=cursor.fetchone()  #fetchone returns one row, 'fetchall() returns full data
print(row[0],row[1],row[2],row[3])
db.close()
