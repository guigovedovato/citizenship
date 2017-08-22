from core.dao.baseDao import BaseDao
from datetime import datetime
from pymongo import MongoClient

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.cliente)

    def insert(self, entity):
        entity["data_conversao"] = str(datetime.now().date())
        entity_inserted = self.coll.insert_one(entity).inserted_id
        return self.get_by_id(str(entity_inserted))