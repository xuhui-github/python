from pymongo import mongo_client
from pymongo import MongoClient


client = mongo_client.MongoClient("localhot", 27017, "testdb")

orders = client.db.orders
inventory = client.db.inventory

with client.start_session() as session:
    with session.start_transaction():
        order.insert_one({"sku": "abc123", "qty": 100}, session=session)
        inventory.update_one(
            {"sku": "abc123", "qty": {"$gte": 100}},
            {"$inc": {"qty": -100}},
            session=session,
        )
