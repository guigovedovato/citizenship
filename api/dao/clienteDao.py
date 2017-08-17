from api.dao.baseDao import BaseDao

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__()
        super().set_coll(self.db.cliente)

    def get_by_filter(self, filters):
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
            },
            {
                'id': 3,
                'title': u'cliente filtro',
                'description': u'Need to find a good Python tutorial on the web', 
                'done': False
            }
        ]