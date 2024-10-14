from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel
from modules.utils.ui_functions import crear_campo_formulario, cargar_ingreso, cargar_egreso
from modules.utils.ui_styles import aplicar_estilos_especiales


class IngresosEgresosWindow(QWidget):
    def __init__(self, usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent  # Referencia a la ventana principal para cambiar vistas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock - Ingresos/Egresos")

        # Layout principal para la vista
        main_layout = QVBoxLayout()

        # Crear el formulario usando la función modular
        form_layout = QFormLayout()

        # Campos del formulario
        self.ubicacion_label, self.ubicacion_input = crear_campo_formulario("Ubicación:", "Ingrese la ubicación")
        self.codigo_label, self.codigo_input = crear_campo_formulario("Código:", "Ingrese el código del producto")
        self.descripcion_label, self.descripcion_input = crear_campo_formulario("Descripción:", "Descripción del producto")
        self.cantidad_label, self.cantidad_input = crear_campo_formulario("Cantidad:", "Ingrese la cantidad")
        self.fecha_label, self.fecha_input = crear_campo_formulario("Fecha (DD/MM/YYYY):", "Ingrese la fecha")
        self.nota_label, self.nota_input = crear_campo_formulario("Nota/Devolución:", "Ingrese el número de nota o devolución")
        self.observaciones_label, self.observaciones_input = crear_campo_formulario("Observaciones:", "Ingrese observaciones")

        # Agregar los campos al layout del formulario
        form_layout.addRow(self.ubicacion_label, self.ubicacion_input)
        form_layout.addRow(self.codigo_label, self.codigo_input)
        form_layout.addRow(self.descripcion_label, self.descripcion_input)
        form_layout.addRow(self.cantidad_label, self.cantidad_input)
        form_layout.addRow(self.fecha_label, self.fecha_input)
        form_layout.addRow(self.nota_label, self.nota_input)
        form_layout.addRow(self.observaciones_label, self.observaciones_input)

        # Agregar el formulario al layout principal
        main_layout.addLayout(form_layout)

        # Generar la barra de botones inferior personalizada para esta vista
        botones = [
            {"texto": "Cargar Ingreso", "color": "green", "funcion": self.cargar_ingreso},
            {"texto": "Cargar Egreso", "color": "red", "funcion": self.cargar_egreso},
            {"texto": "Ver Consolidado", "color": "blue", "funcion": self.ver_consolidado},
            {"texto": "Mover Pallet", "color": "blue", "funcion": self.mover_pallet},
        ]
        bottom_bar = self.parent.crear_barra_botones_inferiores(botones)

        # Añadir la barra de botones al layout principal
        main_layout.addLayout(bottom_bar)

        # Aplicar el layout final a la ventana
        self.setLayout(main_layout)

    # Funciones para los botones
    def cargar_ingreso(self):
        """Función para cargar un ingreso"""
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
        """Función para cargar un egreso"""
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

    def ver_consolidado(self):
        """Función para ver el consolidado de stock"""
        # Cambiar a la vista de Gestión de Stock
        self.parent.mostrar_gestion_stock()

        # Seleccionar la pestaña de Consolidado dentro de la vista de gestión de stock
        self.parent.gestion_stock_view.tabs.setCurrentIndex(0)  # Pestaña 0 es la del Consolidado

    def mover_pallet(self):
        """Función para mover un pallet"""
        # Cambiar a la vista de Gestión de Stock
        self.parent.mostrar_gestion_stock()

        # Seleccionar la pestaña de Mover Pallet dentro de la vista de gestión de stock
        self.parent.gestion_stock_view.tabs.setCurrentIndex(2)

