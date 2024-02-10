import mysqlx
from config import connect_args

session = mysqlx.get_session(**connect_args)
schema = session.get_schema("py_test_db")
employees = schema.get_collection("employees")
employees.drop_index("employee_name")
print("Index employee_name has been dropped")
session.close()
