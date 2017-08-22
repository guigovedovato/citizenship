import core.common.utils as utils
import json

class BaseBo:
    def __init__(self, context):
        self.context = context

    def get_all(self):
        return json.loads(self.context.get_all())

    def get_by_id(self, entity_id):
        return json.loads(self.context.get_by_id(entity_id))

    def get_by_filter(self, filters):
        query = utils.intersection(filters)
        if not query:
            return self.get_all()
        else:
            return json.loads(self.context.get_by_filter(query))
    
    def update(self, entity_id, entity_newer):
        entity_updated = utils.intersection(entity_newer)
        return json.loads(self.context.update(entity_id, entity_updated))

    def insert(self, entity):
        return json.loads(self.context.insert(entity))