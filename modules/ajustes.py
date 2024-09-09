from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class AjustesView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout principal
        layout_principal = QVBoxLayout()

        label_titulo = QLabel("Ajustes de Stock")
        label_titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(label_titulo)

        # Formulario para hacer ajustes
        label_ubicacion = QLabel("Ubicación:")
        self.input_ubicacion = QLineEdit()
        layout_principal.addWidget(label_ubicacion)
        layout_principal.addWidget(self.input_ubicacion)

        label_codigo = QLabel("Código:")
        self.input_codigo = QLineEdit()
        layout_principal.addWidget(label_codigo)
        layout_principal.addWidget(self.input_codigo)

        label_cantidad = QLabel("Nueva Cantidad:")
        self.input_cantidad = QLineEdit()
        layout_principal.addWidget(label_cantidad)
        layout_principal.addWidget(self.input_cantidad)

        # Botón para aplicar ajuste
        btn_aplicar_ajuste = QPushButton("Aplicar Ajuste")
        btn_aplicar_ajuste.clicked.connect(self.aplicar_ajuste)
        layout_principal.addWidget(btn_aplicar_ajuste)

        self.setLayout(layout_principal)

    def aplicar_ajuste(self):
        # Aquí iría la lógica para aplicar el ajuste en la base de datos
        ubicacion = self.input_ubicacion.text()
        codigo = self.input_codigo.text()
        cantidad = self.input_cantidad.text()

        # Simulación de confirmación de ajuste
        QMessageBox.information(self, "Ajuste", f"Ajuste aplicado a {codigo} en {ubicacion} con nueva cantidad: {cantidad}")
