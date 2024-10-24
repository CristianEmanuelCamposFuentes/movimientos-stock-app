from PyQt6.QtWidgets import QInputDialog, QMessageBox,QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QFormLayout, QStackedWidget
from modules.models.database_operations import obtener_consolidado_stock, realizar_ajuste_stock, mover_pallet
from modules.utils.ui_styles import aplicar_estilos_especiales, crear_contenedor_con_estilo
from PyQt6.uic import loadUi
from modules.models.database import get_db
from modules.models.database import Stock, Movimiento, Producto
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QInputDialog
from datetime import datetime

class GestionStockView(QTabWidget):
    def __init__(self, parent=None,stack = None):
        super().__init__(parent)
        self.parent = parent  # Referencia a la ventana principal
        self.stack = stack
        # Cargar la interfaz de Qt Designer
        loadUi("modules\\views\\gestion_stock\\gestion_stock.ui", self)

        # Luego de cargar la UI, puedes conectar los eventos o funciones según sea necesario.
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Stock")
        
        # Conectar el cambio de pestaña a la actualización de la barra inferior
        self.currentChanged.connect(self.actualizar_barra_inferior)
        # Actualizar la barra inferior inicialmente con los botones de la primera pestaña
        self.actualizar_barra_inferior(0)

    # Función para cambiar la vista en el QStackedWidget
    def cambiar_vista(self, indice):
        self.stack.setCurrentIndex(indice)
        self.actualizar_barra_inferior(indice)

    # Función para actualizar la barra inferior según la vista activa
    def actualizar_barra_inferior(self, indice):
        if indice == 0:  # Consolidado
            botones = [
            {"texto": "Exportar a Excel", "color": "alge", "funcion": self.exportar_excel},
            {"texto": "Exportar a CSV", "color": "alge", "funcion": self.exportar_csv},
            {"texto": "Generar PDF", "color": "alge", "funcion": self.generar_pdf},
            {"texto": "Imprimir Pallet", "color": "alge", "funcion": self.imprimir_pallet}
            ]
        elif indice == 1:  # Ajustes
            botones = [
                {"texto": "Confirmar Ajustes", "color": "green", "funcion": self.confirmar_ajustes},
                {"texto": "Mover Pallet", "color": "salmon", "funcion": lambda: self.cambiar_vista(2)}

            ]
        elif indice == 2:  # Mover Pallet
            botones = [
                {"texto": "Solicitar Ubicaciones", "color": "alge", "funcion": self.solicitar_ubicaciones},
                {"texto": "Mover Todo", "color": "green", "funcion": self.mover_todo, "deshabilitado": True},
                {"texto": "Mover Seleccionados", "color": "blue", "funcion": self.mover_seleccionados, "deshabilitado": True},
                {"texto": "Cancelar", "color": "red", "funcion": self.cancelar_movimiento, "deshabilitado": True}
            ]
        self.parent.actualizar_barra_inferior(botones)

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

    # Pestaña 2: Mover Pallet (igual que antes)
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

    # Función para mover pallet (igual que antes)
    def mover_pallet(self):
        codigo_pallet = self.codigo_pallet_input.text()
        ubicacion_actual = self.ubicacion_actual_input.text()
        nueva_ubicacion = self.ubicacion_nueva_input.text()
        mover_pallet(codigo_pallet, ubicacion_actual, nueva_ubicacion, 0)

    # Funciones adicionales
    def exportar_excel(self):
        print("Exportando a Excel...")

    def exportar_csv(self):
        print("Exportando a CSV...")

    def generar_pdf(self):
        print("Generando PDF...")

    def imprimir_pallet(self):
        print("Imprimiendo pallet...")
        
    def confirmar_movimiento_pallet(self):
        # Verificar que los pallets existan y tengan productos
        if self.origen_table.rowCount() == 0 or self.destino_table.rowCount() == 0:
            print("Error: No hay productos en los pallets seleccionados.")
            return

        # TODO: Validar cantidades y mover productos
        # Implementar la lógica para mover de origen a destino
        # Esto implica modificar la tabla Stock y registrar el movimiento en la tabla de Movimiento

        # Ejemplo básico de movimiento
        for i in range(self.origen_table.rowCount()):
            cantidad_a_mover = float(self.origen_table.item(i, 3).text())  # Cantidad a mover
            # Validar si la cantidad es válida, mover a destino, etc.

        # Actualizar las tablas después del movimiento
        self.actualizar_tablas_pallet()


    def cargar_pallet(self, pallet, destino=False):
        table = self.table_pallet_actual if not destino else self.table_pallet_destino
        table.setRowCount(0)  # Limpiar la tabla
        
        for i, item in enumerate(pallet):
            table.insertRow(i)
            checkbox_item = QTableWidgetItem()
            checkbox_item.setCheckState(True)  # Inicialmente marcado
            table.setItem(i, 0, checkbox_item)  # Colocar el checkbox en la primera columna

            # Cargar el resto de los detalles en las siguientes columnas
            table.setItem(i, 1, QTableWidgetItem(item.codigo))
            table.setItem(i, 2, QTableWidgetItem(item.descripcion))
            table.setItem(i, 3, QTableWidgetItem(item.ubicacion))
            table.setItem(i, 4, QTableWidgetItem(str(item.cantidad)))
            table.setItem(i, 5, QTableWidgetItem(item.fecha.strftime('%d/%m/%Y')))

    def mover_todo(self):
        for i in range(self.table_pallet_actual.rowCount()):
            producto = self.table_pallet_actual.item(i, 1).text()
            cantidad = self.table_pallet_actual.item(i, 4).text()
            # Verificar la cantidad y mover a la ubicación de destino
            mover_pallet(producto, cantidad, self.ubicacion_destino)
        self.actualizar_tablas_pallet()



    def solicitar_ubicaciones(self):
        ubicacion_origen, ok_origen = QInputDialog.getText(self, "Ubicación Pallet Origen", "Ingrese el código de ubicación del pallet origen:")
        if ok_origen:
            ubicacion_origen = ubicacion_origen.replace(".", ",").upper()
            if self.verificar_pallet(ubicacion_origen):
                ubicacion_destino, ok_destino = QInputDialog.getText(self, "Ubicación Pallet Destino", "Ingrese el código de ubicación del pallet destino:")
                if ok_destino:
                    ubicacion_destino = ubicacion_destino.replace(".", ",").upper()
                    self.cargar_pallet(ubicacion_origen)
                    self.cargar_pallet(ubicacion_destino, destino=True)
                    self.habilitar_botones_movimiento(True)
                else:
                    QMessageBox.warning(self, "Error", "No se ingresó ninguna ubicación para el pallet destino.")
            else:
                QMessageBox.warning(self, "Error", "El pallet de origen no contiene productos.")

            
    def verificar_pallet(ubicacion: str):
        db = next(get_db())
        try:
            stock_items = db.query(Stock).filter(Stock.ubicacion == ubicacion).all()
            return len(stock_items) > 0  # Devuelve True si hay productos en el pallet
        except Exception as e:
            print(f"Error al verificar el pallet: {e}")
            return False
        finally:
            db.close()       

    def mover_seleccionados(self):
        # Mover solo los productos seleccionados (checkbox marcado)
        for i in range(self.table_pallet_actual.rowCount()):
            checkbox = self.table_pallet_actual.item(i, 0)
            if checkbox.checkState() == Qt.CheckState.Checked:
                producto = self.table_pallet_actual.item(i, 1).text()
                cantidad = self.table_pallet_actual.item(i, 4).text()
                # Mover solo los productos seleccionados a la nueva ubicación
                mover_pallet(producto, cantidad, self.ubicacion_destino)
        self.actualizar_tablas_pallet()

    def cancelar_movimiento(self):
        # Limpiar las tablas o resetear el estado de la vista
        self.table_pallet_actual.clearContents()
        self.table_pallet_destino.clearContents()
        self.habilitar_botones_movimiento(False)
        
    def habilitar_botones_movimiento(self, habilitar):
        self.boton_mover_todo.setEnabled(habilitar)
        self.boton_mover_seleccionados.setEnabled(habilitar)
        self.boton_cancelar.setEnabled(habilitar)


    def confirmar_ajustes(self):
        """Confirma los ajustes realizados en la tabla de stock y los registra en la base de datos."""
        db = next(get_db())
        try:
            for row in range(self.table_ajustes.rowCount()):
                ubicacion = self.table_ajustes.item(row, 0).text()  # Ubicación
                codigo = self.table_ajustes.item(row, 1).text()  # Código del producto
                cantidad = float(self.table_ajustes.item(row, 3).text())  # Cantidad ajustada
                fecha = datetime.strptime(self.table_ajustes.item(row, 4).text(), "%d/%m/%Y")  # Fecha de ajuste

                # Buscar el stock del producto en la ubicación indicada
                stock_item = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion, Producto.codigo == codigo).first()
                if stock_item:
                    # Actualizar la cantidad en el stock
                    stock_item.cantidad = cantidad
                    stock_item.fecha = fecha

                    # Registrar el ajuste como un movimiento en la tabla Movimiento
                    movimiento = Movimiento(
                        ubicacion=ubicacion,
                        codigo=codigo,
                        cantidad=cantidad,
                        fecha=fecha,
                        nota_devolucion="Ajuste de Stock",
                        tipo_movimiento="Ajuste",
                        observaciones="Ajuste manual desde la pestaña Ajustes"
                    )
                    db.add(movimiento)

            db.commit()  # Confirmar los cambios
            QMessageBox.information(self, "Éxito", "Los ajustes han sido confirmados y guardados correctamente.")
            print("Ajustes confirmados y guardados correctamente.")

        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Error", f"Error al confirmar ajustes: {e}")
            print(f"Error al confirmar ajustes: {e}")

        finally:
            db.close()
        