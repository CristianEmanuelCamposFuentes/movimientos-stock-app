from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QTabWidget, QFileDialog, QMessageBox
from modules.database_operations import obtener_movimientos_historicos, obtener_movimientos_pendientes, generar_pdf, exportar_csv
from modules.ui_styles import aplicar_estilos_especiales
from modules.database import get_db, Movimiento, Pendiente


class RegistrosMovimientosView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Referencia a la ventana principal
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registros de Movimientos")
        layout = QVBoxLayout()

        # Crear las pestañas
        tabs = QTabWidget()
        tabs.addTab(self.registros_historicos_tab(), "Registros Históricos")
        tabs.addTab(self.pendientes_tab(), "Pendientes")

        # Agregar pestañas al layout principal
        layout.addWidget(tabs)
        self.setLayout(layout)

    # Pestaña 1: Registros Históricos
    def registros_historicos_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Tabla para mostrar los registros históricos
        self.historico_table = QTableWidget(0, 6)
        self.historico_table.setHorizontalHeaderLabels(
            ["Ubicación", "Código", "Cantidad", "Fecha", "Nota/Devolución", "Observaciones"]
        )
        layout.addWidget(self.historico_table)

        # Cargar registros históricos
        self.cargar_registros_historicos()

        # Barra inferior personalizada
        botones = [
            {"texto": "Exportar a PDF", "color": "blue", "funcion": self.exportar_pdf},
            {"texto": "Exportar a CSV", "color": "alge", "funcion": self.exportar_csv},
            {"texto": "Filtrar", "color": "grass", "funcion": self.filtrar_registros}
        ]
        bottom_bar = self.parent.crear_barra_botones_inferiores(botones)
        layout.addLayout(bottom_bar)

        widget.setLayout(layout)
        return widget

    # Función para cargar los registros históricos
    def cargar_registros_historicos(self):
        db = next(get_db())  # Obtiene la sesión de la base de datos
        try:
            movimientos = obtener_movimientos_historicos(db)  # Pasa la sesión como argumento
            self.tabla_registros.setRowCount(len(movimientos))
            for row, mov in enumerate(movimientos):
                self.tabla_registros.setItem(row, 0, QTableWidgetItem(mov['ubicacion']))
                self.tabla_registros.setItem(row, 1, QTableWidgetItem(mov['codigo']))
                self.tabla_registros.setItem(row, 2, QTableWidgetItem(str(mov['cantidad'])))
                self.tabla_registros.setItem(row, 3, QTableWidgetItem(mov['fecha'].strftime('%d/%m/%Y')))
                self.tabla_registros.setItem(row, 4, QTableWidgetItem(mov['nota_devolucion']))
                self.tabla_registros.setItem(row, 5, QTableWidgetItem(mov['observaciones']))
        except Exception as e:
            print(f"Error al cargar registros históricos: {e}")
        finally:
            db.close()  # Asegúrate de cerrar la sesión
    # Función para exportar a PDF
    def exportar_pdf(self):
        db = next(get_db())  # Obtener la sesión de la base de datos
        movimientos = obtener_movimientos_historicos(db)  # Pasar la sesión como argumento
        ruta_pdf, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "", "PDF Files (*.pdf)")
        if ruta_pdf:
            generar_pdf(movimientos, ruta_pdf)  # Función simulada para generar el PDF
            QMessageBox.information(self, "Éxito", f"PDF generado en {ruta_pdf}")
        db.close()  # Cerrar la sesión 
     
    # Función para exportar a CSV
    def exportar_csv(self):
        db = next(get_db())  # Obtener la sesión de la base de datos
        movimientos = obtener_movimientos_historicos(db)  # Pasar la sesión como argumento
        ruta_csv, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "CSV Files (*.csv)")
        if ruta_csv:
            exportar_csv(movimientos, ruta_csv)  # Usamos la función de exportar_csv
            QMessageBox.information(self, "Éxito", f"CSV generado en {ruta_csv}")
        db.close()  # Cerrar la sesión

    # Función para filtrar registros (Placeholder)
    def filtrar_registros(self):
        QMessageBox.information(self, "Filtrar", "Se implementará la funcionalidad de filtrado.")

    # Pestaña 2: Pendientes
    def pendientes_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Tabla para mostrar los pendientes
        self.pendientes_table = QTableWidget(0, 6)
        self.pendientes_table.setHorizontalHeaderLabels(
            ["Ubicación", "Código", "Cantidad", "Fecha", "Motivo", "Acciones"]
        )
        layout.addWidget(self.pendientes_table)

        # Cargar pendientes
        self.cargar_pendientes()

        # Barra inferior personalizada para la pestaña de Pendientes
        botones = [
            {"texto": "Actualizar Pendientes", "color": "blue", "funcion": self.cargar_pendientes}
        ]
        bottom_bar = self.parent.crear_barra_botones_inferiores(botones)
        layout.addLayout(bottom_bar)

        widget.setLayout(layout)
        return widget

    # Función para cargar los pendientes
    def cargar_pendientes(self):
        db = next(get_db())  # Obtener la sesión de la base de datos
        pendientes = obtener_movimientos_pendientes(db)  # Pasar la sesión como argumento
        self.pendientes_table.setRowCount(0)
        for i, pendiente in enumerate(pendientes):
            self.pendientes_table.insertRow(i)
            self.pendientes_table.setItem(i, 0, QTableWidgetItem(pendiente["ubicacion"]))
            self.pendientes_table.setItem(i, 1, QTableWidgetItem(pendiente["codigo"]))
            self.pendientes_table.setItem(i, 2, QTableWidgetItem(str(pendiente["cantidad"])))
            self.pendientes_table.setItem(i, 3, QTableWidgetItem(pendiente["fecha"].strftime("%d/%m/%Y")))
            self.pendientes_table.setItem(i, 4, QTableWidgetItem(pendiente["motivo"]))

            # Botones de acción: Ver Ubicación, Registrar Movimiento, Cancelar
            acciones_layout = self.crear_botones_accion_pendiente(pendiente)
            acciones_widget = QWidget()
            acciones_widget.setLayout(acciones_layout)
            self.pendientes_table.setCellWidget(i, 5, acciones_widget)
        
        db.close()  # Cerrar la sesión


    # Crear los botones de acción para cada pendiente
    def crear_botones_accion_pendiente(self, pendiente):
        acciones_layout = QHBoxLayout()

        btn_ver_ubicacion = QPushButton("Ver Ubicación")
        btn_ver_ubicacion.clicked.connect(self.crear_boton_ver_ubicacion(pendiente))

        btn_registrar_movimiento = QPushButton("Registrar Movimiento")
        btn_registrar_movimiento.clicked.connect(self.crear_boton_registrar_movimiento(pendiente))

        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.clicked.connect(self.crear_boton_cancelar_pendiente(pendiente))

        acciones_layout.addWidget(btn_ver_ubicacion)
        acciones_layout.addWidget(btn_registrar_movimiento)
        acciones_layout.addWidget(btn_cancelar)

        return acciones_layout

    # Función para ver ubicación del pendiente
    def crear_boton_ver_ubicacion(self, pendiente):
        return lambda: self.ver_ubicacion(pendiente)

    # Función para registrar el movimiento
    def crear_boton_registrar_movimiento(self, pendiente):
        return lambda: self.registrar_movimiento(pendiente)

    # Función para cancelar pendiente
    def crear_boton_cancelar_pendiente(self, pendiente):
        return lambda: self.cancelar_pendiente(pendiente)

    def ver_ubicacion(self, pendiente):
        QMessageBox.information(self, "Ubicación", f"Información de la ubicación: {pendiente['ubicacion']}")

    def registrar_movimiento(self, pendiente):
        db = next(get_db())
        try:
            # Crear un movimiento en base al pendiente
            movimiento = Movimiento(
                ubicacion=pendiente['ubicacion'],
                codigo=pendiente['codigo'],
                cantidad=pendiente['cantidad'],
                fecha=datetime.now(),
                nota_devolucion="Movimiento desde pendiente",
                tipo_movimiento="Egreso",
                observaciones="Se registra el movimiento desde pendiente"
            )
            db.add(movimiento)
            db.commit()

            # Luego de registrar el movimiento, eliminar el pendiente
            db.query(Pendiente).filter(Pendiente.codigo == pendiente['codigo']).delete()
            db.commit()

            QMessageBox.information(self, "Éxito", f"Movimiento registrado y pendiente eliminado: {pendiente['codigo']}")
        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Error", f"Error al registrar movimiento: {e}")
        finally:
            db.close()

    def cancelar_pendiente(self, pendiente):
        db = next(get_db())
        try:
            db.query(Pendiente).filter(Pendiente.codigo == pendiente['codigo']).delete()
            db.commit()
            QMessageBox.information(self, "Éxito", f"Pendiente cancelado: {pendiente['codigo']}")
        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Error", f"Error al cancelar pendiente: {e}")
        finally:
            db.close()
