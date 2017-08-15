from api.dao.baseDao import BaseDao

class ProspectoDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.prospecto)

    def get_by_filter(self, filters):
        pass