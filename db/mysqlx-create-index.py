import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)

schema = db.create_schema("py_test_db")
schema.drop_collection("employees")

employees = schema.create_collection("employees")


field_name = {
    "field": "$.Name",
    "type": "TEXT(60)",
    "required": True,
    "collation": "utf8mb4_0900_ai_ci",
}

field_office_location = {
    "field": "$.Office.Location",
    "type": "GEOJSON",
    "required": True,
    "options": 1,
    "srid": 4326,
}
field_birthday = {
    "field": "$.Birthday",
    "type": "DATE",
    "required": False,
}


# create a normal index on the employee's NameError
index_name = "employee_name"
index_def = {
    "fields": [field_name],
    "type": "INDEX",
}

index = employees.create_index(index_name, index_def)
index.execute()

print("Index created: {0}".format(index_name))

index_name = "employee_office_location"
index_def = {
    "fields": [field_office_location],
    "type": "SPATIAL",
}

employees.create_index(index_name, index_def).execute()

print("Index created: {0}".format(index_name))

index_name = "employee_birthday_name"
index_dev = {
    "fields": [field_birthday, field_name],
    "type": "INDEX",
}

index = employees.create_index(index_name, index_def)
index.execute()
print("Index created {0}".format(index_name))

db.close()
