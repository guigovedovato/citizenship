from core.dao.context import Database
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId, json_util

class BaseDao:
    def __init__(self):
        base = Database()
        self.db = base.get_base()
        self.coll = None

    def set_coll(self, coll):
        self.coll = coll

    def get_all(self):
        output = []
        for data in self.coll.find():
            output.append(data)
        return json_util.dumps(output)

    def get_by_id(self, entity_id):
        return json_util.dumps(self.coll.find_one({'_id': ObjectId(entity_id)}))

    def get_by_filter(self, query):
        return json_util.dumps(self.coll.find(query))

    def update(self, entity_id, entity):
        entity["data_atualizacao"] = str(datetime.now().date())
        entity_updated = self.coll.update({'_id': ObjectId(entity_id)}, {'$set': entity})
        return self.get_by_id(entity_id)

    def insert(self, entity):
        entity["data_criacao"] = str(datetime.now().date())
        entity_inserted = self.coll.insert_one(entity).inserted_id
        return self.get_by_id(str(entity_inserted))