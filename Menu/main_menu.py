# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_menu.py file
#     pyside6-uic menu.ui -o ui_menu.py, or
#     pyside2-uic menu.ui -o ui_menu.py
from ui_form import Ui_Main_menu

class Main_menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main_menu()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main_menu()
    widget.show()
    sys.exit(app.exec())
