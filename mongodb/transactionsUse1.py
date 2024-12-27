# coding: utf-8
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
client.db.testdb
client.testdb
client.testdb.users
orders = client.testdb.orders
orders
orders.count_documents({})
inventory = client.testdb.inventory
inventory.count_documents({})
with client.start_session() as session:
    with session.start_transaction():
        orders.insert_one({"sku": "abc123", "qty": 100}, session=session)
        inventory.update_one(
            {"sku": "abc123", "qty": {"$gte": 100}},
            {"$inc": {"qty": -100}},
            session=session,
        )
