import os
os.system("pip install pymongo && pip install dnspython && pip install motor")
comfig = os.environ.get
from telethon import *
import motor, pymongo

import asyncio

print("Welcome to pyMongo")

def env(var, default=None):
  
  k = os.environ.get(var, default)
  
  return k


mongo = env("MONGO_URI")

if not mongo:
  
  print("Mongo DB Not Found I am Getting Exit")
  
from os import system
APP_ID = comfig("API_ID", None)
API_HASH = comfig("API_HASH", None)
import motor.motor_asyncio
noob = TelegramClient(None, APP_ID, API_HASH)
database = motor.motor_asyncio.AsyncIOMotorClient(mongo)

db = database ["Aman"]
async def do_insert():
    result = await db.test_collection.insert_many(
        [{'i': i} for i in range(2000)])
    print('inserted %d docs' % (len(result.inserted_ids),))

loop = asyncio.get_event_loop()
loop.run_until_complete(do_insert())
noob.run_until_disconnected()
