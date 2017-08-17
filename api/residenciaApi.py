from flask import request
from flask_restful import Resource
import json
from api.bo.residenciaBo import ResidenciaBo

class Residencia(Resource):
    def __init__(self):
        self.residencia = ResidenciaBo()

    def get(self, parameter=""):
        if parameter == "":
            return {'residencias': self.residencia.get_all()}, 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return {'residencia': self.residencia.get_by_id(int(parameter["id"]))}, 201
            else:
                return {'residencias': self.residencia.get_by_filter(parameter)}, 201

    def put(self, parameter):
        residencia_id = int(parameter)
        residencia = request.json
        return {'residencia': self.residencia.update(residencia_id, residencia)}, 201

    def post(self):
        residencia = request.json
        return {'residencia': self.residencia.insert(residencia)}, 201
