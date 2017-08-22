from core.bo.baseBo import BaseBo
from core.dao.comuneDao import ComuneDao
import json

class ComuneBo(BaseBo):
    def __init__(self):
        super().__init__(ComuneDao())

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, ["nome"])