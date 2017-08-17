from api.bo.baseBo import BaseBo
from api.dao.prospectoDao import ProspectoDao

class ProspectoBo(BaseBo):
    def __init__(self):
        super().__init__(ProspectoDao())

    def insert(self, entity):
        return self.context.insert(entity)

    def do_analise(self, entity_id):
        #TODO
        return {"analise": "a analise {0} nao contem erros".format(entity_id)}

    def update(self, entity_id, entity_newer):
        entity = self.context.get_by_id(entity_id)
        entity_updated = self.parse.parse_prospecto(entity, entity_newer)
        return self.context.update(entity_updated)