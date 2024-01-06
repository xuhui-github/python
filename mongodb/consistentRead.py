



client = MongoClient('localhost',27017)

with client.start_session(causal_consistency=True) as session:
    collection = client.db.collection
    collection.update_one({"_id": 1 },{"$set": {"x": 10}} ,session=session)
    secondary_c = collection.with_options(read_preference=ReadPrefence.SECODARY)

    secondary_c.find_one("_id": 1},session=session)



