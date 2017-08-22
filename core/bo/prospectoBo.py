from core.bo.baseBo import BaseBo
from core.dao.prospectoDao import ProspectoDao
import json

class ProspectoBo(BaseBo):
    def __init__(self):
        super().__init__(ProspectoDao())

    def insert(self, entity):
        return json.loads(self.context.insert(entity))

    def do_analise(self, entity_id):
        #TODO
        return {"analise": "a analise {0} nao contem erros".format(entity_id)}