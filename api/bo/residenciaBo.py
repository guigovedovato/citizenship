from api.bo.baseBo import BaseBo
from api.dao.residenciaDao import ResidenciaDao

class ResidenciaBo(BaseBo):
    def __init__(self):
        super().__init__(ResidenciaDao())

    def insert(self, entity):
        return self.context.insert(entity)

    def update(self, entity_id, entity_newer):
        entity = self.context.get_by_id(entity_id)
        entity_updated = self.parse.parse_residencia(entity, entity_newer)
        return self.context.update(entity_updated)