from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class RegistrosMovimientosView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vista para los Registros de Movimientos"))
        self.setLayout(layout)
