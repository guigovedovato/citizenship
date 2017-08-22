from core.bo.baseBo import BaseBo
from core.dao.prospectoDao import ProspectoDao
import json
from core.bo.clienteBo import ClienteBo

class ProspectoBo(BaseBo):
    def __init__(self):
        super().__init__(ProspectoDao())

    def get_all(self):
        return self.get_by_filter({"cliente":"False"})
    
    def convert(self, entity_id):
        ex_prospecto = self.update(entity_id, {"cliente":"True"})
        cliente = ClienteBo()
        cliente.insert(ex_prospecto)
        return "o prospecto {0} foi convertido para cliente com sucesso".format(ex_prospecto["nome"])

    def do_analise(self, entity_id):
        #TODO
        analise = "a analise {0} nao contem erros".format(entity_id)
        return self.update(entity_id, {"analise": analise})