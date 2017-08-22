from core.bo.baseBo import BaseBo
from core.dao.residenciaDao import ResidenciaDao
import json

class ResidenciaBo(BaseBo):
    def __init__(self):
        super().__init__(ResidenciaDao())

    def get_by_filter(self, filters):
        return super().get_by_filter(filters, [])