from flask import request
from flask_restful import Resource
import json
from core.bo.prospectoBo import ProspectoBo

class Prospecto(Resource):
    def __init__(self):
        self.prospecto = ProspectoBo()

    def get(self, parameter=""):
        if parameter == "":
            return {'prospectos': self.prospecto.get_all()}, 201
        else:
            parameter = json.loads(parameter)
            if parameter.get('id'):
                return {'prospecto': self.prospecto.get_by_id(parameter["id"])}, 201
            elif parameter.get('analise'):
                return {'prospecto': self.prospecto.do_analise(parameter["id"])}, 201
            else:
                return {'prospectos': self.prospecto.get_by_filter(parameter)}, 201

    def put(self, parameter):
        prospecto = request.json
        return {'prospecto': self.prospecto.update(parameter, prospecto)}, 201

    def post(self):
        prospecto = request.json
        return {'prospecto': self.prospecto.insert(prospecto)}, 201
