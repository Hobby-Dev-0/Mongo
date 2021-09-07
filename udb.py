from .bot import db
x = db["DEV"]

async def add_dev():
  X = await x.find_one({"_id": "K"})
  if X:
    await x.update_one({"_id": "K"}, {"$set": {"dev": "True"}})
  else:
    await x.insert_one({"_id": "K", "dev": "True"})
async def rm_dev():
  await x.update_one({"_id": "K"}, {"$set": {"dev": "False"}})

async def check_dev():
  X = await x.find_one({"_id": "K"})
  if X:
    return X["dev"]
  else:
    return "False"
