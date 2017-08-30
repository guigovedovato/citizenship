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
        self.setConsulados(entity)
        return super().update(entity_id, entity)

    def get_by_id(self, entity_id):
        entity = super().get_by_id(entity_id)
        entity["colaborador"] = utils.getSeparatedByComma(entity["colaborador"])
        entity["data_contato"] = utils.getData(entity["data_contato"])
        entity["data_interesse"] = utils.getData(entity["data_interesse"])
        if(entity.get("consulado")):
            entity["consulado"] = utils.getSeparatedByComma(entity["consulado"])
        return entity

    def setConsulados(self, query):
        c = ["BH", "SP", "CR", "PA", "RJ", "RC", "BR"]
        consulado = []
        for key in c:
            if query.get(key):
                consulado.append(query[key])
                query.pop(key)             
        query["consulado"] = consulado

    def upload(self, entity_id, file):
        entity = self.find_fields_byID(entity_id, {"cognome":1,"nome":1, "_id":0})
        document = DocumentBo()
        return document.save_document(file, entity)