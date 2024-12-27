import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
print("Retrieving non-default schema")

schema = db.get_schema("py_test_db")
print("Schema name: {0}".format(schema.name))
db.close()
