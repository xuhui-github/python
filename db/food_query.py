import sqlite3
import sys

con = sqlite3.connect("food.db")
cur = con.cursor()

query = "select * from food where " + sys.argv[1]
print(query)
cur.execute(query)
names = [f[0] for f in cur.description]
for row in cur.fetchall():
    for pair in zip(names, row):
        print("{}: {}".format(*pair))
    print()
