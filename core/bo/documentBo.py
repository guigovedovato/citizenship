import json
import core.common.utils as utils
import os

FILES = "c:\\AssessoriaManager\\files"

class DocumentBo():
    def get_document(self, document):
        pass

    def save_document(self, file, entity):
        try:
            directory = os.path.join(FILES, entity["cognome"] + " " + entity["nome"])
            if not os.path.exists(directory):
                os.makedirs(directory)
            file.save(os.path.join(directory, file.filename))
            return True
        except:
            return False