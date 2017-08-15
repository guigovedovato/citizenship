from api.bo.baseBo import BaseBo
from api.dao.clienteDao import ClienteDao

class ClienteBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_contract(self, entity):
        pass

    def get_board(self):
        pass