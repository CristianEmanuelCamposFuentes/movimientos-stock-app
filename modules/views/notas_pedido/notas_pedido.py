from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QTableWidget, QTableWidgetItem, QTabWidget, QComboBox, QTextEdit
from modules.models.database_operations import generar_nota_pedido, cargar_nota_pedido, obtener_registros_notas
from modules.models.database import get_db, Movimiento, Stock, Producto
from datetime import datetime

class NotasPedidoView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Referencia al contenedor principal
        self.stack = stack
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notas de Pedido")
        layout = QVBoxLayout()

        # Crear las pestañas
        self.tabs = QTabWidget()
        self.tabs.addTab(self.generar_nota_tab(), "Generar Nota")
        self.tabs.addTab(self.cargar_nota_tab(), "Cargar Nota")
        self.tabs.addTab(self.registros_tab(), "Registros")

        # Conectar la actualización de la barra inferior cuando cambie la pestaña
        self.tabs.currentChanged.connect(self.on_tab_changed)

        # Agregar las pestañas al layout principal
        layout.addWidget(self.tabs)

        self.setLayout(layout)

        # Inicializar la barra inferior para la primera pestaña
        self.on_tab_changed(0)

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

        layout.addLayout(form_layout)

        widget.setLayout(layout)
        return widget

    # Función para generar la nota de pedido
    def generar_nota(self):
        codigo = self.codigo_input.text()
        cantidad = self.cantidad_input.text()

        # Buscar la descripción del producto en la base de datos
        db = next(get_db())
        try:
            producto = db.query(Producto).filter(Producto.codigo == codigo).first()

            if producto:
                descripcion = producto.descripcion
                self.descripcion_output.setText(descripcion)
                generar_nota_pedido(db, codigo, descripcion, float(cantidad), datetime.now().strftime("%d/%m/%Y"))
                print("Nota de pedido generada con éxito")
            else:
                self.descripcion_output.setText("Producto no encontrado")
                print("Error: Producto no encontrado")
        except Exception as e:
            print(f"Error al generar la nota de pedido: {e}")
        finally:
            db.close()

    # Pestaña 2: Cargar Notas de Pedido
    def cargar_nota_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        # Campos del formulario
        self.numero_nota_input = QLineEdit()
        form_layout.addRow("Número de Nota:", self.numero_nota_input)

        # Tabla para mostrar los códigos, cantidades, ubicaciones y checkboxes
        self.nota_table = QTableWidget(0, 4)
        self.nota_table.setHorizontalHeaderLabels(["Código", "Cantidad", "Ubicación", "Cantidad para descontar"])
        layout.addLayout(form_layout)
        layout.addWidget(self.nota_table)

        widget.setLayout(layout)
        return widget

    # Función para buscar la nota e insertar los datos en la tabla
    def buscar_nota(self):
        numero_nota = self.numero_nota_input.text()
        db = next(get_db())  # Obtener la sesión de la base de datos
        try:
            nota = cargar_nota_pedido(db, numero_nota)  # Cargar los datos de la nota

            self.nota_table.setRowCount(0)

            # Recorrer cada código y mostrar sus ubicaciones y cantidades en la tabla
            for i, item in enumerate(nota):
                self.nota_table.insertRow(i)
                self.nota_table.setItem(i, 0, QTableWidgetItem(item.codigo))
                self.nota_table.setItem(i, 1, QTableWidgetItem(str(item.cantidad)))

                # Cargar las ubicaciones en cada fila
                ubicaciones = self.obtener_ubicaciones_por_codigo(item.codigo)
                ubicacion_combo = QComboBox()
                ubicacion_combo.addItems([ub.ubicacion for ub in ubicaciones])
                self.nota_table.setCellWidget(i, 2, ubicacion_combo)

                # Cantidad a descontar, editable
                cantidad_descuento = QLineEdit()
                cantidad_descuento.setPlaceholderText("0")
                self.nota_table.setCellWidget(i, 3, cantidad_descuento)
        except Exception as e:
            print(f"Error al buscar la nota: {e}")
        finally:
            db.close()

    # Pestaña 3: Registros de Notas de Pedido
    def registros_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Tabla para mostrar los registros de notas de pedido
        self.registros_table = QTableWidget(0, 5)
        self.registros_table.setHorizontalHeaderLabels(["Número de Nota", "Código", "Cantidad", "Ubicación", "Fecha"])
        layout.addWidget(self.registros_table)

        # Buscar registros de notas de pedido
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
        db = next(get_db())
        try:
            resultados = obtener_registros_notas(db, filtro)
            self.registros_table.setRowCount(0)
            for i, item in enumerate(resultados):
                self.registros_table.insertRow(i)
                self.registros_table.setItem(i, 0, QTableWidgetItem(item.numero_nota))
                self.registros_table.setItem(i, 1, QTableWidgetItem(item.codigo))
                self.registros_table.setItem(i, 2, QTableWidgetItem(str(item.cantidad)))
                self.registros_table.setItem(i, 3, QTableWidgetItem(item.ubicacion))
                self.registros_table.setItem(i, 4, QTableWidgetItem(item.fecha.strftime('%d/%m/%Y')))
        except Exception as e:
            print(f"Error al buscar registros: {e}")
        finally:
            db.close()

    # Evento que se llama cuando se cambia de pestaña
    def on_tab_changed(self, index):
        if index == 0:  # Pestaña Generar Nota
            botones_personalizados = [
                {"texto": "Generar Nota", "funcion": self.generar_nota, "color": "grass"}
            ]
        elif index == 1:  # Pestaña Cargar Nota
            botones_personalizados = [
                {"texto": "Buscar Nota", "funcion": self.buscar_nota, "color": "blue"},
                {"texto": "Guardar Nota", "funcion": self.guardar_nota_actualizada, "color": "green"}
            ]
        elif index == 2:  # Pestaña Registros
            botones_personalizados = [
                {"texto": "Buscar Registros", "funcion": self.buscar_registros, "color": "alge"}
            ]

        # Actualizar la barra inferior en la ventana principal
        self.parent.actualizar_barra_inferior(botones_personalizados)

    # Función para guardar la nota actualizada
    def guardar_nota_actualizada(self):
        db = next(get_db())
        try:
            for row in range(self.nota_table.rowCount()):
                codigo = self.nota_table.item(row, 0).text()
                ubicacion = self.nota_table.cellWidget(row, 2).currentText()  # Ubicación seleccionada
                cantidad_descuento = self.nota_table.cellWidget(row, 3).text()

                # Validar si la cantidad está en 0 o si hay que descontar
                if cantidad_descuento and float(cantidad_descuento) > 0:
                    # Registrar el descuento de stock
                    self.registrar_descuento(db, codigo, ubicacion, float(cantidad_descuento))
            db.commit()
            print("Nota de pedido actualizada con éxito")
        except Exception as e:
            print(f"Error al guardar la nota actualizada: {e}")
        finally:
            db.close()

    # Función para obtener ubicaciones por código
    def obtener_ubicaciones_por_codigo(self, codigo):
        db = next(get_db())  # Abrir la sesión de la base de datos
        ubicaciones = db.query(Stock).filter(Stock.codigo == codigo).all()
        return ubicaciones  # Retornar las ubicaciones relacionadas con el código        



