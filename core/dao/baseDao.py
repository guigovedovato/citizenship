from core.dao.context import Database
from datetime import datetime

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

    def get_by_filter(self, query):    
        comunes_filtered = [
            {
                "_id": "ObjectId('584d947dea542a13e9ec7ae7')",
                "data_criacao": "15/08/2017",
                "comune_nome":"Barbarano Romano",
                "abrasileiramento": False,
                "obito_obrigatorio": True,
                "auto_declaracao": False,
                "status": True,
                "contato_nome":"Giulia",
                "contato_telefone":"0761414601",
                "contato_email":"comune.barbaranoromano@pec.it"
            },
            {
                "_id": "ObjectId('584d947dea542a13e9ec9iu8')",
                "data_criacao": "15/08/2017",
                "comune_nome":"San Giovani in Tuscia",
                "abrasileiramento": True,
                "obito_obrigatorio": False,
                "auto_declaracao": True,
                "status": True,
                "contato_nome":"Luciano",
                "contato_telefone":"0761414601",
                "contato_email":"comune.barbaranoromano@pec.it"
            }
        ]
        return comunes_filtered

    def update(self, entity_id, entity):
        return entity

    def insert(self, entity):
        return entity