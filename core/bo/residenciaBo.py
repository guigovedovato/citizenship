from core.bo.baseBo import BaseBo
from core.dao.residenciaDao import ResidenciaDao
import json
import core.common.utils as utils

class ResidenciaBo(BaseBo):
    def __init__(self):
        super().__init__(ResidenciaDao())

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, [], ["camas", "quartos", "vagas"])

    def insert(self, entity):
        entity["vagas"] = int(entity["capacidade"])
        utils.toInt(entity, ['capacidade','camas','vencimento_aluguel','quartos'])
        return super().insert(entity)

    def update(self, entity_id, entity):
        utils.itensFalse(entity, ["ativo"])
        utils.toInt(entity, ['capacidade','camas','vencimento_aluguel','quartos','vagas','capacidade_old'])
        if entity.get('capacidade_old'):
            if entity['capacidade_old'] > entity['capacidade'] :
                entity['vagas'] -= 1;
            elif entity['capacidade_old'] < entity['capacidade'] :
                entity['vagas'] += 1;
            entity.pop('capacidade_old')
        return super().update(entity_id, entity)