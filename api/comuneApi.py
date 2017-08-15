from flask_restful import Resource
from api.bo.comuneBo import ComuneBo

class Comune(Resource):
    def __init__(self):
        self.comune = ComuneBo()

    def get(self, parameter=""):
        return self.comune.get_all()

    def put(self, parameter):
        pass

    def post(self):
        pass
    