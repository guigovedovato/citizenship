from core.bo.baseBo import BaseBo
from core.dao.clienteDao import ClienteDao
import json
import core.common.utils as utils

class BoardBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_board(self):
        pass