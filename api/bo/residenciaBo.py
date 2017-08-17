from api.bo.baseBo import BaseBo
from api.dao.residenciaDao import ResidenciaDao

class ResidenciaBo(BaseBo):
    def __init__(self):
        super().__init__(ResidenciaDao())

    def insert(self, entity):
        return self.context.insert(entity)