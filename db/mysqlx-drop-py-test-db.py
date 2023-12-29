import mysqlx
from config import connect_args


db = mysqlx.get_session(**connect_args)
db.drop_schema("py_test_db")
db.close()
