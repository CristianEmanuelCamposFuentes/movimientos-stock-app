from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QTableWidget, QTableWidgetItem, QTabWidget, QTextEdit
from PyQt5.QtCore import Qt
from modules.database_operations import generar_nota_pedido, cargar_nota_pedido, obtener_registros_notas

class NotasPedidoView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notas de Pedido")
        layout = QVBoxLayout()

        # Crear las pestañas
        tabs = QTabWidget()
        tabs.addTab(self.generar_nota_tab(), "Generar Nota")
        tabs.addTab(self.cargar_nota_tab(), "Cargar Nota")
        tabs.addTab(self.registros_tab(), "Registros")

        # Agregar pestañas al layout principal
        layout.addWidget(tabs)
        self.setLayout(layout)

    # Pestaña 1: Generar Nota de Pedido
    def generar_nota_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        
        # Campos del formulario
        self.codigo_input = QLineEdit()
        form_layout.addRow("Código del producto:", self.codigo_input)

        self.cantidad_input = QLineEdit()
        form_layout.addRow("Cantidad requerida:", self.cantidad_input)

        self.descripcion_output = QTextEdit()
        self.descripcion_output.setReadOnly(True)
        form_layout.addRow("Descripción del producto:", self.descripcion_output)

        # Botón para generar la nota
        generar_button = QPushButton("Generar Nota de Pedido")
        generar_button.clicked.connect(self.generar_nota)

        layout.addLayout(form_layout)
        layout.addWidget(generar_button)

        widget.setLayout(layout)
        return widget

    # Función para generar la nota de pedido
    def generar_nota(self):
        codigo = self.codigo_input.text()
        cantidad = self.cantidad_input.text()
        descripcion = generar_nota_pedido(codigo, cantidad)  # Función simulada que genera la nota de pedido
        self.descripcion_output.setText(descripcion)  # Mostrar la descripción

    # Pestaña 2: Cargar Notas de Pedido
    def cargar_nota_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        
        # Campos del formulario
        self.numero_nota_input = QLineEdit()
        form_layout.addRow("Número de Nota:", self.numero_nota_input)

        self.ubicacion_input = QLineEdit()
        form_layout.addRow("Ubicación:", self.ubicacion_input)

        self.cantidad_entregada_input = QLineEdit()
        form_layout.addRow("Cantidad Entregada:", self.cantidad_entregada_input)

        # Botón para cargar la nota
        cargar_button = QPushButton("Cargar Nota")
        cargar_button.clicked.connect(self.cargar_nota)

        layout.addLayout(form_layout)
        layout.addWidget(cargar_button)

        widget.setLayout(layout)
        return widget

    # Función para cargar la nota de pedido
    def cargar_nota(self):
        numero_nota = self.numero_nota_input.text()
        ubicacion = self.ubicacion_input.text()
        cantidad_entregada = self.cantidad_entregada_input.text()
        resultado = cargar_nota_pedido(numero_nota, ubicacion, cantidad_entregada)  # Función simulada para cargar la nota
        print(resultado)  # Simulación de éxito

    # Pestaña 3: Registros de Notas de Pedido
    def registros_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Tabla para mostrar los registros de notas de pedido
        self.registros_table = QTableWidget(0, 5)
        self.registros_table.setHorizontalHeaderLabels(["Número de Nota", "Código", "Cantidad", "Ubicación", "Fecha"])
        layout.addWidget(self.registros_table)

        # Botón para buscar registros
        buscar_layout = QHBoxLayout()
        self.buscar_registros_input = QLineEdit()
        buscar_layout.addWidget(self.buscar_registros_input)
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(self.buscar_registros)
        buscar_layout.addWidget(buscar_button)
        layout.addLayout(buscar_layout)

        widget.setLayout(layout)
        return widget

    # Función para buscar registros de notas de pedido
    def buscar_registros(self):
        filtro = self.buscar_registros_input.text()
        resultados = obtener_registros_notas(filtro)  # Función simulada que devolvería los registros de notas
        self.registros_table.setRowCount(0)
        for i, item in enumerate(resultados):
            self.registros_table.insertRow(i)
            self.registros_table.setItem(i, 0, QTableWidgetItem(item["numero_nota"]))
            self.registros_table.setItem(i, 1, QTableWidgetItem(item["codigo"]))
            self.registros_table.setItem(i, 2, QTableWidgetItem(str(item["cantidad"])))
            self.registros_table.setItem(i, 3, QTableWidgetItem(item["ubicacion"]))
            self.registros_table.setItem(i, 4, QTableWidgetItem(item["fecha"]))
