from api import api
from api.clienteApi import Cliente
from api.prospectoApi import Prospecto
from api.comuneApi import Comune
from api.residenciaApi import Residencia

api.add_resource(Cliente, '/api/cliente', endpoint = 'clientes')
api.add_resource(Cliente, '/api/cliente/<parameter>', endpoint = 'cliente')

api.add_resource(Prospecto, '/api/prospecto', endpoint = 'prospectos')
api.add_resource(Prospecto, '/api/prospecto/<parameter>', endpoint = 'prospecto')

api.add_resource(Comune, '/api/comune', endpoint = 'comunes')
api.add_resource(Comune, '/api/comune/<parameter>', endpoint = 'comune')

api.add_resource(Residencia, '/api/residencia', endpoint = 'residencias')
api.add_resource(Residencia, '/api/residencia/<parameter>', endpoint = 'residencia')