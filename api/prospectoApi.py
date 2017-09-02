from flask import request
from flask_restful import Resource
import json
from core.bo.prospectoBo import ProspectoBo

class Prospecto(Resource):
    def __init__(self):
        self.prospecto = ProspectoBo()

    def get(self, parameter=""):
        if parameter == "":
            return self.prospecto.get_all(), 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return self.prospecto.get_by_id(parameter["id"]), 201
            elif parameter.get('analise'):
                return self.prospecto.do_analise(parameter["analise"]), 201
            elif parameter.get('convert'):
                return self.prospecto.convert(parameter["convert"]), 201
            elif parameter.get('fields'):
                return self.prospecto.find_fields(parameter["fields"]), 201
            else:
                return self.prospecto.get_by_filter(parameter), 201

    def put(self, parameter):
        prospecto = request.json
        return self.prospecto.update(parameter, prospecto), 201

    def post(self):
        prospecto = request.json
        return self.prospecto.insert(prospecto), 201
