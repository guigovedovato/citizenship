import core.common.utils as utils
import json

class BaseBo:
    def __init__(self, context):
        self.context = context

    def get_all(self):
        return json.loads(self.context.get_all())

    def get_by_id(self, entity_id):
        return json.loads(self.context.get_by_id(entity_id))

    def get_by_filter(self, filters, likes):
        query = utils.fieldBlank(filters)
        if not query:
            return self.get_all()
        else:
            for like in likes:
                utils.like(query, like)
            utils.dates(query)
            return json.loads(self.context.get_by_filter(query))
    
    def update(self, entity_id, entity_newer):
        utils.fromOnToBoolean(entity_newer)
        entity_updated = utils.fieldBlank(entity_newer)
        return json.loads(self.context.update(entity_id, entity_updated))

    def insert(self, entity):
        utils.fromOnToBoolean(entity)
        entity_newer = utils.fieldBlank(entity)
        return json.loads(self.context.insert(entity_newer))