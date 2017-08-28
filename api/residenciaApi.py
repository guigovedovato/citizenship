from flask import request
from flask_restful import Resource
import json
from core.bo.residenciaBo import ResidenciaBo

class Residencia(Resource):
    def __init__(self):
        self.residencia = ResidenciaBo()

    def get(self, parameter=""):
        if parameter == "":
            return self.residencia.get_all(), 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return self.residencia.get_by_id(parameter["id"]), 201
            elif parameter.get('fields'):
                return self.residencia.find_fields(parameter["fields"]), 201
            else:
                return self.residencia.get_by_filter(parameter), 201

    def put(self, parameter):
        residencia = request.json
        return self.residencia.update(parameter, residencia), 201

    def post(self):
        residencia = request.json
        return self.residencia.insert(residencia), 201
