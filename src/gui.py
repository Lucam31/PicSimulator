import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 GUI Template")

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Example button
        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        print("Button clicked!")
