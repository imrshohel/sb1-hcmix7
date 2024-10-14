from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from qfluentwidgets import (FluentIcon, NavigationInterface, NavigationItemPosition,
                            NavigationWidget, Theme, setTheme)
from ai_proofreading_tool.frontend.components.document_manager import DocumentManager
from ai_proofreading_tool.frontend.components.text_editor import TextEditor
from ai_proofreading_tool.frontend.components.suggestions_panel import SuggestionsPanel
from ai_proofreading_tool.frontend.components.settings_panel import SettingsPanel
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Proofreading Tool")
        self.resize(1200, 800)
        setTheme(Theme.DARK)

        # Load stylesheet
        stylesheet_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'stylesheets', 'main.qss')
        with open(stylesheet_path, 'r') as f:
            self.setStyleSheet(f.read())

        # Set application icon
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'app_icon.png')
        self.setWindowIcon(QIcon(icon_path))

        # Create central widget and main layout
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create and set up the navigation interface
        self.navigationInterface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True)
        main_layout.addWidget(self.navigationInterface)

        # Create stacked widget for main content
        self.stackedWidget = QWidget()
        self.stackedLayout = QStackedLayout(self.stackedWidget)
        main_layout.addWidget(self.stackedWidget)

        # Create components
        self.documentManager = DocumentManager()
        self.textEditor = TextEditor()
        self.suggestionsPanel = SuggestionsPanel()
        self.settingsPanel = SettingsPanel()

        # Add components to stacked layout
        self.stackedLayout.addWidget(self.documentManager)
        self.stackedLayout.addWidget(self.textEditor)
        self.stackedLayout.addWidget(self.suggestionsPanel)
        self.stackedLayout.addWidget(self.settingsPanel)

        # Set up navigation
        self.setupNavigation()

    def setupNavigation(self):
        self.addSubInterface(self.documentManager, 'document', 'Documents', FluentIcon.DOCUMENT)
        self.addSubInterface(self.textEditor, 'edit', 'Editor', FluentIcon.EDIT)
        self.addSubInterface(self.suggestionsPanel, 'suggestions', 'Suggestions', FluentIcon.CHAT)
        self.addSubInterface(self.settingsPanel, 'settings', 'Settings', FluentIcon.SETTING, NavigationItemPosition.BOTTOM)

    def addSubInterface(self, interface, objectName, text, icon, position=NavigationItemPosition.TOP):
        self.navigationInterface.addItem(
            routeKey=objectName,
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position
        )

    def switchTo(self, widget):
        self.stackedLayout.setCurrentWidget(widget)