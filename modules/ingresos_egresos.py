from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QTableWidgetItem
from modules.ui_functions import cargar_ingreso, cargar_egreso, crear_campo_formulario
from modules.ui_styles import aplicar_estilos_especiales, crear_contenedor_con_estilo
from modules.database_operations import obtener_consolidado_stock


class IngresosEgresosWindow(QWidget):
    def __init__(self, usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent  # Referencia a la ventana principal para cambiar vistas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock - Ingresos/Egresos")
        
        # Crear el contenedor principal con estilo
        main_layout = crear_contenedor_con_estilo()

        # Crear el formulario usando la función modular
        form_layout = QFormLayout()

        # Campos del formulario
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
        btn_cargar_ingreso = QPushButton("Cargar Ingreso")
        btn_cargar_ingreso.clicked.connect(self.cargar_ingreso)

        btn_cargar_egreso = QPushButton("Cargar Egreso")
        btn_cargar_egreso.clicked.connect(self.cargar_egreso)

        btn_cargar_ajustes = QPushButton("Ir a Ajustes")
        btn_cargar_ajustes.clicked.connect(self.ir_a_ajustes)

        btn_ver_consolidado = QPushButton("Ver Consolidado")
        btn_ver_consolidado.clicked.connect(self.ver_consolidado)

        btn_mover_pallet = QPushButton("Mover Pallet")
        btn_mover_pallet.clicked.connect(self.mover_pallet)

        # Aplicar estilos especiales a los botones
        botones = [btn_cargar_ingreso, btn_cargar_egreso, btn_cargar_ajustes, btn_ver_consolidado, btn_mover_pallet]
        colores = ["green", "red", "gray", "blue", "blue"]
        aplicar_estilos_especiales(botones, colores)

        # Añadir el formulario y los botones al layout principal
        main_layout.addLayout(form_layout)
        main_layout.addStretch()  # Separar el formulario del final
        main_layout.addLayout(self.parent.crear_barra_botones_inferiores())  # Reutilizar la barra de botones inferior

        # Establecer el layout final
        self.setLayout(main_layout)
        
        
        # Funciones para los botones
    def cargar_ingreso(self):
        # Obtener los valores del formulario
        ubicacion = self.ubicacion_input.text().strip()
        codigo = self.codigo_input.text().strip()
        cantidad = self.cantidad_input.text().strip()
        fecha = self.fecha_input.text().strip()
        nota_devolucion = self.nota_input.text().strip()
        observaciones = self.observaciones_input.text().strip()

        # Validar que los campos obligatorios no estén vacíos
        if not ubicacion or not codigo or not cantidad or not fecha:
            print("Error: Los campos obligatorios no pueden estar vacíos.")
            return

        # Llamar a la función para registrar el ingreso en la base de datos
        cargar_ingreso(ubicacion, codigo, float(cantidad), fecha, nota_devolucion, observaciones)

        # Feedback para el usuario
        print(f"Ingreso registrado: {cantidad} unidades de {codigo} en la ubicación {ubicacion}.")


    def cargar_egreso(self):
        # Obtener los valores del formulario
        ubicacion = self.ubicacion_input.text().strip()
        codigo = self.codigo_input.text().strip()
        cantidad = self.cantidad_input.text().strip()
        fecha = self.fecha_input.text().strip()
        nota_devolucion = self.nota_input.text().strip()
        observaciones = self.observaciones_input.text().strip()

        # Validar que los campos obligatorios no estén vacíos
        if not ubicacion or not codigo or not cantidad or not fecha:
            print("Error: Los campos obligatorios no pueden estar vacíos.")
            return

        # Llamar a la función para registrar el egreso en la base de datos
        cargar_egreso(ubicacion, codigo, float(cantidad), fecha, nota_devolucion, observaciones)

        # Feedback para el usuario
        print(f"Egreso registrado: {cantidad} unidades de {codigo} desde la ubicación {ubicacion}.")

    def ir_a_ajustes(self):
        # Cambiar a la vista de Ajustes
        self.parent.mostrar_ajustes()

    def ver_consolidado(self):
        # Cambiar a la vista de Gestión de Stock (donde se muestra el consolidado)
        self.parent.mostrar_gestion_stock()

        # Seleccionar la pestaña de Consolidado dentro de la vista de gestión de stock
        self.parent.gestion_stock_view.tabs.setCurrentIndex(0)  # Pestaña 0 es la del Consolidado


    def mover_pallet(self):
        # Cambiar a la vista de Gestión de Stock
        self.parent.mostrar_gestion_stock()

        # Seleccionar la pestaña de Mover Pallet dentro de la vista de gestión de stock
        self.parent.gestion_stock_view.tabs.setCurrentIndex(2)