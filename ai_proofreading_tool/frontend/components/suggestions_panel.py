from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import ListWidget, PushButton, InfoBar, InfoBarPosition
from ai_proofreading_tool.backend.suggestion_service import SuggestionService

class SuggestionsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.suggestion_service = SuggestionService()
        self.current_document_id = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        self.suggestions_list = ListWidget()
        layout.addWidget(self.suggestions_list)
        
        button_layout = QHBoxLayout()
        self.refresh_button = PushButton('Refresh Suggestions')
        self.refresh_button.clicked.connect(self.refresh_suggestions)
        button_layout.addWidget(self.refresh_button)
        
        self.apply_button = PushButton('Apply Selected Suggestion')
        self.apply_button.clicked.connect(self.apply_suggestion)
        button_layout.addWidget(self.apply_button)
        
        layout.addLayout(button_layout)

    def set_current_document(self, document_id):
        self.current_document_id = document_id
        self.refresh_suggestions()

    def refresh_suggestions(self):
        if self.current_document_id:
            self.suggestions_list.clear()
            suggestions = self.suggestion_service.get_suggestions(self.current_document_id)
            for suggestion in suggestions:
                self.suggestions_list.addItem(suggestion)
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

    def apply_suggestion(self):
        selected_item = self.suggestions_list.currentItem()
        if selected_item and self.current_document_id:
            suggestion = selected_item.text()
            self.suggestion_service.apply_suggestion(self.current_document_id, suggestion)
            InfoBar.success(
                title='Success',
                content="Suggestion applied successfully",
                orient=InfoBarPosition.TOP,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        else:
            InfoBar.warning(
                title='Warning',
                content="Please select a suggestion to apply",
                orient=InfoBarPosition.TOP,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )