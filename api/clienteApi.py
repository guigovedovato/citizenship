from flask_restful import Resource
from api.bo.clienteBo import ClienteBo

class Cliente(Resource):
    def __init__(self):
        self.cliente = ClienteBo()

    def get(self, parameter=""):
        return self.cliente.get_all()

    def put(self, parameter):
        pass
