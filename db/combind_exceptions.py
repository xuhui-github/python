#!/usr/bin/python
import MySQLdb, sys

con = MySQLdb.connect(host="localhost", user="xuhui", passwd="flower", db="employees")

cur = con.cursor()
identifier = sys.argv[1]
statement = """select * from employees where id=%s""" % (identifier)

try:
    cur.execute(statement)
    results = cur.fetchall()
    print(results)
except (MySQLdb.OperationalError, MySQLdb.ProgrammingError) as e:
    raise (e)
