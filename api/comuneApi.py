from flask import request
from flask_restful import Resource
import json
from core.bo.comuneBo import ComuneBo

class Comune(Resource):
    def __init__(self):
        self.comune = ComuneBo()

    def get(self, parameter=""):
        if parameter == "":
            return self.comune.get_all(), 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return self.comune.get_by_id(parameter["id"]), 201
            else:
                return self.comune.get_by_filter(parameter), 201

    def put(self, parameter):
        comune = request.json
        return self.comune.update(parameter, comune), 201

    def post(self):
        comune = request.json
        return self.comune.insert(comune), 201
    