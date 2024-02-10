import mysql.connector
from mysql.connector import MySQLConnection

db = MySQLConnection()

print("{0:<9s}  {1:<7s} {2:<18s}".format("Stage", "charset", "collation"))
print("-" * 40)
print("{0:<9s}  {1:<7s} {2:<18s}".format("Initial", db.charset, db.collation))
