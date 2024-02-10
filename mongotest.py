import os.path
import mongodb

import sys
import pymongo
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

client = MongoClient("localhost", 27017)
names = client.list_database_names()

example = client.get_database("OrderExample")
collections = example.list_collections()
print("Collections in database OrderExample")

for coll in collections:
    print(coll)
customers = example.get_collection("customers")
print(customers.__class__.__name__)
print(names)
print(collections)
