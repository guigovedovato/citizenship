from core.bo.baseBo import BaseBo
from core.dao.prospectoDao import ProspectoDao
import json
from core.bo.clienteBo import ClienteBo
import core.common.utils as utils

class ProspectoBo(BaseBo):
    def __init__(self):
        super().__init__(ProspectoDao())

    def get_all(self):
        return self.get_by_filter({"cliente":"False"})
    
    def convert(self, entity_id):
        ex_prospecto = self.update(entity_id, {"cliente":"True"})
        cliente = ClienteBo()
        cliente.insert(ex_prospecto)
        return "O prospecto {0} foi convertido para cliente com sucesso".format(ex_prospecto["nome"])

    def do_analise(self, entity_id):
        analise = self.find_fields(entity_id, {"analise": 1, "_id": 0})
        if not analise.get("analise"):
            analise = self.analise(entity_id)
            self.update(entity_id, {"analise": analise})
            return analise
        else:
            return analise.get("analise")

    def analise(self, entity_id):
        #TODO
        return "a analise {0} nao contem erros".format(entity_id)

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, [])

    def insert(self, entity):
        return super().insert(entity)

    def update(self, entity_id, entity):
        return super().update(entity_id, entity)

    def find_fields(self, entity_id, fields):
        return json.loads(self.context.find_fields(entity_id, fields))