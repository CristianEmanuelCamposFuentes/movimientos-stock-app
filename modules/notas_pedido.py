from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class NotasPedidoView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vista para Generar y Cargar Notas de Pedido"))
        self.setLayout(layout)
