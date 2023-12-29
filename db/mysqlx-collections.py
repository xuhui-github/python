import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)

db.drop_schema('py_test_db')
schema = db.create_schema('py_test_db')

schema.create_collection('employees')
schema.create_collection('customers')

collections = schema.get_collections()
for collection in collections:
    print("Collection name: {0}".format(collection.name))

coll_dict = { collection.name: collection for collection in collections}

db.close()


