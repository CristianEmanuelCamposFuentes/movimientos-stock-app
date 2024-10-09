import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtGui import QColor, QPalette
from datetime import datetime
import sqlite3

# Importar los estilos globales
from modules.ui_styles import aplicar_estilos_especiales, aplicar_estilo_global

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.habilitar_formulario(False)  # El formulario está deshabilitado inicialmente

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Botones de tipo de movimiento
        self.ingreso_button = QPushButton("Ingresar Ingresos")
        self.egreso_button = QPushButton("Ingresar Egresos")
        self.ingreso_button.clicked.connect(lambda: self.desplegar_formulario("Ingreso"))
        self.egreso_button.clicked.connect(lambda: self.desplegar_formulario("Egreso"))

        # Aplicar estilos a los botones
        aplicar_estilos_especiales([self.ingreso_button, self.egreso_button], ["green", "red"])

        layout.addWidget(self.ingreso_button)
        layout.addWidget(self.egreso_button)

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

        self.observaciones_label = QLabel("Observaciones:")
        self.observaciones_input = QLineEdit()
        layout.addWidget(self.observaciones_label)
        layout.addWidget(self.observaciones_input)

        # Botón para registrar el movimiento
        self.registrar_button = QPushButton("Registrar Movimiento")
        self.registrar_button.clicked.connect(self.registrar_movimiento)
        aplicar_estilos_especiales([self.registrar_button], ["blue"])  # Aplicar estilo al botón de registrar

        layout.addWidget(self.registrar_button)

        # Establecer layout
        self.setLayout(layout)

    def habilitar_formulario(self, habilitar):
        """Habilitar o deshabilitar el formulario completo"""
        widgets = [self.ubicacion_input, self.codigo_input, self.descripcion_input,
                   self.cantidad_input, self.fecha_input, self.nota_devolucion_input,
                   self.observaciones_input, self.registrar_button]
        
        # Habilitar/deshabilitar campos y cambiar el color de fondo
        for widget in widgets:
            widget.setEnabled(habilitar)
            pal = widget.palette()
            pal.setColor(QPalette.Base, QColor(255, 255, 255) if habilitar else QColor(200, 200, 200))  # Fondo blanco/gris
            widget.setPalette(pal)

    def desplegar_formulario(self, tipo_movimiento):
        """Desbloquear el formulario y establecer el tipo de movimiento"""
        self.habilitar_formulario(True)
        self.tipo_movimiento = tipo_movimiento

    def registrar_movimiento(self):
        """Lógica para registrar el movimiento en la base de datos"""
        ubicacion = self.ubicacion_input.text().strip()
        codigo = self.codigo_input.text().strip()
        descripcion = self.descripcion_input.text().strip()
        cantidad = self.cantidad_input.text().strip()
        fecha = self.fecha_input.text().strip()
        nota_devolucion = self.nota_devolucion_input.text().strip()
        observaciones = self.observaciones_input.text().strip()

        # Validar los campos
        if not ubicacion or not codigo or not cantidad:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return

        try:
            cantidad = float(cantidad)
            self.insertar_en_base_datos(ubicacion, codigo, descripcion, cantidad, fecha, nota_devolucion, self.tipo_movimiento, observaciones)
            QMessageBox.information(self, "Éxito", "Movimiento registrado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo registrar el movimiento: {str(e)}")

    def insertar_en_base_datos(self, ubicacion, codigo, descripcion, cantidad, fecha, nota_devolucion, tipo_movimiento, observaciones):
        """Insertar el movimiento en la base de datos SQLite"""
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

    # Aplicar estilos globales
    aplicar_estilo_global(app)

    ventana = Form()
    ventana.show()
    sys.exit(app.exec_())
