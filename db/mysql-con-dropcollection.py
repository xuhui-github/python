import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.get_schema("py_test_db")

schema.drop_collection("my_docs")
schema.drop_collection("employees")
schema.drop_collection("customers")

db.drop_schema("py_test_db")
db.close()
