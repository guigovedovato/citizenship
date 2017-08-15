from api.dao.baseDao import BaseDao

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.cliente)

    def get_by_filter(self, filters):
        pass