from api.common.validation import Validation

class BaseBo:
    def __init__(self, context):
        self.context = context

    def get_all(self):
        return self.context.get_all()

    def get_by_id(self, entity_id):
        pass

    def get_by_filter(self, filters):
        pass

    def update(self, entity):
        pass