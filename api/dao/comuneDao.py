from api.dao.baseDao import BaseDao

class ComuneDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.comune)

    def get_by_filter(self, filters):
        pass