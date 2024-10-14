from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout
from qfluentwidgets import LineEdit, PushButton

class CreateDocumentPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Document")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        self.title_input = LineEdit()
        self.title_input.setPlaceholderText("Enter document title")
        layout.addWidget(self.title_input)
        
        button_layout = QHBoxLayout()
        self.create_button = PushButton("Create")
        self.create_button.clicked.connect(self.accept)
        self.cancel_button = PushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

    def get_title(self):
        return self.title_input.text()