import os
os.system('pip install pymongo')
import pymongo
print("Welcome to pyMongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
