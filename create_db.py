import sqlite3 as sql

#connect to SQLite
con = sql.connect('cupbkitch.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS orders")

#Create users table  in db_web database
sql ='''CREATE TABLE IF NOT EXISTS "orders" (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT,
        phone TEXT ,
        furniture INTEGER, 
        height FLOAT, 
        long FLOAT, 
        dising_number INTEGER,
        bools TEXT,
        price_furnitur FLOAT,
        date datetime
)'''

cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()