from PySide6.QtWidgets import QMessageBox
from qfluentwidgets import MessageBox

class ConfirmationDialog(MessageBox):
    def __init__(self, title, message, parent=None):
        super().__init__(title, message, parent)
        self.setIcon(MessageBox.Icon.Warning)
        self.addButton("Yes", MessageBox.ButtonRole.YesRole)
        self.addButton("No", MessageBox.ButtonRole.NoRole)

class ErrorDialog(MessageBox):
    def __init__(self, title, message, parent=None):
        super().__init__(title, message, parent)
        self.setIcon(MessageBox.Icon.Error)
        self.addButton("OK", MessageBox.ButtonRole.AcceptRole)

class InfoDialog(MessageBox):
    def __init__(self, title, message, parent=None):
        super().__init__(title, message, parent)
        self.setIcon(MessageBox.Icon.Information)
        self.addButton("OK", MessageBox.ButtonRole.AcceptRole)