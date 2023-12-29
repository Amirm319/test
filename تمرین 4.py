import sqlite3
con = sqlite3.connect('d:/mydata.db')
print('databas file created')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS student(id integer , Fname text , Lname text , score real)')
print('*******')

print('* * * ')
con.commit()
