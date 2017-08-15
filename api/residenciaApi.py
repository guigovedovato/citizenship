from flask_restful import Resource
from api.bo.residenciaBo import ResidenciaBo

class Residencia(Resource):
    def __init__(self):
        self.residencia = ResidenciaBo()

    def get(self, parameter=""):
        return self.residencia.get_all()

    def put(self, parameter):
        pass

    def post(self):
        pass
