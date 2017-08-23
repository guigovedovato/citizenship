from core.bo.baseBo import BaseBo
from core.dao.residenciaDao import ResidenciaDao
import json
import core.common.utils as utils

class ResidenciaBo(BaseBo):
    def __init__(self):
        super().__init__(ResidenciaDao())

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, [])

    def insert(self, entity):
        return super().insert(entity)

    def update(self, entity_id, entity):
        return super().update(entity_id, entity)