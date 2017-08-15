from flask_restful import Resource
from api.bo.prospectoBo import ProspectoBo

class Prospecto(Resource):
    def __init__(self):
        self.prospecto = ProspectoBo()

    def get(self, parameter=""):
        return self.prospecto.get_all()

    def put(self, parameter):
        pass

    def post(self):
        pass
