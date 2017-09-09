import json
import core.common.utils as utils
import os
from docx import Document

FILES_TO_SAVE = "c:\\AssessoriaManager\\files"

class DocumentBo():
    def get_document(self, file, cliente):
        filename = "contrato.docx" if file == "contrato" else "richiedente.docx"
        documents_directory = os.path.join(os.getcwd(), "documents")
        cliente_directory = utils.create_directory(FILES_TO_SAVE, cliente["cognome"] + " " + cliente["nome"])
        document_to_edit = os.path.join(documents_directory, filename)
        filename_to_download = self.edit_document(document_to_edit, cliente_directory, cliente, file)
        return os.path.join(cliente_directory, filename_to_download)

    def edit_document(self, document_to_edit, cliente_directory, cliente, file):
        if file == "contrato":
            return self.edit_contrato(document_to_edit, cliente_directory, cliente)
        else:
            return self.edit_richiedente(document_to_edit, cliente_directory, cliente)

    def edit_contrato(self, document_to_edit, cliente_directory, cliente):
        document = Document(document_to_edit)
        new_name = "contrato_" + cliente["cognome"] + "_" + cliente["nome"] + ".docx"
        #TODO
        document.save(os.path.join(cliente_directory, new_name))
        return new_name

    def edit_richiedente(self, document_to_edit, cliente_directory, cliente):
        document = Document(document_to_edit)
        new_name = "richiedente_" + cliente["cognome"] + "_" + cliente["nome"] + ".docx"
        #TODO
        document.save(os.path.join(cliente_directory, new_name))
        return new_name

    def save_document(self, file, entity):
        try:
            directory = utils.create_directory(FILES_TO_SAVE, entity["cognome"] + " " + entity["nome"])
            file.save(os.path.join(directory, file.filename))
            return True
        except:
            return False