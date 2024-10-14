import sys
from PySide6.QtWidgets import QApplication
from ai_proofreading_tool.frontend.main_window import MainWindow
from ai_proofreading_tool.database.database_setup import create_database

def main():
    # Ensure the database is set up
    create_database()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()