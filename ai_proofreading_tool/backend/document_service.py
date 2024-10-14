from ai_proofreading_tool.database.document_model import DocumentModel

class DocumentService:
    def __init__(self):
        self.document_model = DocumentModel()

    def get_all_documents(self):
        return self.document_model.get_all_documents()

    def get_document(self, document_id):
        return self.document_model.get_document(document_id)

    def create_document(self, title, content=""):
        return self.document_model.create_document(title, content)

    def update_document(self, document_id, content):
        return self.document_model.update_document(document_id, content)

    def delete_document(self, document_id):
        return self.document_model.delete_document(document_id)