from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QTabWidget, QFileDialog, QMessageBox
from modules.database_operations import obtener_movimientos_historicos, obtener_movimientos_pendientes, generar_pdf, exportar_csv
from modules.database import get_db, Movimiento, Pendiente

class RegistrosMovimientosView(QWidget):
    def __init__(self):
        super().__init__()
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
        self.historico_table.setHorizontalHeaderLabels(["Ubicación", "Código", "Cantidad", "Fecha", "Nota/Devolución", "Observaciones"])
        layout.addWidget(self.historico_table)

        # Cargar registros históricos
        self.cargar_registros_historicos()

        # Botones para exportar e imprimir
        btn_exportar_pdf = QPushButton("Exportar a PDF")
        btn_exportar_pdf.clicked.connect(self.exportar_pdf)

        btn_exportar_csv = QPushButton("Exportar a CSV")
        btn_exportar_csv.clicked.connect(self.exportar_csv)

        btn_filtrar = QPushButton("Filtrar")
        btn_filtrar.clicked.connect(self.filtrar_registros)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(btn_exportar_pdf)
        botones_layout.addWidget(btn_exportar_csv)
        botones_layout.addWidget(btn_filtrar)

        layout.addLayout(botones_layout)
        widget.setLayout(layout)
        return widget

    # Función para cargar los registros históricos
    def cargar_registros_historicos(self):
        movimientos = obtener_movimientos_historicos()  # Función simulada para obtener los movimientos históricos
        self.historico_table.setRowCount(0)
        for i, movimiento in enumerate(movimientos):
            self.historico_table.insertRow(i)
            self.historico_table.setItem(i, 0, QTableWidgetItem(movimiento["ubicacion"]))
            self.historico_table.setItem(i, 1, QTableWidgetItem(movimiento["codigo"]))
            self.historico_table.setItem(i, 2, QTableWidgetItem(str(movimiento["cantidad"])))
            self.historico_table.setItem(i, 3, QTableWidgetItem(movimiento["fecha"].strftime("%d/%m/%Y")))
            self.historico_table.setItem(i, 4, QTableWidgetItem(movimiento["nota_devolucion"]))
            self.historico_table.setItem(i, 5, QTableWidgetItem(movimiento["observaciones"]))

    # Función para exportar a PDF
    def exportar_pdf(self):
        movimientos = obtener_movimientos_historicos()  # Obtenemos los movimientos históricos
        ruta_pdf, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "", "PDF Files (*.pdf)")
        if ruta_pdf:
            generar_pdf(movimientos, ruta_pdf)  # Función simulada para generar el PDF
            QMessageBox.information(self, "Éxito", f"PDF generado en {ruta_pdf}")

    # Función para exportar a CSV
    def exportar_csv(self):
        ruta_csv, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "CSV Files (*.csv)")
        if ruta_csv:
            exportar_csv(ruta_csv)  # Función simulada para exportar los datos a CSV
            QMessageBox.information(self, "Éxito", f"CSV generado en {ruta_csv}")

    # Función para filtrar registros (Placeholder)
    def filtrar_registros(self):
        QMessageBox.information(self, "Filtrar", "Se implementará la funcionalidad de filtrado.")

    # Pestaña 2: Pendientes
    def pendientes_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Tabla para mostrar los pendientes
        self.pendientes_table = QTableWidget(0, 6)
        self.pendientes_table.setHorizontalHeaderLabels(["Ubicación", "Código", "Cantidad", "Fecha", "Motivo", "Acciones"])
        layout.addWidget(self.pendientes_table)

        # Cargar pendientes
        self.cargar_pendientes()

        # Botones para acciones en los pendientes
        layout.addLayout(self.botones_acciones_pendientes())

        widget.setLayout(layout)
        return widget

    # Función para cargar los pendientes
    def cargar_pendientes(self):
        pendientes = obtener_movimientos_pendientes()  # Función simulada para obtener los movimientos pendientes
        self.pendientes_table.setRowCount(0)
        for i, pendiente in enumerate(pendientes):
            self.pendientes_table.insertRow(i)
            self.pendientes_table.setItem(i, 0, QTableWidgetItem(pendiente["ubicacion"]))
            self.pendientes_table.setItem(i, 1, QTableWidgetItem(pendiente["codigo"]))
            self.pendientes_table.setItem(i, 2, QTableWidgetItem(str(pendiente["cantidad"])))
            self.pendientes_table.setItem(i, 3, QTableWidgetItem(pendiente["fecha"].strftime("%d/%m/%Y")))
            self.pendientes_table.setItem(i, 4, QTableWidgetItem(pendiente["motivo"]))

            # Botones de acción: Ver Ubicación, Registrar Movimiento, Cancelar
            btn_ver_ubicacion = QPushButton("Ver Ubicación")
            btn_ver_ubicacion.clicked.connect(lambda _, p=pendiente: self.ver_ubicacion(p))

            btn_registrar_movimiento = QPushButton("Registrar Movimiento")
            btn_registrar_movimiento.clicked.connect(lambda _, p=pendiente: self.registrar_movimiento(p))

            btn_cancelar = QPushButton("Cancelar")
            btn_cancelar.clicked.connect(lambda _, p=pendiente: self.cancelar_pendiente(p))

            acciones_layout = QHBoxLayout()
            acciones_layout.addWidget(btn_ver_ubicacion)
            acciones_layout.addWidget(btn_registrar_movimiento)
            acciones_layout.addWidget(btn_cancelar)

            acciones_widget = QWidget()
            acciones_widget.setLayout(acciones_layout)
            self.pendientes_table.setCellWidget(i, 5, acciones_widget)

    # Botones de acción en pendientes
    def botones_acciones_pendientes(self):
        botones_layout = QHBoxLayout()

        btn_actualizar_pendientes = QPushButton("Actualizar Pendientes")
        btn_actualizar_pendientes.clicked.connect(self.cargar_pendientes)
        botones_layout.addWidget(btn_actualizar_pendientes)

        return botones_layout

    # Función para ver ubicación del pendiente
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
