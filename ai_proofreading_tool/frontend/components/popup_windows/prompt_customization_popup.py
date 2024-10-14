from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QScrollArea, 
                               QWidget, QPushButton, QLineEdit, QLabel)
from PySide6.QtCore import Qt
from qfluentwidgets import ScrollArea, ExpandLayout, PushButton, LineEdit, 
                            InfoBar, InfoBarPosition

class PromptCustomizationPopup(QDialog):
    def __init__(self, prompt_factory, parent=None):
        super().__init__(parent)
        self.prompt_factory = prompt_factory
        self.setWindowTitle("Customize Prompts")
        self.setMinimumSize(800, 600)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)

        # Left Panel (Categories and Buttons)
        left_scroll = ScrollArea()
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        categories = self.prompt_factory.get_prompt_categories()

        for category, buttons in categories.items():
            category_label = QLabel(category)
            left_layout.addWidget(category_label)
            for button_text in buttons:
                button = QPushButton(button_text)
                button.clicked.connect(lambda checked, text=button_text: self.toggle_prompt(text))
                left_layout.addWidget(button)
            left_layout.addSpacing(10)

        left_scroll.setWidget(left_widget)
        left_scroll.setWidgetResizable(True)
        layout.addWidget(left_scroll)

        # Right Panel (Selected Prompts)
        right_scroll = ScrollArea()
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout(self.right_widget)
        
        self.right_layout.addWidget(QLabel("Selected Prompts"))
        
        # Add Custom Prompt section
        custom_prompt_layout = QHBoxLayout()
        self.custom_prompt_label = LineEdit()
        self.custom_prompt_label.setPlaceholderText("Label (max 10 chars)")
        custom_prompt_layout.addWidget(self.custom_prompt_label)
        
        add_custom_button = PushButton("+ Add Custom Prompt")
        add_custom_button.clicked.connect(self.add_custom_prompt)
        custom_prompt_layout.addWidget(add_custom_button)
        
        self.right_layout.addLayout(custom_prompt_layout)
        
        # Save Button
        save_button = PushButton("Save")
        save_button.clicked.connect(self.save_prompts)
        self.right_layout.addWidget(save_button)

        right_scroll.setWidget(self.right_widget)
        right_scroll.setWidgetResizable(True)
        layout.addWidget(right_scroll)

    def toggle_prompt(self, prompt_name):
        # Check if prompt already exists in right panel
        for i in range(self.right_layout.count()):
            item = self.right_layout.itemAt(i)
            if item and item.widget():
                if isinstance(item.widget(), QLabel) and item.widget().text() == prompt_name:
                    # Remove if exists
                    self.right_layout.removeItem(item)
                    item.widget().deleteLater()
                    return

        # Add if doesn't exist
        prompt_layout = QHBoxLayout()
        prompt_label = QLabel(prompt_name)
        prompt_edit = LineEdit()
        prompt_edit.setText(self.prompt_factory.get_prompt(prompt_name))
        delete_button = QPushButton("🗑️")
        delete_button.clicked.connect(lambda: self.remove_prompt(prompt_layout))

        prompt_layout.addWidget(prompt_label)
        prompt_layout.addWidget(prompt_edit)
        prompt_layout.addWidget(delete_button)

        self.right_layout.insertLayout(self.right_layout.count() - 2, prompt_layout)

    def remove_prompt(self, layout):
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().deleteLater()
        self.right_layout.removeItem(layout)

    def add_custom_prompt(self):
        label = self.custom_prompt_label.text()[:10]  # Limit to 10 chars
        if label:
            self.toggle_prompt(label)
            self.custom_prompt_label.clear()

    def save_prompts(self):
        for i in range(self.right_layout.count()):
            item = self.right_layout.itemAt(i)
            if isinstance(item, QHBoxLayout):
                label = item.itemAt(0).widget().text()
                content = item.itemAt(1).widget().text()
                self.prompt_factory.save_user_prompt(label, content)
        self.accept()