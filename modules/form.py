import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from datetime import datetime
import sqlite3

class StockMovementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()

        # Campos del formulario
        self.ubicacion_label = QLabel("Ubicación:")
        self.ubicacion_input = QLineEdit()
        layout.addWidget(self.ubicacion_label)
        layout.addWidget(self.ubicacion_input)

        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit()
        layout.addWidget(self.codigo_label)
        layout.addWidget(self.codigo_input)

        self.descripcion_label = QLabel("Descripción:")
        self.descripcion_input = QLineEdit()
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.descripcion_input)

        self.cantidad_label = QLabel("Cantidad:")
        self.cantidad_input = QLineEdit()
        layout.addWidget(self.cantidad_label)
        layout.addWidget(self.cantidad_input)

        self.fecha_label = QLabel("Fecha (DD/MM/YYYY):")
        self.fecha_input = QLineEdit(datetime.now().strftime('%d/%m/%Y'))
        layout.addWidget(self.fecha_label)
        layout.addWidget(self.fecha_input)

        self.nota_devolucion_label = QLabel("Nota/Devolución:")
        self.nota_devolucion_input = QLineEdit()
        layout.addWidget(self.nota_devolucion_label)
        layout.addWidget(self.nota_devolucion_input)

        self.tipo_movimiento_label = QLabel("Tipo de Movimiento:")
        self.tipo_movimiento_combo = QComboBox()
        self.tipo_movimiento_combo.addItems(["Ingreso", "Egreso"])
        layout.addWidget(self.tipo_movimiento_label)
        layout.addWidget(self.tipo_movimiento_combo)

        self.observaciones_label = QLabel("Observaciones:")
        self.observaciones_input = QLineEdit()
        layout.addWidget(self.observaciones_label)
        layout.addWidget(self.observaciones_input)

        # Botón para registrar el movimiento
        self.registrar_button = QPushButton("Registrar Movimiento")
        self.registrar_button.clicked.connect(self.registrar_movimiento)
        layout.addWidget(self.registrar_button)

        self.setLayout(layout)

    def registrar_movimiento(self):
        # Aquí agregamos la lógica para procesar el movimiento
        ubicacion = self.ubicacion_input.text()
        codigo = self.codigo_input.text()
        descripcion = self.descripcion_input.text()
        cantidad = self.cantidad_input.text()
        fecha = self.fecha_input.text()
        nota_devolucion = self.nota_devolucion_input.text()
        tipo_movimiento = self.tipo_movimiento_combo.currentText()
        observaciones = self.observaciones_input.text()

        # Validar los campos (similar a como lo tenías en Tkinter)
        if not ubicacion or not codigo or not cantidad:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return

        # Aquí podrías insertar los datos en la base de datos SQLite
        try:
            cantidad = float(cantidad)
            self.insertar_en_base_datos(ubicacion, codigo, descripcion, cantidad, fecha, nota_devolucion, tipo_movimiento, observaciones)
            QMessageBox.information(self, "Éxito", "Movimiento registrado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo registrar el movimiento: {str(e)}")

    def insertar_en_base_datos(self, ubicacion, codigo, descripcion, cantidad, fecha, nota_devolucion, tipo_movimiento, observaciones):
        # Conectar con SQLite e insertar el movimiento
        conexion = sqlite3.connect('data/stock_management.db')
        cursor = conexion.cursor()
        
        cursor.execute('''
            INSERT INTO movimientos (ubicacion, codigo, cantidad, fecha, nota_devolucion, tipo_movimiento, observaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ubicacion, codigo, cantidad, fecha, nota_devolucion, tipo_movimiento, observaciones))

        conexion.commit()
        conexion.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = StockMovementApp()
    ventana.show()
    sys.exit(app.exec_())


