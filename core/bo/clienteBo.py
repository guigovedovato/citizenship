from core.bo.baseBo import BaseBo
from core.dao.clienteDao import ClienteDao

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_contract(self, entity_id):
        #TODO
        return self.context.get_by_id(entity_id)

    def get_board(self):
        #TODO
        return self.context.get_all()