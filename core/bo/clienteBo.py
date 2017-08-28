from core.bo.baseBo import BaseBo
from core.dao.clienteDao import ClienteDao
import json
import core.common.utils as utils

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_documents(self, document):
        #TODO
        return self.get_by_id(document["entity_id"])

    def get_board(self):
        #TODO
        return self.get_all()

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, ["cognome","nome"], [])

    def insert(self, entity):
        self.setClient(entity, ["_id","cliente","data_atualizacao","ativo"])
        return super().insert(entity)

    def setClient(self, entity, fields):
        for field in fields:
            if entity.get(field):
                entity.pop(field)

    def update(self, entity_id, entity):
        return super().update(entity_id, entity)