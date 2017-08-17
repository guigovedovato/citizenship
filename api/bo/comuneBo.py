from api.bo.baseBo import BaseBo
from api.dao.comuneDao import ComuneDao

class ComuneBo(BaseBo):
    def __init__(self):
        super().__init__(ComuneDao())

    def insert(self, entity):
        return self.context.insert(entity)