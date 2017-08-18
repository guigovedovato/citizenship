from flask import request
from flask_restful import Resource
import json
from core.bo.residenciaBo import ResidenciaBo

class Residencia(Resource):
    def __init__(self):
        self.residencia = ResidenciaBo()

    def get(self, parameter=""):
        if parameter == "":
            return {'residencias': self.residencia.get_all()}, 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return {'residencia': self.residencia.get_by_id(parameter["id"])}, 201
            else:
                return {'residencias': self.residencia.get_by_filter(parameter)}, 201

    def put(self, parameter):
        residencia = request.json
        return {'residencia': self.residencia.update(parameter, residencia)}, 201

    def post(self):
        residencia = request.json
        return {'residencia': self.residencia.insert(residencia)}, 201