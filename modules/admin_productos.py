from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QTabWidget, QDialog, QLabel, QFileDialog
from modules.database_operations import agregar_producto, obtener_productos, editar_producto, eliminar_producto
from modules.database import get_db

class AdminProductosView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Administrar Productos")
        layout = QVBoxLayout()

        # Crear las pestañas
        tabs = QTabWidget()
        tabs.addTab(self.tabla_productos_tab(), "Tabla Actual")
        tabs.addTab(self.clasificaciones_tab(), "Clasificaciones")
        tabs.addTab(self.imagenes_tab(), "Imágenes de Productos")

        # Agregar pestañas al layout principal
        layout.addWidget(tabs)
        self.setLayout(layout)

    # Pestaña 1: Tabla Actual de Productos
    def tabla_productos_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Tabla de productos
        self.productos_table = QTableWidget(0, 4)
        self.productos_table.setHorizontalHeaderLabels(["Código", "Descripción", "Categoría", "Acciones"])
        layout.addWidget(self.productos_table)

        # Cargar productos en la tabla
        self.cargar_productos()

        # Botones para CRUD
        btn_agregar = QPushButton("Agregar Producto")
        btn_agregar.clicked.connect(self.abrir_agregar_producto)

        layout.addWidget(btn_agregar)
        widget.setLayout(layout)
        return widget

    # Función para cargar productos en la tabla
    def cargar_productos(self):
        db = next(get_db())  # Obtener la sesión de la base de datos
        productos = obtener_productos(db)  # Obtener los productos de la base de datos
        self.productos_table.setRowCount(0)
        for i, producto in enumerate(productos):
            self.productos_table.insertRow(i)
            self.productos_table.setItem(i, 0, QTableWidgetItem(producto.codigo))
            self.productos_table.setItem(i, 1, QTableWidgetItem(producto.descripcion))
            self.productos_table.setItem(i, 2, QTableWidgetItem(producto.categoria))

            # Botones de editar y eliminar
            btn_editar = QPushButton("Editar")
            btn_editar.clicked.connect(lambda _, p=producto: self.abrir_editar_producto(p))

            btn_eliminar = QPushButton("Eliminar")
            btn_eliminar.clicked.connect(lambda _, p=producto: self.eliminar_producto(p))

            acciones_layout = QHBoxLayout()
            acciones_layout.addWidget(btn_editar)
            acciones_layout.addWidget(btn_eliminar)

            acciones_widget = QWidget()
            acciones_widget.setLayout(acciones_layout)
            self.productos_table.setCellWidget(i, 3, acciones_widget)

    # Función para abrir el diálogo de agregar producto
    def abrir_agregar_producto(self):
        dialog = ProductoDialog()
        if dialog.exec_():
            nuevo_producto = dialog.get_data()
            db = next(get_db())  # Obtener la sesión de la base de datos
            agregar_producto(db, nuevo_producto["codigo"], nuevo_producto["descripcion"], nuevo_producto["categoria"])
            self.cargar_productos()

    # Función para abrir el diálogo de editar producto
    def abrir_editar_producto(self, producto):
        dialog = ProductoDialog(producto)
        if dialog.exec_():
            producto_actualizado = dialog.get_data()
            db = next(get_db())  # Obtener la sesión de la base de datos
            editar_producto(db, producto.id_producto, producto_actualizado)
            self.cargar_productos()

    # Función para eliminar producto
    def eliminar_producto(self, producto):
        db = next(get_db())  # Obtener la sesión de la base de datos
        eliminar_producto(db, producto.id_producto)
        self.cargar_productos()

    # Pestaña 2: Clasificaciones de Productos
    def clasificaciones_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Aquí se podrían agregar clasificaciones de productos
        layout.addWidget(QLabel("Clasificaciones de Productos"))

        widget.setLayout(layout)
        return widget

    # Pestaña 3: Gestión de Imágenes de Productos
    def imagenes_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Aquí se gestionan las imágenes de los productos
        layout.addWidget(QLabel("Gestión de Imágenes de Productos"))

        # Botón para cargar imagen
        btn_cargar_imagen = QPushButton("Cargar Imagen")
        btn_cargar_imagen.clicked.connect(self.cargar_imagen)

        layout.addWidget(btn_cargar_imagen)
        widget.setLayout(layout)
        return widget

    # Función para cargar una imagen
    def cargar_imagen(self):
        imagen_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg)")
        if imagen_path:
            print(f"Imagen seleccionada: {imagen_path}")

# Diálogo para agregar/editar producto
class ProductoDialog(QDialog):
    def __init__(self, producto=None):
        super().__init__()
        self.producto = producto
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Agregar/Editar Producto")
        layout = QFormLayout()

        self.codigo_input = QLineEdit()
        self.descripcion_input = QLineEdit()
        self.categoria_input = QLineEdit()

        if self.producto:
            self.codigo_input.setText(self.producto.codigo)
            self.descripcion_input.setText(self.producto.descripcion)
            self.categoria_input.setText(self.producto.categoria)

        layout.addRow("Código:", self.codigo_input)
        layout.addRow("Descripción:", self.descripcion_input)
        layout.addRow("Categoría:", self.categoria_input)

        # Botones de Aceptar/Cancelar
        botones_layout = QHBoxLayout()
        btn_aceptar = QPushButton("Aceptar")
        btn_aceptar.clicked.connect(self.accept)
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.clicked.connect(self.reject)

        botones_layout.addWidget(btn_aceptar)
        botones_layout.addWidget(btn_cancelar)

        layout.addRow(botones_layout)

        self.setLayout(layout)

    def get_data(self):
        return {
            "codigo": self.codigo_input.text(),
            "descripcion": self.descripcion_input.text(),
            "categoria": self.categoria_input.text()
        }

