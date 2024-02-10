import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    """connect to MongodDB"""
    try:
        # c=Connection(host="localhost",port=27017)
        client = MongoClient("localhost", 27017)
        client.start_session()
        print("Connected successfully")
    except ConnectionFailure:
        sys.stderr.write("Could not connect to MongoDB: %s " % e)
        sys.exit(1)


if __name__ == "__main__":
    main()
