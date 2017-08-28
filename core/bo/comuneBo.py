from core.bo.baseBo import BaseBo
from core.dao.comuneDao import ComuneDao
import json
import core.common.utils as utils

class ComuneBo(BaseBo):
    def __init__(self):
        super().__init__(ComuneDao())
        self.fields = ["abrasileiramento","obito","auto_declaracao"]

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, ["nome_comune"], [])

    def insert(self, entity):
        utils.itensFalse(entity, self.fields)
        return super().insert(entity)

    def update(self, entity_id, entity):
        self.fields.append("ativo")
        utils.itensFalse(entity, self.fields)
        return super().update(entity_id, entity)

    