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
        utils.to_int(entity, ['capacidade','camas','vencimento_aluguel','quartos'])
        return super().insert(entity)

    def update(self, entity_id, entity):
        utils.itens_false(entity, ["ativo"])
        utils.to_int(entity, ['capacidade','camas','vencimento_aluguel','quartos','vagas','capacidade_old'])
        if entity.get('capacidade_old'):
            if entity['capacidade_old'] > entity['capacidade'] :
                entity['vagas'] -= 1;
            elif entity['capacidade_old'] < entity['capacidade'] :
                entity['vagas'] += 1;
            entity.pop('capacidade_old')
        return super().update(entity_id, entity)

    def decrease_vaga(self, endereco):
        residencia = json.loads(self.get_residencia(endereco))
        residencia[0]["vagas"] -= 1
        self.set_residencia(residencia)
    
    def increase_vaga(self, endereco):
        residencia = json.loads(self.get_residencia(endereco))
        residencia[0]["vagas"] += 1
        self.set_residencia(residencia)

    def get_residencia(self, endereco):
        return self.context.get_by_filter_fields({"endereco":endereco},{"vagas":1})

    def set_residencia(self, residencia):
        new_residence = {"vagas":residencia[0]["vagas"]}
        super().update(residencia[0]["_id"]["$oid"], new_residence)

    def get_by_comune(self, comune):
        comune.update({"ativo":"True"})
        return json.loads(self.context.get_by_filter_fields(comune, {"endereco":1}))