#!/usr/bin/python
import MySQLdb

con = MySQLdb.connect(host="localhost", user="xuhui", passwd="flower", db="employees")

cur = con.cursor()

statement = """select * from employees limit 10"""
try:
    cur.execute(statement)
    result = cur.fetchall()
    print(result)
except MySQLdb.Error as e:
    print("An error has been passed. %s" % e)
finally:
    cur.close()
    con.close()
