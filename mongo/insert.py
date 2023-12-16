from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

client =MongoClient('localhost',27017)
db = client['OrderExample']
customers = db['customers']
cursor=customers.find().limit(10)
for customer in cursor:
    print(customer['first_name'])

testdb=client['testdb']
users=testdb['users']
users.insert_one({"username" : "hui","addr" : "renqiu"})
cur2=users.find()
print(cur2.next())
print(cur2.next())

