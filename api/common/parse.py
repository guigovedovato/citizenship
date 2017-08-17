import json

class Parse:
    def parse_comune(self, entity, entity_newer):
        entity["title"] = entity["title"] if entity_newer["title"] == "" else entity_newer["title"]
        entity["description"] = entity["description"] if entity_newer["description"] == "" else entity_newer["description"]
        entity["done"] = entity["done"] if entity_newer["done"] == "" else entity_newer["done"]
        return entity

    def parse_cliente(self, entity, entity_newer):
        entity["title"] = entity["title"] if entity_newer["title"] == "" else entity_newer["title"]
        entity["description"] = entity["description"] if entity_newer["description"] == "" else entity_newer["description"]
        entity["done"] = entity["done"] if entity_newer["done"] == "" else entity_newer["done"]
        return entity

    def parse_prospecto(self, entity, entity_newer):
        entity["title"] = entity["title"] if entity_newer["title"] == "" else entity_newer["title"]
        entity["description"] = entity["description"] if entity_newer["description"] == "" else entity_newer["description"]
        entity["done"] = entity["done"] if entity_newer["done"] == "" else entity_newer["done"]
        return entity

    def parse_residencia(self, entity, entity_newer):
        entity["title"] = entity["title"] if entity_newer["title"] == "" else entity_newer["title"]
        entity["description"] = entity["description"] if entity_newer["description"] == "" else entity_newer["description"]
        entity["done"] = entity["done"] if entity_newer["done"] == "" else entity_newer["done"]
        return entity