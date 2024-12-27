import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
cur.execute("select 23 as val")
con.close()
