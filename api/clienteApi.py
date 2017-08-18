from flask import request
from flask_restful import Resource
import json
from core.bo.clienteBo import ClienteBo

class Cliente(Resource):
    def __init__(self):
        self.cliente = ClienteBo()

    def get(self, parameter=""):
        if parameter == "":
            return {'clientes': self.cliente.get_all()}, 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return {'cliente': self.cliente.get_by_id(parameter["id"])}, 201
            elif parameter.get('contract'):
                return {'cliente': self.cliente.get_contract(parameter["id"])}, 201
            elif parameter.get('board'):
                return {'clientes': self.cliente.get_board()}, 201
            else:
                return {'clientes': self.cliente.get_by_filter(parameter)}, 201

    def put(self, parameter):
        cliente = request.json
        return {'cliente': self.cliente.update(parameter, cliente)}, 201
