import sqlite3 as sq
conn_db=sq.connect('main.db')
cursor_db=conn_db.cursor()
conn_db.text_factory=str

rno=252
reserch=cursor_db.execute("SELECT * FROM ip WHERE no=:rno",{"rno":rno})
result=reserch.fetchone()
if result!=None:
	print (0)


print (1)



conn_db.commit()
cursor_db.close()
conn_db.close()