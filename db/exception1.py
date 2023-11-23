#!/usr/bin/python

import MySQLdb

con=MySQLdb.connect(host ='localhost',
        user = 'xuhui',
        passwd = 'flower',
        db = 'employees')

cur = con.cursor()

statement = """select * from employees limit 10"""

try:
    cur.execute(statement)
    results = cur.fetchall()
    print(results)
except MySQLdb.Error:
    print("An error has been passed.")
finally:
    con.close()
    


