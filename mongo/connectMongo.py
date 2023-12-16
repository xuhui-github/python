import sys
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


def main():
    """Connect to MongoDB"""
    try:
        client =MongoClient("localhost",27017)

        print("Connected successfully")
    except:
        sys.stderr.write("Could not connect to MongoDB: %" % e)

        sys.exit(1)

if __name__ == '__main__':
    main()

