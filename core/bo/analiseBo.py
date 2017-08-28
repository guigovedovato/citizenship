from core.bo.baseBo import BaseBo
from core.dao.analiseDao import AnaliseDao
import json
import core.common.utils as utils

class AnaliseBo(BaseBo):
    def __init__(self):
        super().__init__(AnaliseDao())

    def do_analise(self, entity_id):
        pass