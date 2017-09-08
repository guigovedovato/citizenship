from core.bo.baseBo import BaseBo
from core.dao.analiseDao import AnaliseDao
import json
import core.common.utils as utils

class AnaliseBo(BaseBo):
    def __init__(self):
        super().__init__(AnaliseDao())

    def do_analise(self, entity):
        return entity

    def get_by_prospecto(self, entity):
        if(utils.is_number(entity)):
            return []
        return json.loads(self.context.get_by_prospecto(entity))

    def insert(self, entity):
        analise_inserted = super().insert(entity)
        analise_inserted.pop("_id")
        analise_inserted.pop("prospecto")
        analise_inserted.pop("ativo")
        analise_inserted.pop("data_cadastro")
        analise_inserted.pop("data_atualizacao")
        return self.do_analise(analise_inserted)

    def update(self, entity_id, entity):
        analise_updated = super().update(entity_id, entity)
        analise_updated.pop("_id")
        analise_updated.pop("prospecto")
        analise_updated.pop("ativo")
        analise_updated.pop("data_cadastro")
        analise_updated.pop("data_atualizacao")
        return self.do_analise(analise_updated)

    def find_fields_by_id(self, entity_id):
        return super().find_fields_by_id(entity_id, {"_id":0,"prospecto":0,"ativo":0,"data_cadastro":0,"data_atualizacao":0})