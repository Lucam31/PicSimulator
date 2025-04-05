from PySide6.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the gui.py file
#     pyside6-uic form.ui -o gui.py, or
#     pyside2-uic form.ui -o gui.py
from gui.gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PIC-SIMU by Luca Mueller & Leander Gantert")
