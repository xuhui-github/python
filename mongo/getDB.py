from pymongo import MongoClient
from pymongo.database import Database
import sys


def main():
    client = MongoClient("localhost", 27017)
    db = client.get_database("OrderExample")

    customers = db["customers"]
    print(customers.__class__.__name__)
    cursor = customers.find().limit(10)

    record = cursor.next()
    while record is not None:
        print(record["first_name"], record["last_name"])
        try:
            record = cursor.next()
        except StopIteration:
            break
    cursor.rewind()
    for customer in cursor:
        print(customer)


if __name__ == "__main__":
    main()
