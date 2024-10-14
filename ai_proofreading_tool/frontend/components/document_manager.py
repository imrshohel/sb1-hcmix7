from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from qfluentwidgets import (ListWidget, PushButton, LineEdit, InfoBar,
                            InfoBarPosition, MessageBox)
from ai_proofreading_tool.backend.document_service import DocumentService
from .buttons.action_buttons import NewDocumentButton, DeleteDocumentButton, UploadDocumentButton
from .popup_windows.create_document_popup import CreateDocumentPopup

class DocumentManager(QWidget):
    def __init__(self):
        super().__init__()
        self.document_service = DocumentService()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Document list
        self.document_list = ListWidget()
        self.refresh_document_list()
        layout.addWidget(self.document_list)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.new_doc_button = NewDocumentButton()
        self.new_doc_button.clicked.connect(self.create_new_document)
        self.delete_doc_button = DeleteDocumentButton()
        self.delete_doc_button.clicked.connect(self.delete_document)
        self.upload_doc_button = UploadDocumentButton()
        self.upload_doc_button.clicked.connect(self.upload_document)
        
        button_layout.addWidget(self.new_doc_button)
        button_layout.addWidget(self.delete_doc_button)
        button_layout.addWidget(self.upload_doc_button)
        layout.addLayout(button_layout)

    def refresh_document_list(self):
        self.document_list.clear()
        documents = self.document_service.get_all_documents()
        for doc in documents:
            self.document_list.addItem(doc.title)

    def create_new_document(self):
        popup = CreateDocumentPopup(self)
        if popup.exec():
            title = popup.get_title()
            if title:
                self.document_service.create_document(title)
                self.refresh_document_list()
                InfoBar.success(
                    title='Success',
                    content=f"Document '{title}' created successfully",
                    orient=InfoBarPosition.TOP,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=2000,
                    parent=self
                )

    def delete_document(self):
        current_item = self.document_list.currentItem()
        if current_item:
            title = current_item.text()
            confirm = MessageBox(
                'Confirm Deletion',
                f'Are you sure you want to delete "{title}"?',
                self
            )
            if confirm.exec():
                self.document_service.delete_document(title)
                self.refresh_document_list()
                InfoBar.success(
                    title='Success',
                    content=f"Document '{title}' deleted successfully",
                    orient=InfoBarPosition.TOP,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=2000,
                    parent=self
                )
        else:
            InfoBar.warning(
                title='Warning',
                content="Please select a document to delete",
                orient=InfoBarPosition.TOP,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )

    def upload_document(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt);;Word documents (*.docx)")
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                file_name = os.path.basename(file_path)
                self.document_service.upload_document(file_path)
                self.refresh_document_list()
                InfoBar.success(
                    title='Success',
                    content=f"Document '{file_name}' uploaded successfully",
                    orient=InfoBarPosition.TOP,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=2000,
                    parent=self
                )