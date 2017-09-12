from core.bo.baseBo import BaseBo
from core.bo.boardBo import BoardBo
from core.bo.documentBo import DocumentBo
from core.bo.residenciaBo import ResidenciaBo
from core.dao.clienteDao import ClienteDao
import json
import core.common.utils as utils

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_document(self, witch, entity_id):
        cliente = self.get_by_id(entity_id)
        document = DocumentBo()
        return document.get_document(witch, cliente)

    def get_board(self):
        board = BoardBo()
        return board.get_board()

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, ["cognome","nome"], [])

    def insert(self, entity):
        set_client(entity, ["_id","cliente","data_atualizacao","ativo"])
        return super().insert(entity)

    def update(self, entity_id, entity):
        set_consulados(entity)
        utils.from_on_to_boolean(entity)
        utils.itens_false(entity, ["ativo"])
        if entity["ativo"] == "False" or entity["data_chegada_aire"] != "":
            if entity.get("_residencia_italia"):
                if entity["_residencia_italia"] != "":
                    residencia = ResidenciaBo()
                    residencia.increase_vaga(entity["_residencia_italia"])
                    entity["_residencia_italia"] = ""
        else:
            if entity["residencia_italia"] != entity["_residencia_italia"]:
                residencia = ResidenciaBo()
                if entity["residencia_italia"] != "":
                    residencia.decrease_vaga(entity["residencia_italia"])
                if entity["_residencia_italia"] != "":
                    residencia.increase_vaga(entity["_residencia_italia"])
                entity["_residencia_italia"] = entity["residencia_italia"]
        return json.loads(self.context.update(entity_id, entity))

    def get_by_id(self, entity_id):
        entity = super().get_by_id(entity_id)
        entity["colaborador"] = utils.get_separated_by_comma(entity["colaborador"])
        if entity.get("data_contato"):
            entity["data_contato"] = utils.get_data(entity["data_contato"])
        if entity.get("data_interesse"):
            entity["data_interesse"] = utils.get_data(entity["data_interesse"])
        if entity.get("consulado"):
            entity["consulado"] = utils.get_separated_by_comma(entity["consulado"])
        return entity

    def upload(self, entity_id, file):
        entity = self.find_fields_by_id(entity_id, {"cognome":1,"nome":1, "_id":0})
        document = DocumentBo()
        return document.save_document(file, entity)

def set_client(entity, fields):
    for field in fields:
        if entity.get(field):
            entity.pop(field)

def set_consulados(query):
    consulados = ["BH", "SP", "CR", "PA", "RJ", "RC", "BR"]
    consulado = []
    for key in consulados:
        if query.get(key):
            consulado.append(query[key])
            query.pop(key)
    query["consulado"] = consulado