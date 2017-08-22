from core.bo.baseBo import BaseBo
from core.dao.residenciaDao import ResidenciaDao
import json

class ResidenciaBo(BaseBo):
    def __init__(self):
        super().__init__(ResidenciaDao())

    def insert(self, entity):
        return json.loads(self.context.insert(entity))