from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from qfluentwidgets import ComboBox, PushButton, LineEdit, InfoBar, InfoBarPosition
from ai_proofreading_tool.utils.prompt_factory import PromptFactory
from ai_proofreading_tool.backend.user_service import UserService
from ai_proofreading_tool.utils.license_manager import LicenseManager
from .popup_windows.prompt_customization_popup import PromptCustomizationPopup

class SettingsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.prompt_factory = PromptFactory()
        self.user_service = UserService()
        self.license_manager = LicenseManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # AI Service settings
        ai_service_layout = QHBoxLayout()
        ai_service_layout.addWidget(QLabel("AI Service:"))
        self.ai_service_combo = ComboBox()
        self.ai_service_combo.addItems(['OpenAI', 'Claude AI', 'Google AI', 'Groq', 'Ollama'])
        self.ai_service_combo.currentIndexChanged.connect(self.update_ai_service)
        ai_service_layout.addWidget(self.ai_service_combo)
        layout.addLayout(ai_service_layout)
        
        # API Key settings
        api_key_layout = QHBoxLayout()
        api_key_layout.addWidget(QLabel("API Key:"))
        self.api_key_input = LineEdit()
        self.api_key_input.setPlaceholderText('Enter API Key')
        api_key_layout.addWidget(self.api_key_input)
        self.save_api_key_button = PushButton('Save API Key')
        self.save_api_key_button.clicked.connect(self.save_api_key)
        api_key_layout.addWidget(self.save_api_key_button)
        layout.addLayout(api_key_layout)
        
        # Prompt Customization Button
        self.customize_prompts_button = PushButton('Customize Prompts')
        self.customize_prompts_button.clicked.connect(self.open_prompt_customization)
        layout.addWidget(self.customize_prompts_button)
        
        # License settings
        license_layout = QHBoxLayout()
        license_layout.addWidget(QLabel("License Key:"))
        self.license_key_input = LineEdit()
        self.license_key_input.setPlaceholderText('Enter License Key')
        license_layout.addWidget(self.license_key_input)
        self.activate_license_button = PushButton('Activate License')
        self.activate_license_button.clicked.connect(self.activate_license)
        license_layout.addWidget(self.activate_license_button)
        self.deactivate_license_button = PushButton('Deactivate License')
        self.deactivate_license_button.clicked.connect(self.deactivate_license)
        license_layout.addWidget(self.deactivate_license_button)
        layout.addLayout(license_layout)

    def update_ai_service(self):
        selected_service = self.ai_service_combo.currentText()
        self.user_service.update_ai_service(selected_service)

    def save_api_key(self):
        api_key = self.api_key_input.text()
        self.user_service.save_api_key(api_key)
        InfoBar.success(
            title='Success',
            content="API Key saved successfully",
            orient=InfoBarPosition.BOTTOM,
            parent=self
        )

    def open_prompt_customization(self):
        popup = PromptCustomizationPopup(self.prompt_factory, self)
        if popup.exec():
            InfoBar.success(
                title='Success',
                content="Prompts customized successfully",
                orient=InfoBarPosition.BOTTOM,
                parent=self
            )

    def activate_license(self):
        license_key = self.license_key_input.text()
        if self.license_manager.validate_license(license_key):
            InfoBar.success(
                title='Success',
                content="License activated successfully",
                orient=InfoBarPosition.BOTTOM,
                parent=self
            )
        else:
            InfoBar.error(
                title='Error',
                content="Invalid license key or already in use",
                orient=InfoBarPosition.BOTTOM,
                parent=self
            )

    def deactivate_license(self):
        license_key = self.license_key_input.text()
        if self.license_manager.deactivate_license(license_key):
            InfoBar.success(
                title='Success',
                content="License deactivated successfully",
                orient=InfoBarPosition.BOTTOM,
                parent=self
            )
        else:
            InfoBar.error(
                title='Error',
                content="Failed to deactivate license",
                orient=InfoBarPosition.BOTTOM,
                parent=self
            )