from core.bo.baseBo import BaseBo
from core.dao.prospectoDao import ProspectoDao
from core.bo.analiseBo import AnaliseBo
from core.bo.clienteBo import ClienteBo
import core.common.utils as utils
import json

class ProspectoBo(BaseBo):
    def __init__(self):
        super().__init__(ProspectoDao())

    def get_all(self):
        return self.get_by_filter({"cliente":"False"})
    
    def convert(self, entity_id):
        ex_prospecto = self.update(entity_id, {"cliente":"True", "ativo":"False"})
        return "O prospecto {0} foi convertido para cliente com sucesso".format(ex_prospecto["cognome"])

    def get_by_filter(self, filters):
        filters.update({"cliente":"False"})
        return super().get_by_filter(filters, ["cognome","nome"], [])

    def insert(self, entity):
        set_colaborador(entity)
        entity["cliente"] = "False"
        return super().insert(entity)

    def update(self, entity_id, entity):
        set_colaborador(entity)
        utils.itens_false(entity, ["ativo"])
        saved = super().update(entity_id, entity)
        if(entity.get('cliente')):
            to_convert(saved)
        return saved

    def get_by_id(self, entity_id):
        entity = super().get_by_id(entity_id)
        entity["colaborador"] = utils.get_separated_by_comma(entity["colaborador"])
        if entity.get("data_contato"):
            entity["data_contato"] = utils.get_data(entity["data_contato"])
        print(entity)
        return entity

def to_convert(entity):
    cliente = ClienteBo()
    cliente.insert(entity)

def set_colaborador(query):
    c_list = ["c1", "c2", "c3", "c4"]
    colaboradores = []
    for key in c_list:
        if query.get(key):
            colaboradores.append(query[key])
            query.pop(key)             
    query["colaborador"] = colaboradores