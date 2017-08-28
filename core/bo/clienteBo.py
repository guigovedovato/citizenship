from core.bo.baseBo import BaseBo
from core.bo.boardBo import BoardBo
from core.bo.documentBo import DocumentBo
from core.dao.clienteDao import ClienteDao
import json
import core.common.utils as utils

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_document(self, document):
        document = DocumentBo(self)
        return document.get_document(document)

    def get_board(self):
        board = BoardBo()
        return board.get_board()

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