from flask import request
from flask_restful import Resource
import json
from core.bo.analiseBo import AnaliseBo
import core.common.utils as utils

class Analise(Resource):
    def __init__(self):
        self.analise = AnaliseBo()

    def get(self, parameter):
        if utils.is_oid(parameter):
            return self.analise.find_fields_by_id(parameter, {}), 201
        else:
            return self.analise.get_by_prospecto(parameter), 201

    def put(self, parameter):
        analise = request.json
        return self.analise.update(parameter, analise), 201

    def post(self):
        analise = request.json
        return self.analise.insert(analise), 201
