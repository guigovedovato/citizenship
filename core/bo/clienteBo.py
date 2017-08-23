from core.bo.baseBo import BaseBo
from core.dao.clienteDao import ClienteDao
import json
import core.common.utils as utils

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_contract(self, entity_id):
        #TODO
        return self.get_by_id(entity_id)

    def get_board(self):
        #TODO
        return self.get_all()

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, [])

    def insert(self, entity):
        #TODO
        entity.pop("_id")
        entity.pop("analise")
        entity_insert = entity
        return super().insert(entity_insert)

    def update(self, entity_id, entity):
        return super().update(entity_id, entity)