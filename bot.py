import os
os.system("pip install pymongo && pip install dnspython && pip install motor")
comfig = os.environ.get

import motor, pymongo
  
print("Welcome to pyMongo")

def env(var, default=None):
  
  k = os.environ.get(var, default)
  
  return k


mongo = env("MONGO_URI")

if not mongo:
  
  print("Mongo DB Not Found I am Getting Exit")
  
from os import system

import motor.motor_asyncio

database = motor.motor_asyncio.AsyncIOMotorClient(mongo)

db = database ["Aman"]
