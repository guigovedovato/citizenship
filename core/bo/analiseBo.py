from core.bo.baseBo import BaseBo
from core.dao.analiseDao import AnaliseDao
import json
import core.common.utils as utils

class AnaliseBo(BaseBo):
    def __init__(self):
        super().__init__(AnaliseDao())

    def do_analise(self, entity):
        pass

    def get_by_prospecto(self, entity):
        if(utils.is_number(entity)):
            return []
        return {"prospecto":entity}

    def insert(self, entity):
        analise_inserted = super().insert(entity)
        return self.do_analise(analise_inserted)

    def update(self, entity_id, entity):
        analise_updated = super().update(entity_id, entity)
        return self.do_analise(analise_updated)