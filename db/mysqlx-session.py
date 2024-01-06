import mysqlx.connection
from config import connect_args

db = mysqlx.get_session(
        schema="py_test_db",
        **connect_args
        )

print("Retrieving default schema")
schema = db.get_default_schema()
print("Schema name: {0}".format(schema.name))

print("ok")
db.close()
