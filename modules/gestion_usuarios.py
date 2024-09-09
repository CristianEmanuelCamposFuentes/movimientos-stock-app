from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class GestionUsuariosView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vista para la Gestión de Usuarios"))
        self.setLayout(layout)
