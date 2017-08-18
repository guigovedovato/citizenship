from core.bo.baseBo import BaseBo
from core.dao.comuneDao import ComuneDao

class ComuneBo(BaseBo):
    def __init__(self):
        super().__init__(ComuneDao())

    def insert(self, entity):
        return self.context.insert(entity)