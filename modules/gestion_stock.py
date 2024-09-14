from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QFormLayout
from PyQt5.QtCore import Qt
from modules.database_operations import obtener_consolidado_stock, realizar_ajuste_stock, mover_pallet
from modules.ui_styles import aplicar_estilos_especiales, crear_contenedor_con_estilo


class GestionStockView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Referencia a la ventana principal
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Stock")

        # Crear el contenedor principal con estilo
        main_layout = crear_contenedor_con_estilo()

        # Crear las pestañas
        self.tabs = QTabWidget()
        self.tabs.addTab(self.consolidado_tab(), "Consolidado")
        self.tabs.addTab(self.ajustes_tab(), "Ajustes")
        self.tabs.addTab(self.mover_pallet_tab(), "Mover Pallet")

        # Conectar el cambio de pestañas al evento para actualizar la tabla
        self.tabs.currentChanged.connect(self.on_tab_changed)

        # Agregar pestañas al layout principal
        main_layout.addWidget(self.tabs)
        #main_layout.addLayout(self.parent.crear_barra_botones_inferiores())  # Barra de botones inferior reutilizable
        self.setLayout(main_layout)

    # Pestaña 1: Consolidado
    def consolidado_tab(self):
        consolidado_widget = QWidget()
        layout = QVBoxLayout()

        # Buscador de stock
        buscar_layout = QHBoxLayout()
        self.buscar_input = QLineEdit()
        buscar_layout.addWidget(QLabel("Buscar:"))
        buscar_layout.addWidget(self.buscar_input)
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(self.buscar_consolidado)
        buscar_layout.addWidget(buscar_button)
        layout.addLayout(buscar_layout)

        # Tabla para mostrar el consolidado de stock
        self.consolidado_table = QTableWidget(0, 5)
        self.consolidado_table.setHorizontalHeaderLabels(["Código", "Descripción", "Ubicación", "Cantidad", "Fecha"])
        layout.addWidget(self.consolidado_table)

        # Botones de exportar e imprimir
        export_layout = QHBoxLayout()
        export_excel_button = QPushButton("Exportar a Excel")
        export_csv_button = QPushButton("Exportar a CSV")
        generar_pdf_button = QPushButton("Generar PDF")
        imprimir_pallet_button = QPushButton("Imprimir Pallet")
        export_layout.addWidget(export_excel_button)
        export_layout.addWidget(export_csv_button)
        export_layout.addWidget(generar_pdf_button)
        export_layout.addWidget(imprimir_pallet_button)

        # Aplicar estilos a los botones
        botones = [export_excel_button, export_csv_button, generar_pdf_button, imprimir_pallet_button]
        colores = ["alge", "alge", "alge", "alge"]
        aplicar_estilos_especiales(botones, colores)

        layout.addLayout(export_layout)

        consolidado_widget.setLayout(layout)
        return consolidado_widget

    # Función para buscar y filtrar consolidado
    def buscar_consolidado(self):
        filtro = self.buscar_input.text()
        resultados = obtener_consolidado_stock(filtro)
        self.consolidado_table.setRowCount(0)
        for i, item in enumerate(resultados):
            self.consolidado_table.insertRow(i)
            self.consolidado_table.setItem(i, 0, QTableWidgetItem(item.codigo))
            self.consolidado_table.setItem(i, 1, QTableWidgetItem(item.descripcion))
            self.consolidado_table.setItem(i, 2, QTableWidgetItem(item.ubicacion))
            self.consolidado_table.setItem(i, 3, QTableWidgetItem(str(item.cantidad)))
            self.consolidado_table.setItem(i, 4, QTableWidgetItem(item.fecha.strftime('%d/%m/%Y')))

    # Pestaña 2: Ajustes
    def ajustes_tab(self):
        ajustes_widget = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.codigo_input = QLineEdit()
        form_layout.addRow("Código del producto:", self.codigo_input)

        self.ubicacion_input = QLineEdit()
        form_layout.addRow("Ubicación:", self.ubicacion_input)

        self.cantidad_input = QLineEdit()
        form_layout.addRow("Cantidad ajustada:", self.cantidad_input)

        ajustar_button = QPushButton("Ajustar Stock")
        ajustar_button.clicked.connect(self.ajustar_stock)
        
        # Aplicar estilo especial al botón
        aplicar_estilos_especiales([ajustar_button], ["grass"])

        layout.addLayout(form_layout)
        layout.addWidget(ajustar_button)

        ajustes_widget.setLayout(layout)
        return ajustes_widget

    # Función para realizar ajuste de stock
    def ajustar_stock(self):
        codigo = self.codigo_input.text()
        ubicacion = self.ubicacion_input.text()
        cantidad = self.cantidad_input.text()
        realizar_ajuste_stock(ubicacion, codigo, float(cantidad))

    # Pestaña 3: Mover Pallet
    def mover_pallet_tab(self):
        mover_pallet_widget = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.codigo_pallet_input = QLineEdit()
        form_layout.addRow("Código del pallet:", self.codigo_pallet_input)

        self.ubicacion_actual_input = QLineEdit()
        form_layout.addRow("Ubicación actual:", self.ubicacion_actual_input)

        self.ubicacion_nueva_input = QLineEdit()
        form_layout.addRow("Nueva ubicación:", self.ubicacion_nueva_input)

        mover_button = QPushButton("Mover Pallet")
        mover_button.clicked.connect(self.mover_pallet)
        
        # Aplicar estilo especial al botón
        aplicar_estilos_especiales([mover_button], ["salmon"])

        layout.addLayout(form_layout)
        layout.addWidget(mover_button)

        mover_pallet_widget.setLayout(layout)
        return mover_pallet_widget

    # Función para mover pallet
    def mover_pallet(self):
        codigo_pallet = self.codigo_pallet_input.text()
        ubicacion_actual = self.ubicacion_actual_input.text()
        nueva_ubicacion = self.ubicacion_nueva_input.text()
        mover_pallet(codigo_pallet, ubicacion_actual, nueva_ubicacion, 0)

    # Función para actualizar automáticamente la tabla de consolidado cuando se selecciona la pestaña
    def on_tab_changed(self, index):
        if index == 0:  # Pestaña de consolidado
            self.buscar_consolidado()