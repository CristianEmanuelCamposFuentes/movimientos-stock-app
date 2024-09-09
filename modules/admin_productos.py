from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class AdminProductosView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vista para Administrar Productos"))
        self.setLayout(layout)
