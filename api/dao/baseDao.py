from api.dao.context import Database

class BaseDao:
    def __init__(self):
        base = Database()
        self.db = base.get_base()
        self.coll = None

    def set_coll(self, coll):
        self.coll = coll

    def get_all(self):
        return [
            {
                'id': 1,
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
                'done': False
            },
            {
                'id': 2,
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web', 
                'done': False
            }
        ]

    def get_by_id(self, entity_id):
        return {
                "id": str(entity_id),
                "title": "Buy groceries",
                "description": "Milk, Cheese, Pizza, Fruit, Tylenol", 
                "done": str(False)
            }

    def update(self, entity):
        return entity

    def insert(self, entity):
        return entity