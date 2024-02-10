from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
with client:
    db = client.testdb
    colls = db.list_collections()

    c = colls.next()

    while c is not None:
        print(c)
        try:
            c = colls.next()
        except:
            break

        print(db.list_collection_names())

if __name__ == "__main__":
    print("__main__ going")
