from core.dao.baseDao import BaseDao
from pymongo import MongoClient
from bson import ObjectId, json_util

class ProspectoDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.prospecto)

    def insert(self, entity):
        entity["cliente"] = str(False)
        return super().insert(entity)