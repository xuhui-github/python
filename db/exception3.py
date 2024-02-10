#!/usr/bin/python
import MySQLdb, sys

mydb = MySQLdb.connect(host="localhost", user="xuhui", passwd="flower", db="employees")

cur = mydb.cursor()
statement = """select count(*) as ammount from employees"""

try:
    cur.execute(statement)
    results = cur.fetchall()
    print(results)
except MySQLdb.OperationalError as e:
    raise e
