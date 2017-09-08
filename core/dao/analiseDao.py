from core.dao.baseDao import BaseDao
import pymongo 
from bson import ObjectId, json_util

class AnaliseDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.analise)

    def get_by_prospecto(self, prospecto):
        return json_util.dumps(self.coll.find_one({'prospecto': prospecto}, {"prospecto": 1}))