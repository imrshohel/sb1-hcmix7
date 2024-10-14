from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import TextEdit, PushButton, InfoBar, InfoBarPosition
from ai_proofreading_tool.backend.document_service import DocumentService

class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.document_service = DocumentService()
        self.current_document_id = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        self.editor = TextEdit()
        layout.addWidget(self.editor)
        
        button_layout = QHBoxLayout()
        self.save_button = PushButton('Save')
        self.save_button.clicked.connect(self.save_document)
        button_layout.addWidget(self.save_button)
        
        layout.addLayout(button_layout)

    def load_document(self, document_id):
        self.current_document_id = document_id
        document = self.document_service.get_document(document_id)
        if document:
            self.editor.setPlainText(document.content)

    def save_document(self):
        if self.current_document_id:
            content = self.editor.toPlainText()
            self.document_service.update_document(self.current_document_id, content)
            InfoBar.success(
                title='Success',
                content="Document saved successfully",
                orient=InfoBarPosition.TOP,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        else:
            InfoBar.warning(
                title='Warning',
                content="No document is currently open",
                orient=InfoBarPosition.TOP,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )