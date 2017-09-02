from core.dao.baseDao import BaseDao

class AnaliseDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.analise)

    def get_by_prospecto(self, prospecto):
        pass