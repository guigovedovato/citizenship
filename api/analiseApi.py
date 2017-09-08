from flask import request
from flask_restful import Resource
import json
from core.bo.analiseBo import AnaliseBo

class Analise(Resource):
    def __init__(self):
        self.analise = AnaliseBo()

    def get(self, parameter):
        return self.analise.find_fields_by_id(parameter), 201

    def put(self, parameter):
        analise = request.json
        return self.analise.update(parameter, analise), 201

    def post(self):
        analise = request.json
        return self.analise.insert(analise), 201
