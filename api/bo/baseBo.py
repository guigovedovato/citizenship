from api.common.validation import Validation
from api.common.parse import Parse

class BaseBo:
    def __init__(self, context):
        self.context = context
        self.parse = Parse()

    def get_all(self):
        return self.context.get_all()

    def get_by_id(self, entity_id):
        return self.context.get_by_id(entity_id)

    def get_by_filter(self, filters):
        return self.context.get_by_filter(filters)
