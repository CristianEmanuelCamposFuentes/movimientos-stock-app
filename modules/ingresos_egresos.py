from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QFormLayout
from PyQt5.QtCore import QDate
from modules.ui_functions import cargar_ingreso, cargar_egreso
from modules.ui_functions import crear_campo_formulario
from modules.ui_styles import aplicar_estilos_especiales
from modules.gestion_stock import GestionStockView
from modules.database_operations import get_description_by_code
from modules.database_operations import obtener_consolidado_stock



class IngresosEgresosWindow(QWidget):
    def __init__(self, usuario,parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent  # Referencia a la ventana principal para cambiar vistas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock - Ingresos/Egresos")
        
        # Layout principal
        layout = QVBoxLayout()

        # Crear el formulario usando la función modular
        form_layout = QFormLayout()

        ubicacion_label, ubicacion_input = crear_campo_formulario("Ubicación:", "Ingrese la ubicación")
        codigo_label, codigo_input = crear_campo_formulario("Código:", "Ingrese el código del producto")
        descripcion_label, descripcion_input = crear_campo_formulario("Descripción:", "Descripción del producto")
        cantidad_label, cantidad_input = crear_campo_formulario("Cantidad:", "Ingrese la cantidad")
        fecha_label, fecha_input = crear_campo_formulario("Fecha (DD/MM/YYYY):", "Ingrese la fecha")
        nota_label, nota_input = crear_campo_formulario("Nota/Devolución:", "Ingrese el número de nota o devolución")
        observaciones_label, observaciones_input = crear_campo_formulario("Observaciones:", "Ingrese observaciones")

        # Agregar los campos al layout del formulario
        form_layout.addRow(ubicacion_label, ubicacion_input)
        form_layout.addRow(codigo_label, codigo_input)
        form_layout.addRow(descripcion_label, descripcion_input)
        form_layout.addRow(cantidad_label, cantidad_input)
        form_layout.addRow(fecha_label, fecha_input)
        form_layout.addRow(nota_label, nota_input)
        form_layout.addRow(observaciones_label, observaciones_input)

        # Crear los botones de acción
        buttons_layout = QHBoxLayout()

        # Botón para cargar Ingreso
        btn_cargar_ingreso = QPushButton("Cargar Ingreso")
        btn_cargar_ingreso.setStyleSheet("background-color: green; color: white;")
        btn_cargar_ingreso.clicked.connect(self.cargar_ingreso)  # Conecta con la función cargar_ingreso

        # Botón para cargar Egreso
        btn_cargar_egreso = QPushButton("Cargar Egreso")
        btn_cargar_egreso.setStyleSheet("background-color: red; color: white;")
        btn_cargar_egreso.clicked.connect(self.cargar_egreso)  # Conecta con la función cargar_egreso

        # Botón para ir a Ajustes
        btn_cargar_ajustes = QPushButton("Ir a Ajustes")
        btn_cargar_ajustes.clicked.connect(self.ir_a_ajustes)  # Conecta con la función ir_a_ajustes

        # Botón para ver Consolidado
        btn_ver_consolidado = QPushButton("Ver Consolidado")
        btn_ver_consolidado.clicked.connect(self.ver_consolidado)  

        # Botón para mover Pallet
        btn_mover_pallet = QPushButton("Mover Pallet")
        btn_mover_pallet.clicked.connect(self.mover_pallet) 
        
        # Añadir botones al layout
        buttons_layout.addWidget(btn_cargar_ingreso)
        buttons_layout.addWidget(btn_cargar_egreso)
        buttons_layout.addWidget(btn_cargar_ajustes)
        buttons_layout.addWidget(btn_ver_consolidado)
        buttons_layout.addWidget(btn_mover_pallet)

        # Agregar el formulario y los botones al layout principal
        layout.addLayout(form_layout)
        layout.addLayout(buttons_layout)
        layout.setContentsMargins(20, 20, 20, 20) 
        self.setLayout(layout)
        
        # Aplicar estilos especiales
        # En el método initUI o donde crees los botones:
        botones = [btn_cargar_ingreso, btn_cargar_egreso, btn_cargar_ajustes]
        colores = ["green", "red", "gray"]  # Definir colores específicos para cada botón
        aplicar_estilos_especiales(botones, colores)

 # Funciones para los botones
    def cargar_ingreso(self):
        print("Cargar Ingreso")

    def cargar_egreso(self):
            print("Cargar Egreso")

    def ir_a_ajustes(self):
        print("Ir a Ajustes")
        self.parent.mostrar_ajustes()

    def ver_consolidado(self):
        print("Ver Consolidado")
        consolidado = obtener_consolidado_stock()
         # Supongamos que 'self.table_widget' es el QTableWidget donde mostrarás el stock
        self.stock_table.setRowCount(0)  # Limpiar tabla antes de llenarla
        for i, item in enumerate(consolidado):
            self.stock_table.insertRow(i)
            self.stock_table.setItem(i, 0, QTableWidgetItem(item.codigo))
            self.stock_table.setItem(i, 1, QTableWidgetItem(item.descripcion))
            self.stock_table.setItem(i, 2, QTableWidgetItem(str(item.cantidad)))
            self.stock_table.setItem(i, 3, QTableWidgetItem(item.ubicacion))
            self.stock_table.setItem(i, 4, QTableWidgetItem(item.fecha.strftime("%d/%m/%Y")))
            
        

    def mover_pallet(self):
        print("Mover Pallet")
        self.parent.mostrar_gestion_stock()