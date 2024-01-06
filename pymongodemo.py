import pymongo
from pymongo import MongoClient 
from pprint import pprint

client = MongoClient('localhost',27017)
db = client['testdb']
users = db['users']

for user in users.find():
    pprint(user)

for user in users.find({"username": "hui"}):
    pprint(user)
client.close()



