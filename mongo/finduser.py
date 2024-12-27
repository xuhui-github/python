from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

con = MongoClient("localhost", 27017)
db = con["testdb"]
cur = db["users"].find().limit(2)
for user in cur:
    print(user["username"])
cur.close()
con.close()
