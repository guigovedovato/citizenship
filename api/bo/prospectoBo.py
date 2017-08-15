from api.bo.baseBo import BaseBo
from api.dao.prospectoDao import ProspectoDao

class ProspectoBo(BaseBo):
    def __init__(self):
        super().__init__(ProspectoDao())

    def insert(self, entity):
        pass

    def do_analise(self, entities):
        pass