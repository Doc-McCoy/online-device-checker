import os
import pymongo


class Mongo:
    def __init__(self):
        path = os.environ.get('MONGODB_URI', "mongodb://localhost:27017")
        self.mongo = pymongo.MongoClient(path)
        self.db = self.mongo["database"]
        self.client = self.db["clients"]

    def insert(self, data):
        assert isinstance(data, dict)
        self.client.insert_one(data)

    def get(self):
        #query = self.client.find({}, {'_id': False})
        query = self.client.find()
        data = {'clients': list(query)}
        return data

    def drop(self):
        self.mongo.drop_database('database')
