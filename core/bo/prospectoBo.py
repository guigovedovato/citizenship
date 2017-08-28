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
        ex_prospecto = self.update(entity_id, {"cliente":"True", "ativo":"False"})
        cliente = ClienteBo()
        cliente.insert(ex_prospecto)
        return "O prospecto {0} foi convertido para cliente com sucesso".format(ex_prospecto["cognome"])

    def do_analise(self, entity_id):
        analise = self.find_fields_byID(entity_id, {"analise": 1, "_id": 0})
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
        filters.update({"cliente":"False"})
        return super().get_by_filter(filters, ["cognome","nome"], [])

    def insert(self, entity):
        self.setColaborador(entity)
        entity["cliente"] = "False"
        return super().insert(entity)

    def update(self, entity_id, entity):
        utils.itensFalse(entity, ["ativo"])
        return super().update(entity_id, entity)

    def setColaborador(self, query):
        c = ["c1", "c2", "c3", "c4"]
        colaboradores = []
        for key in c:
            if query.get(key):
                colaboradores.append(query[key])
                query.pop(key)             
        query["colaborador"] = colaboradores

    def get_by_id(self, entity_id):
        entity = super().get_by_id(entity_id)
        entity["colaborador"] = self.getColaborador(entity["colaborador"])
        from datetime import datetime
        d = datetime.strptime(entity["data_contato"], '%Y-%m-%d')
        entity["data_contato"] = datetime.strftime(d, "%d/%m/%Y")
        return entity

    def getColaborador(self, listaColaboradores):
        colaboradores = ""
        for colaborador in listaColaboradores:
            colaboradores += ", " + colaborador
        return colaboradores[2:]