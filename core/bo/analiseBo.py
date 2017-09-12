from core.bo.baseBo import BaseBo
from core.dao.analiseDao import AnaliseDao
import json
import core.common.utils as utils

class AnaliseBo(BaseBo):
    def __init__(self):
        super().__init__(AnaliseDao())

    def do_analise(self, entity):
        entity_response = {}
        self.analise_name(entity, entity_response)
        self.analise_conjuge(entity, entity_response)
        self.analise_date(entity, entity_response)
        return entity_response

    def analise_date(self, entity, entity_response):
        # Pai/Mãe
        if entity.get("casamento_paimae_idade"):
            date = utils.get_age(entity["nascimento_paimae_data"], entity["casamento_paimae_data"])
            if int(entity["casamento_paimae_idade"]) != date:
                entity_response.update({"casamento_paimae_data": entity["casamento_paimae_data"]})
        if entity.get("obito_paimae_idade"):
            date = utils.get_age(entity["nascimento_paimae_data"], entity["obito_paimae_data"])
            if int(entity["obito_paimae_idade"]) != date:
                entity_response.update({"obito_paimae_data": entity["obito_paimae_data"]})
        if entity.get("nascimento_paimae_requerente_idade"):
            date = utils.get_age(entity["nascimento_paimae_data"], entity["nascimento_requerente_data"])
            if int(entity["nascimento_paimae_requerente_idade"]) != date:
                entity_response.update({"nascimento_paimae_requerente_idade": entity["nascimento_paimae_requerente_idade"]})
        if entity.get("casamento_paimae_requerente_idade"):
            date = utils.get_age(entity["nascimento_paimae_data"], entity["casamento_requerente_data"])
            if int(entity["casamento_paimae_requerente_idade"]) != date:
                entity_response.update({"casamento_paimae_requerente_idade": entity["casamento_paimae_requerente_idade"]})
        # Avô/Avó
        if entity.get("casamento_avo_idade"):
            date = utils.get_age(entity["nascimento_avo_data"], entity["casamento_avo_data"])
            if int(entity["casamento_avo_idade"]) != date:
                entity_response.update({"casamento_avo_data": entity["casamento_avo_data"]})
        if entity.get("obito_avo_idade"):
            date = utils.get_age(entity["nascimento_avo_data"], entity["obito_avo_data"])
            if int(entity["obito_avo_idade"]) != date:
                entity_response.update({"obito_avo_data": entity["obito_avo_data"]})
        if entity.get("nascimento_avo_paimae_idade"):
            date = utils.get_age(entity["nascimento_avo_data"], entity["nascimento_paimae_data"])
            if int(entity["nascimento_avo_paimae_idade"]) != date:
                entity_response.update({"nascimento_avo_paimae_idade": entity["nascimento_avo_paimae_idade"]})
        if entity.get("casamento_avo_paimae_idade"):
            date = utils.get_age(entity["nascimento_avo_data"], entity["casamento_paimae_data"])
            if int(entity["casamento_avo_paimae_idade"]) != date:
                entity_response.update({"casamento_avo_paimae_idade": entity["casamento_avo_paimae_idade"]})
        if entity.get("nascimento_avo_requerente_idade"):
            date = utils.get_age(entity["nascimento_avo_data"], entity["nascimento_requerente_data"])
            if int(entity["nascimento_avo_requerente_idade"]) != date:
                entity_response.update({"nascimento_avo_requerente_idade": entity["nascimento_avo_requerente_idade"]})
        # Bisavô/Bisavó
        if entity.get("casamento_bisavo_idade"):
            date = utils.get_age(entity["nascimento_bisavo_data"], entity["casamento_bisavo_data"])
            if int(entity["casamento_bisavo_idade"]) != date:
                entity_response.update({"casamento_bisavo_data": entity["casamento_bisavo_data"]})
        if entity.get("obito_bisavo_idade"):
            date = utils.get_age(entity["nascimento_bisavo_data"], entity["obito_bisavo_data"])
            if int(entity["obito_bisavo_idade"]) != date:
                entity_response.update({"obito_bisavo_data": entity["obito_bisavo_data"]})
        if entity.get("nascimento_bisavo_avo_idade"):
            date = utils.get_age(entity["nascimento_bisavo_data"], entity["nascimento_avo_data"])
            if int(entity["nascimento_bisavo_avo_idade"]) != date:
                entity_response.update({"nascimento_bisavo_avo_idade": entity["nascimento_bisavo_avo_idade"]})
        if entity.get("casamento_bisavo_avo_idade"):
            date = utils.get_age(entity["nascimento_bisavo_data"], entity["casamento_avo_data"])
            if int(entity["casamento_bisavo_avo_idade"]) != date:
                entity_response.update({"casamento_bisavo_avo_idade": entity["casamento_bisavo_avo_idade"]})
        if entity.get("nascimento_bisavo_paimae_idade"):
            date = utils.get_age(entity["nascimento_bisavo_data"], entity["nascimento_paimae_data"])
            if int(entity["nascimento_bisavo_paimae_idade"]) != date:
                entity_response.update({"nascimento_bisavo_paimae_idade": entity["nascimento_bisavo_paimae_idade"]})
        # Trisavô/Trisavó
        if entity.get("casamento_trisavo_idade"):
            date = utils.get_age(entity["nascimento_trisavo_data"], entity["casamento_trisavo_data"])
            if int(entity["casamento_trisavo_idade"]) != date:
                entity_response.update({"casamento_trisavo_data": entity["casamento_trisavo_data"]})
        if entity.get("obito_trisavo_idade"):
            date = utils.get_age(entity["nascimento_trisavo_data"], entity["obito_trisavo_data"])
            if int(entity["obito_trisavo_idade"]) != date:
                entity_response.update({"obito_trisavo_data": entity["obito_trisavo_data"]})
        if entity.get("nascimento_trisavo_bisavo_idade"):
            date = utils.get_age(entity["nascimento_trisavo_data"], entity["nascimento_bisavo_data"])
            if int(entity["nascimento_trisavo_bisavo_idade"]) != date:
                entity_response.update({"nascimento_trisavo_bisavo_idade": entity["nascimento_trisavo_bisavo_idade"]})
        if entity.get("casamento_trisavo_bisavo_idade"):
            date = utils.get_age(entity["nascimento_trisavo_data"], entity["casamento_bisavo_data"])
            if int(entity["casamento_trisavo_bisavo_idade"]) != date:
                entity_response.update({"casamento_trisavo_bisavo_idade": entity["casamento_trisavo_bisavo_idade"]})
        if entity.get("nascimento_trisavo_avo_idade"):
            date = utils.get_age(entity["nascimento_trisavo_data"], entity["nascimento_avo_data"])
            if int(entity["nascimento_trisavo_avo_idade"]) != date:
                entity_response.update({"nascimento_trisavo_avo_idade": entity["nascimento_trisavo_avo_idade"]})

    def analise_conjuge(self, entity, entity_response):
        # Pai/Mãe
        if entity.get("casamento_paimae_conjuge"):
            if entity.get("obito_paimae_conjuge"):
                if entity["casamento_paimae_conjuge"] != entity["obito_paimae_conjuge"]:
                    entity_response.update({"obito_paimae_conjuge": entity["obito_paimae_conjuge"]})
            if entity.get("nascimento_paimae_requerente_conjuge"):
                if entity["casamento_paimae_conjuge"] != entity["nascimento_paimae_requerente_conjuge"]:
                    entity_response.update({"nascimento_paimae_requerente_conjuge": entity["nascimento_paimae_requerente_conjuge"]})
            if entity.get("casamento_paimae_requerente_conjuge"):
                if entity["casamento_paimae_conjuge"] != entity["casamento_paimae_requerente_conjuge"]:
                    entity_response.update({"casamento_paimae_requerente_conjuge": entity["casamento_paimae_requerente_conjuge"]})
        # Avô/Avó
        if entity.get("casamento_avo_conjuge"):
            if entity.get("obito_avo_conjuge"):
                if entity["casamento_avo_conjuge"] != entity["obito_avo_conjuge"]:
                    entity_response.update({"obito_avo_conjuge": entity["obito_avo_conjuge"]})
            if entity.get("nascimento_avo_paimae_conjuge"):
                if entity["casamento_avo_conjuge"] != entity["nascimento_avo_paimae_conjuge"]:
                    entity_response.update({"nascimento_avo_paimae_conjuge": entity["nascimento_avo_paimae_conjuge"]})
            if entity.get("casamento_avo_paimae_conjuge"):
                if entity["casamento_avo_conjuge"] != entity["casamento_avo_paimae_conjuge"]:
                    entity_response.update({"casamento_avo_paimae_conjuge": entity["casamento_avo_paimae_conjuge"]})
            if entity.get("nascimento_avo_requerente_conjuge"):
                if entity["casamento_avo_conjuge"] != entity["nascimento_avo_requerente_conjuge"]:
                    entity_response.update({"nascimento_avo_requerente_conjuge": entity["nascimento_avo_requerente_conjuge"]})
        # Bisavô/Bisavó
        if entity.get("casamento_bisavo_conjuge"):
            if entity.get("obito_bisavo_conjuge"):
                if entity["casamento_bisavo_conjuge"] != entity["obito_bisavo_conjuge"]:
                    entity_response.update({"obito_bisavo_conjuge": entity["obito_bisavo_conjuge"]})
            if entity.get("nascimento_bisavo_avo_conjuge"):
                if entity["casamento_bisavo_conjuge"] != entity["nascimento_bisavo_avo_conjuge"]:
                    entity_response.update({"nascimento_bisavo_avo_conjuge": entity["nascimento_bisavo_avo_conjuge"]})
            if entity.get("casamento_bisavo_avo_conjuge"):
                if entity["casamento_bisavo_conjuge"] != entity["casamento_bisavo_avo_conjuge"]:
                    entity_response.update({"casamento_bisavo_avo_conjuge": entity["casamento_bisavo_avo_conjuge"]})
            if entity.get("nascimento_bisavo_paimae_conjuge"):
                if entity["casamento_bisavo_conjuge"] != entity["nascimento_bisavo_paimae_conjuge"]:
                    entity_response.update({"nascimento_bisavo_paimae_conjuge": entity["nascimento_bisavo_paimae_conjuge"]})
        # Trisavô/Trisavó
        if entity.get("casamento_trisavo_conjuge"):
            if entity.get("obito_trisavo_conjuge"):
                if entity["casamento_trisavo_conjuge"] != entity["obito_trisavo_conjuge"]:
                    entity_response.update({"obito_trisavo_conjuge": entity["obito_trisavo_conjuge"]})
            if entity.get("nascimento_trisavo_bisavo_conjuge"):
                if entity["casamento_trisavo_conjuge"] != entity["nascimento_trisavo_bisavo_conjuge"]:
                    entity_response.update({"nascimento_trisavo_bisavo_conjuge": entity["nascimento_trisavo_bisavo_conjuge"]})
            if entity.get("casamento_trisavo_bisavo_conjuge"):
                if entity["casamento_trisavo_conjuge"] != entity["casamento_trisavo_bisavo_conjuge"]:
                    entity_response.update({"casamento_trisavo_bisavo_conjuge": entity["casamento_trisavo_bisavo_conjuge"]})
            if entity.get("nascimento_trisavo_avo_conjuge"):
                if entity["casamento_trisavo_conjuge"] != entity["nascimento_trisavo_avo_conjuge"]:
                    entity_response.update({"nascimento_trisavo_avo_conjuge": entity["nascimento_trisavo_avo_conjuge"]})

    def analise_name(self, entity, entity_response):
        # Pai/Mãe
        if entity["nascimento_paimae_nome"] != entity["nascimento_paimae_requerente_nome"]:
            entity_response.update({"nascimento_paimae_requerente_nome": entity["nascimento_paimae_requerente_nome"]})
        if entity.get("casamento_paimae_requerente_nome"):
            if entity["casamento_paimae_nome"] != entity["casamento_paimae_requerente_nome"]:
                entity_response.update({"casamento_paimae_requerente_nome": entity["casamento_paimae_requerente_nome"]})
        if entity.get("obito_paimae_nome"):
            if entity["casamento_paimae_nome"] != entity["obito_paimae_nome"]:
                entity_response.update({"obito_paimae_nome": entity["obito_paimae_nome"]})
        # Avô/Avó
        if entity["nascimento_avo_nome"] != entity["nascimento_avo_paimae_nome"]:
            entity_response.update({"nascimento_avo_paimae_nome": entity["nascimento_avo_paimae_nome"]})
        if entity["nascimento_avo_nome"] != entity["nascimento_avo_requerente_nome"]:
            entity_response.update({"nascimento_avo_requerente_nome": entity["nascimento_avo_requerente_nome"]})
        if entity["casamento_avo_nome"] != entity["casamento_avo_paimae_nome"]:
            entity_response.update({"casamento_avo_paimae_nome": entity["casamento_avo_paimae_nome"]})
        if entity.get("obito_avo_nome"):
            if entity["casamento_avo_nome"] != entity["obito_avo_nome"]:
                entity_response.update({"obito_avo_nome": entity["obito_avo_nome"]})
        # Bisavô/Bisavó
        if entity.get("nascimento_bisavo_nome"):
            if entity["nascimento_bisavo_nome"] != entity["nascimento_bisavo_avo_nome"]:
                entity_response.update({"nascimento_bisavo_avo_nome": entity["nascimento_bisavo_avo_nome"]})
            if entity["nascimento_bisavo_nome"] != entity["nascimento_bisavo_paimae_nome"]:
                entity_response.update({"nascimento_bisavo_paimae_nome": entity["nascimento_bisavo_paimae_nome"]})
        if entity.get("casamento_bisavo_nome"):
            if entity["casamento_bisavo_nome"] != entity["casamento_bisavo_avo_nome"]:
                entity_response.update({"casamento_bisavo_avo_nome": entity["casamento_bisavo_avo_nome"]})
        if entity.get("obito_bisavo_nome"):
            if entity["casamento_bisavo_nome"] != entity["obito_bisavo_nome"]:
                entity_response.update({"obito_bisavo_nome": entity["obito_bisavo_nome"]})
        # Trisavô/Trisavó
        if entity.get("nascimento_trisavo_nome"):
            if entity["nascimento_trisavo_nome"] != entity["nascimento_trisavo_bisavo_nome"]:
                entity_response.update({"nascimento_trisavo_bisavo_nome": entity["nascimento_trisavo_bisavo_nome"]})
            if entity["nascimento_trisavo_nome"] != entity["nascimento_trisavo_avo_nome"]:
                entity_response.update({"nascimento_trisavo_avo_nome": entity["nascimento_trisavo_avo_nome"]})
        if entity.get("casamento_trisavo_nome"):
            if entity["casamento_trisavo_nome"] != entity["casamento_trisavo_bisavo_nome"]:
                entity_response.update({"casamento_trisavo_bisavo_nome": entity["casamento_trisavo_bisavo_nome"]})
        if entity.get("obito_trisavo_nome"):
            if entity["casamento_trisavo_nome"] != entity["obito_trisavo_nome"]:
                entity_response.update({"obito_trisavo_nome": entity["obito_trisavo_nome"]})

    def get_name_by_prospecto(self, entity):
        if utils.is_number(entity):
            return []
        return json.loads(self.context.get_name_by_prospecto(entity))

    def get_by_prospecto(self, entity):
        return json.loads(self.context.get_by_prospecto(entity))

    def insert(self, entity):
        analise_inserted = super().insert(entity)
        analise_inserted.pop("_id")
        analise_inserted.pop("prospecto")
        analise_inserted.pop("ativo")
        analise_inserted.pop("data_cadastro")
        if analise_inserted.get("data_atualizacao"):
            analise_inserted.pop("data_atualizacao")
        return self.do_analise(analise_inserted)

    def update(self, entity_id, entity):
        analise_updated = super().update(entity_id, entity)
        analise_updated.pop("_id")
        analise_updated.pop("prospecto")
        analise_updated.pop("ativo")
        analise_updated.pop("data_cadastro")
        analise_updated.pop("data_atualizacao")
        return self.do_analise(analise_updated)

    def find_fields_by_id(self, entity_id, fields):
        return super().find_fields_by_id(entity_id, {"_id":0,"prospecto":0,"ativo":0,"data_cadastro":0,"data_atualizacao":0})
    