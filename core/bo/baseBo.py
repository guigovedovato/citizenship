import core.common.utils as utils
import json

class BaseBo:
    def __init__(self, context):
        self.context = context

    def get_all(self):
        return json.loads(self.context.get_all())

    def get_by_id(self, entity_id):
        return json.loads(self.context.get_by_id(entity_id))

    def get_by_filter(self, filters, likes, gtes):
        query = utils.fieldBlank(filters)
        if not query:
            return self.get_all()
        else:
            for like in likes:
                utils.like(query, like)
            for gte in gtes:
                utils.gte(query, gte)
            utils.dates(query)
            return json.loads(self.context.get_by_filter(query))
    
    def update(self, entity_id, entity):
        entity = utils.fieldBlank(entity)
        utils.fromOnToBoolean(entity)
        return json.loads(self.context.update(entity_id, entity))

    def insert(self, entity):
        entity = utils.fieldBlank(entity)
        utils.fromOnToBoolean(entity)
        return json.loads(self.context.insert(entity))
    
    def find_fields_byID(self, entity_id, fields):
        return json.loads(self.context.find_fields_byID(entity_id, fields))

    def find_fields(self, fields):
        fields = {k:1 for k in fields }
        fields.update({'_id':0})
        return json.loads(self.context.find_fields(fields))