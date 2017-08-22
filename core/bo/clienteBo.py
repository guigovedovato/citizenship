from core.bo.baseBo import BaseBo
from core.dao.clienteDao import ClienteDao
import json

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_contract(self, entity_id):
        #TODO
        return self.get_by_id(entity_id)

    def get_board(self):
        #TODO
        return self.get_all()

    def insert(self, entity):
        entity.pop("_id")
        return json.loads(self.context.insert(entity))