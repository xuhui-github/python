import mysqlx

from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.create_schema("py_test_db")
db.close()
