from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel
from modules.utils.ui_functions import crear_campo_formulario, cargar_ingreso, cargar_egreso
from modules.utils.ui_styles import aplicar_estilos_especiales
from PyQt6.uic import loadUi


class IngresosEgresosWindow(QWidget):
    def __init__(self, usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        loadUi("modules\\views\\ingresos_egresos\ingresos_egresos.ui", self)
        self.parent = parent  # Referencia a la ventana principal para cambiar vistas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock - Ingresos/Egresos")

        # Conectar las funcionalidades de los botones
        self.procesar_movimiento_button.clicked.connect(self.cargar_ingreso)
        self.cancelar_movimiento_button.clicked.connect(self.limpiar_formulario)
        self.limpiar_formulario_button.clicked.connect(self.limpiar_formulario)
        
        # Actualizar la barra inferior con los botones específicos de esta vista
        self.actualizar_barra_inferior()

    def actualizar_barra_inferior(self, indice=None):
        """Función para actualizar la barra inferior con los botones de Ingresos/Egresos."""
        botones_personalizados = [
            {"texto": "Cargar Ingreso", "funcion": lambda: self.procesar_movimiento('ingreso'), "color": "green"},
            {"texto": "Cargar Egreso", "funcion": lambda: self.procesar_movimiento('egreso'), "color": "red"},
            {"texto": "Ver Consolidado", "funcion": self.ver_consolidado, "color": "blue"},
            {"texto": "Mover Pallet", "funcion": self.mover_pallet, "color": "blue"}
        ]
        # Llamar a la función para actualizar la barra inferior con estos botones
        self.parent.actualizar_barra_inferior(botones_personalizados)

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

    def procesar_movimiento(self, tipo_movimiento):
        """Función genérica para manejar ingresos y egresos"""
        ubicacion = self.ubicacion_input.text().strip()
        codigo = self.codigo_input.text().strip()
        cantidad = self.cantidad_input.text().strip()
        fecha = self.fecha_input.text().strip()
        nota_devolucion = self.nota_input.text().strip()
        observaciones = self.observaciones_input.text().strip()

        # Validar que los campos obligatorios no estén vacíos
        if not ubicacion or not codigo or not cantidad or not fecha:
            print(f"Error: Los campos obligatorios no pueden estar vacíos para {tipo_movimiento}.")
            return

        if tipo_movimiento == "Ingreso":
            cargar_ingreso(ubicacion, codigo, float(cantidad), fecha, nota_devolucion, observaciones)
            print(f"{tipo_movimiento} registrado: {cantidad} unidades de {codigo} en la ubicación {ubicacion}.")
        elif tipo_movimiento == "Egreso":
            cargar_egreso(ubicacion, codigo, float(cantidad), fecha, nota_devolucion, observaciones)
            print(f"{tipo_movimiento} registrado: {cantidad} unidades de {codigo} desde la ubicación {ubicacion}.")
            
    def cargar_ingreso(self):
        self.procesar_movimiento("Ingreso")

    def cargar_egreso(self):
        self.procesar_movimiento("Egreso")
        
    def limpiar_formulario(self):
        self.ubicacion_input.clear()
        self.codigo_input.clear()
        self.cantidad_input.clear()
        self.fecha_input.clear()
        self.nota_input.clear()
        self.observaciones_input.clear()

