from api.bo.baseBo import BaseBo
from api.dao.clienteDao import ClienteDao

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_contract(self, entity_id):
        #TODO
        return self.context.get_by_id(entity_id)

    def get_board(self):
        #TODO
        return self.context.get_all()

    def update(self, entity_id, entity_newer):
        entity = self.context.get_by_id(entity_id)
        entity_updated = self.parse.parse_cliente(entity, entity_newer)
        return self.context.update(entity_updated)