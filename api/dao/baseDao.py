from api.dao.context import Database

class BaseDao:
    def __init__(self):
        base = Database()
        self.db = base.get_db()
        self.coll = None

    def set_coll(self, coll):
        self.coll = coll

    def get_all(self):
        pass

    def get_by_id(self, entity_id):
        pass

    def update(self, entity):
        pass

    def insert(self, entity):
        pass