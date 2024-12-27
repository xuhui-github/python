from pymongo import mongo_client

client1 = mongo_client.MongoClient("localhost", 27017)
db1 = client1.db["testdb"]
