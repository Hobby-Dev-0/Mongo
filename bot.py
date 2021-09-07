import os
comfig = os.environ.get
from telethon import *
import motor, pymongo
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import asyncio

print ("Welcome to pyMongo")

def env(var, default=None):
  
  k = os.environ.get(var, default)
  
  return k


mongo = env("MONGO_URI")

if not mongo:
  
  print("Mongo DB Not Found I am Getting Exit")
  
from os import system

APP_ID = comfig("API_ID", None)

API_HASH = comfig("API_HASH", None)

s = comfig("SESSION", None)

import motor.motor_asyncio


if s:
    session = StringSession(str(s))
else:
    session = "Noob"
try:
    noob = TelegramClient(
        session=session,
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"SESSION - {e}")

noob.start()

database = motor.motor_asyncio.AsyncIOMotorClient(mongo)

db = database ["Aman"]

async def do_insert():
    result = await db.test_collection.insert_many(
        [{'i': i} for i in range(2000)])
    print('inserted %d docs' % (len(result.inserted_ids),))

noob.loop.create_task(do_insert())
if __name__ == "__main__":
  noob.run_until_disconnected()
