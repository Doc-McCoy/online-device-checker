import requests
from mongo import Mongo

db = Mongo()
clients = db.get()
for client in clients:
    print(client)
