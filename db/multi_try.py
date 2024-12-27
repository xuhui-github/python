#!/usr/bin/python
import MySQLdb, sys

con = MySQLdb.connect(host="localhost", user="xuhui", passwd="flower", db="employees")

identifier = sys.argv[1]
statement = """select * from employees where emp_no = %s""" % (identifier)
cur = con.cursor()
try:
    cur.execute(statement)
    results = cur.fetchall()
    print(results)
except MySQLdb.OperationalError as e:
    raise e
except MySQLdb.ProgrammingError as e:
    raise e
