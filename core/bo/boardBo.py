from core.bo.baseBo import BaseBo
from core.dao.clienteDao import ClienteDao
import json
import core.common.utils as utils
from datetime import datetime, timedelta

class BoardBo(BaseBo):
    def __init__(self):
        super().__init__(ClienteDao())

    def get_recepcao(self):
        recepcao = []
        end_date = (datetime.now().date() + timedelta(days=6))
        clientes = self.search({"chegada":{"$lte":str(end_date)+"T00:00", "$ne":""}, "data_entrada_processo":""}, 
                          {"cognome":1, "nome":1, "chegada":1, "aeroporto":1, "_id":0},
                          "chegada")
        for cliente in clientes:
            data, hora = cliente["chegada"].split("T")
            if utils.convert_date(data).date() < datetime.now().date():
                recepcao.append(self.set_recepcao(cliente, data, hora, "-1"))
            else:
                recepcao.append(self.set_recepcao(cliente, data, hora, self.get_expiration_date(utils.convert_date(data).date(), datetime.now().date())))
        return recepcao

    def get_residencia(self):
        residencia = []
        start_date = (datetime.now().date() - timedelta(days=45))
        end_date = (start_date + timedelta(days=5))
        clientes = self.search({"data_entrada_processo":{'$lte':str(end_date), '$ne':""}, "data_entrada_nr":""}, 
                          {"cognome":1, "nome":1, "data_entrada_processo":1, "comune":1, "_id":0},
                          "data_entrada_processo")
        for cliente in clientes:
            data = utils.convert_date(cliente["data_entrada_processo"]).date()
            if data < start_date:
                residencia.append(self.set_residencia_nr(cliente, cliente["data_entrada_processo"], "-1", 45))
            else:
                residencia.append(self.set_residencia_nr(cliente, cliente["data_entrada_processo"], self.get_expiration_date(utils.convert_date(cliente["data_entrada_processo"]).date(), start_date), 45))
        return residencia

    def get_naoRenuncia(self):
        nao_renuncia = []
        start_date = (datetime.now().date() - timedelta(days=30))
        end_date = (start_date + timedelta(days=5))
        clientes = self.search({"data_entrada_nr":{'$lte':str(end_date), '$ne':""}, "data_entrada_passaporte":""}, 
                          {"cognome":1, "nome":1, "data_entrada_nr":1, "comune":1, "_id":0},
                          "data_entrada_nr")
        for cliente in clientes:
            data = utils.convert_date(cliente["data_entrada_nr"]).date()
            if data < start_date:
                nao_renuncia.append(self.set_residencia_nr(cliente, cliente["data_entrada_nr"], "-1", 30))
            else:
                nao_renuncia.append(self.set_residencia_nr(cliente, cliente["data_entrada_nr"], self.get_expiration_date(utils.convert_date(cliente["data_entrada_nr"]).date(), start_date), 30))
        return nao_renuncia

    def get_passaporte(self):
        passaporte = []
        start_date = (datetime.now().date() - timedelta(days=20))
        end_date = (start_date + timedelta(days=5))
        clientes = self.search({"data_entrada_passaporte":{'$lte':str(end_date), '$ne':""}, "data_chegada_aire":""}, 
                          {"cognome":1, "nome":1, "data_entrada_passaporte":1, "comune":1, "_id":0},
                          "data_entrada_passaporte")
        for cliente in clientes:
            data = utils.convert_date(cliente["data_entrada_passaporte"]).date()
            if data < start_date:
                passaporte.append(self.set_passaporte(cliente, "-1"))
            else:
                passaporte.append(self.set_passaporte(cliente, self.get_expiration_date(utils.convert_date(cliente["data_entrada_passaporte"]).date(), start_date)))
        return passaporte

    def get_board(self):
        recepcao = self.get_recepcao()
        residencia = self.get_residencia()
        nao_renuncia = self.get_naoRenuncia()
        passaporte = self.get_passaporte()
        board = [{"recepcao": recepcao, "residencia": residencia, "naoRenuncia": nao_renuncia, "passaporte":passaporte}]
        return json.loads(json.dumps(board))

    def search(self, query, fields, order):
        query.update({"ativo":"True"})
        return json.loads(self.context.get_by_filter_fields(query, fields, order))
    
    def set_recepcao(self, cliente, data, hora, expiracao):
        return {"cognome":cliente["cognome"], "nome":cliente["nome"], "data":utils.get_data(data), "hora":hora, "aeroporto":cliente["aeroporto"], "expiracao":expiracao}

    def set_residencia_nr(self, cliente, data, expiracao, days):
        final_date = (utils.convert_date(data) + timedelta(days=days))
        return {"cognome":cliente["cognome"], "nome":cliente["nome"], "data":utils.date_convert(final_date), "comune":cliente["comune"], "expiracao":expiracao}

    def set_passaporte(self, cliente, expiracao):
        final_date = (utils.convert_date(cliente["data_entrada_passaporte"]) + timedelta(days=20))
        return {"cognome":cliente["cognome"], "nome":cliente["nome"], "data":utils.date_convert(final_date), "expiracao":expiracao}

    def get_expiration_date(self, end_date, start_date):
        days = (end_date - start_date).days
        return str(days)