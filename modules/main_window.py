from PyQt5.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QFormLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from modules.stock_manager import abrir_ingresos_egresos, abrir_gestion_stock, abrir_registros_movimientos, abrir_admin_productos
from modules.pedidos import abrir_nota_pedido
from modules.usuarios import abrir_gestion_usuarios
from modules.ui_functions import aplicar_estilos
from modules.form import Form

class MainWindow(QWidget):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon('img/deposito.png'))

        # Layout principal (vertical)
        main_layout = QVBoxLayout()

        # Barra de navegación (horizontal)
        nav_bar = QHBoxLayout()
        search_label = QLabel("Buscar:")
        search_input = QLineEdit()
        user_section = QLabel(f"Bienvenido, {self.usuario}")
        nav_bar.addWidget(search_label)
        nav_bar.addWidget(search_input)
        nav_bar.addStretch()
        nav_bar.addWidget(user_section)

        # Menú lateral (vertical)
        menu_layout = QVBoxLayout()
        btn_ingresos = QPushButton("Ingresos/Egresos")
        btn_gestion_stock = QPushButton("Gestión de Stock")
        btn_nota_pedido = QPushButton("Generar Nota de Pedido")
        btn_admin_productos = QPushButton("Administrar Productos")
        btn_registros_movimientos = QPushButton("Registros de Movimientos")
        btn_usuarios = QPushButton("Gestión de Usuarios")

        # Agregar iconos (asegúrate de tener las imágenes en la carpeta 'img')
        btn_ingresos.setIcon(QIcon('img/icono_ingresos.png'))
        btn_gestion_stock.setIcon(QIcon('img/icono_gestion.png'))
        btn_nota_pedido.setIcon(QIcon('img/icono_nota_pedido.png'))
        btn_admin_productos.setIcon(QIcon('img/icono_admin.png'))
        btn_registros_movimientos.setIcon(QIcon('img/icono_registros.png'))
        btn_usuarios.setIcon(QIcon('img/icono_usuarios.png')) 

        menu_layout.addWidget(btn_ingresos)
        menu_layout.addWidget(btn_gestion_stock)
        menu_layout.addWidget(btn_nota_pedido)
        menu_layout.addWidget(btn_admin_productos)
        menu_layout.addWidget(btn_registros_movimientos)
        menu_layout.addWidget(btn_usuarios)
        menu_layout.addStretch()  # Para empujar los botones hacia arriba
        
        #Crear eventos para cada boton al clickearlos
        btn_ingresos.clicked.connect(abrir_ingresos_egresos)
        btn_gestion_stock.clicked.connect(abrir_gestion_stock)
        btn_nota_pedido.clicked.connect(abrir_nota_pedido)
        btn_admin_productos.clicked.connect(abrir_admin_productos)
        btn_registros_movimientos.clicked.connect(abrir_registros_movimientos)
        btn_usuarios.clicked.connect(abrir_gestion_usuarios)

        # Contenido central - Implementar Tabs
        tabs = QTabWidget()


        # Pestaña 1: Ingresos/Egresos (con tabla y formulario)
        tab1 = QWidget()
        layout1 = QHBoxLayout()
        
        # Tabla de movimientos
        table = QTableWidget(10, 5)  # Tabla con 10 filas y 5 columnas como ejemplo
        table.setHorizontalHeaderLabels(["Ubicación", "Código", "Descripción", "Cantidad", "Fecha"])

        # Formulario
        form_layout = QVBoxLayout()
        form = Form()  # Importamos el formulario de form.py y lo integramos
        form_layout.addWidget(form)
        
        layout1.addWidget(table)  # Tabla a la izquierda
        layout1.addLayout(form_layout)  # Formulario a la derecha
        tab1.setLayout(layout1)

        # Pestaña 2: Estadísticas
        tab2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Estadísticas del Depósito"))
        tab2.setLayout(layout2)

        # Pestaña 3: Análisis de Datos
        tab3 = QWidget()
        layout3 = QVBoxLayout()
        layout3.addWidget(QLabel("Análisis de Datos"))
        tab3.setLayout(layout3)

        # Agregar pestañas al QTabWidget
        tabs.addTab(tab1, "Ingresos/Egresos")
        tabs.addTab(tab2, "Estadísticas")
        tabs.addTab(tab3, "Análisis")

        # Agregar el menú lateral y las pestañas al layout principal
        content_layout = QHBoxLayout()
        content_layout.addLayout(menu_layout)  # Menú lateral
        content_layout.addWidget(tabs)         # Contenido principal (pestañas)

        # Agregar barra de navegación y contenido al layout principal
        main_layout.addLayout(nav_bar)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)
        
        # Aplicar estilos
        aplicar_estilos([btn_ingresos, btn_gestion_stock, btn_nota_pedido, btn_admin_productos, btn_registros_movimientos, btn_usuarios])

        
