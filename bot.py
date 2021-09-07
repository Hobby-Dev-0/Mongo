import os
comfig = os.environ.get
import pymongo
print("Welcome to pyMongo")
client = pymongo.MongoClient(comfig("MONGO_URI", None))
print(client)
