from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel
from PyQt6.QtCore import Qt
from sqlalchemy.orm import Session
from modules.models.database import get_db, Stock, Movimiento
from datetime import datetime
from modules.utils.ui_styles import aplicar_estilos_especiales


class AjustesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Referencia a la ventana principal
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ajustes de Stock")

        # Layout principal
        main_layout = QVBoxLayout()

        # Barra de búsqueda
        search_layout = QHBoxLayout()
        search_label = QLabel("Buscar:")
        self.search_input = QLineEdit()
        btn_buscar = QPushButton("Buscar")
        btn_buscar.clicked.connect(self.buscar_stock)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(btn_buscar)

        # Tabla de stock ajustable
        self.stock_table = QTableWidget()
        self.stock_table.setColumnCount(5)
        self.stock_table.setHorizontalHeaderLabels(["Ubicación", "Código", "Descripción", "Cantidad", "Fecha"])
        self.cargar_stock()

        # Agregar todos los layouts al layout principal
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.stock_table)

                # Crear la barra de botones inferior
        if self.parent:  # Verificar si el padre está disponible
            botones = [
                {"texto": "Cargar CSV", "color": "snow", "funcion": self.parent.cargar_csv_stock},
                {"texto": "Backup Stock", "color": "snow", "funcion": self.parent.hacer_backup_stock}
            ]
            bottom_bar = self.parent.crear_barra_botones_inferiores(botones)
            main_layout.addLayout(bottom_bar)

        self.setLayout(main_layout)

    def cargar_stock(self):
        """Cargar los datos del stock en la tabla para ajustes"""
        db = next(get_db())
        stock_items = db.query(Stock).all()

        self.stock_table.setRowCount(len(stock_items))
        for row_num, item in enumerate(stock_items):
            self.stock_table.setItem(row_num, 0, QTableWidgetItem(item.ubicacion))
            self.stock_table.setItem(row_num, 1, QTableWidgetItem(item.codigo))
            self.stock_table.setItem(row_num, 2, QTableWidgetItem(item.descripcion))
            cantidad_item = QTableWidgetItem(str(item.cantidad))
            cantidad_item.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)  # Editable
            self.stock_table.setItem(row_num, 3, cantidad_item)
            fecha_item = QTableWidgetItem(item.fecha.strftime("%d/%m/%Y"))
            fecha_item.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)  # Editable
            self.stock_table.setItem(row_num, 4, fecha_item)

    def buscar_stock(self):
        """Buscar stock para ajustes"""
        search_term = self.search_input.text()
        # Aquí puedes agregar la lógica para filtrar los productos
        print(f"Buscando: {search_term}")

    def guardar_ajustes(self):
        """Guardar los ajustes realizados al stock"""
        db = next(get_db())
        try:
            for row in range(self.stock_table.rowCount()):
                ubicacion = self.stock_table.item(row, 0).text()
                codigo = self.stock_table.item(row, 1).text()
                cantidad = float(self.stock_table.item(row, 3).text())
                fecha = datetime.strptime(self.stock_table.item(row, 4).text(), "%d/%m/%Y")

                # Actualizar la base de datos
                stock_item = db.query(Stock).filter(Stock.ubicacion == ubicacion, Stock.codigo == codigo).first()
                if stock_item:
                    stock_item.cantidad = cantidad
                    stock_item.fecha = fecha

                    # Registrar el ajuste en la tabla de movimientos
                    movimiento = Movimiento(
                        ubicacion=ubicacion,
                        codigo=codigo,
                        cantidad=cantidad,
                        fecha=fecha,
                        nota_devolucion="Ajuste de Stock",
                        tipo_movimiento="Ajuste",
                        observaciones="Ajuste manual desde la vista de ajustes"
                    )
                    db.add(movimiento)

            db.commit()
            print("Ajustes guardados exitosamente")

        except Exception as e:
            db.rollback()
            print(f"Error al guardar ajustes: {e}")

        finally:
            db.close()
