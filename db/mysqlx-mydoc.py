import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)

schema = db.get_schema("py_test_db")

docs = schema.get_collection("my_docs")

print("Name of collection: {0}".format(docs.name))
db.close()
