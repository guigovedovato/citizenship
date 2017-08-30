from flask import request
from flask_restful import Resource
import json
from core.bo.clienteBo import ClienteBo

class Cliente(Resource):
    def __init__(self):
        self.cliente = ClienteBo()

    def get(self, parameter=""):
        if parameter == "":
            return self.cliente.get_all(), 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return self.cliente.get_by_id(parameter["id"]), 201
            elif parameter.get('document'):
                return self.cliente.get_document(parameter), 201
            elif parameter.get('board'):
                return self.cliente.get_board(), 201
            else:
                return self.cliente.get_by_filter(parameter), 201

    def put(self, parameter):
        cliente = request.json
        return self.cliente.update(parameter, cliente), 201

    def post(self, parameter):
        file = request.files['arquivo']
        return self.cliente.upload(parameter, file), 201