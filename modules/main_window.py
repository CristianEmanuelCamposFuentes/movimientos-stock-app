from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel
from modules.ingresos_egresos import IngresosEgresosWindow
from modules.ajustes import AjustesView
from modules.gestion_stock import GestionStockView
from modules.notas_pedido import NotasPedidoView
from modules.admin_productos import AdminProductosView
from modules.registros_movimientos import RegistrosMovimientosView
from modules.gestion_usuarios import GestionUsuariosView

class MainWindow(QWidget):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 1200, 800)

        # Layout principal
        main_layout = QVBoxLayout()

        # Barra de navegación superior
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QLabel(f"Bienvenido, {self.usuario}"))  # Mostrar nombre de usuario
        nav_layout.addStretch()  # Espacio flexible para alinear el texto

        # Menú lateral (botones)
        menu_layout = QVBoxLayout()
        btn_ingresos_egresos = QPushButton("Ingresos/Egresos")
        btn_gestion_stock = QPushButton("Gestión de Stock")
        btn_notas_pedido = QPushButton("Notas de Pedido")
        btn_admin_productos = QPushButton("Administrar Productos")
        btn_registros_movimientos = QPushButton("Registros de Movimientos")
        btn_gestion_usuarios = QPushButton("Gestión de Usuarios")
        btn_ajustes = QPushButton("Ajustes de Stock")

        # Conectar botones a funciones
        btn_ingresos_egresos.clicked.connect(self.mostrar_ingresos_egresos)
        btn_gestion_stock.clicked.connect(self.mostrar_gestion_stock)
        btn_notas_pedido.clicked.connect(self.mostrar_notas_pedido)
        btn_admin_productos.clicked.connect(self.mostrar_admin_productos)
        btn_registros_movimientos.clicked.connect(self.mostrar_registros_movimientos)
        btn_gestion_usuarios.clicked.connect(self.mostrar_gestion_usuarios)
        btn_ajustes.clicked.connect(self.mostrar_ajustes)

        # Agregar botones al menú lateral
        menu_layout.addWidget(btn_ingresos_egresos)
        menu_layout.addWidget(btn_gestion_stock)
        menu_layout.addWidget(btn_notas_pedido)
        menu_layout.addWidget(btn_admin_productos)
        menu_layout.addWidget(btn_registros_movimientos)
        menu_layout.addWidget(btn_gestion_usuarios)
        menu_layout.addWidget(btn_ajustes)

        # Contenido principal (pestañas)
        self.contenido_principal = QStackedWidget()

        # Inicialización de las vistas
        self.ingresos_egresos_view = IngresosEgresosWindow(self.usuario)
        self.ajustes_view = AjustesView()
        self.gestion_stock_view = GestionStockView()
        self.notas_pedido_view = NotasPedidoView()
        self.admin_productos_view = AdminProductosView()
        self.registros_movimientos_view = RegistrosMovimientosView()
        self.gestion_usuarios_view = GestionUsuariosView()

        # Añadir las vistas al QStackedWidget
        self.contenido_principal.addWidget(self.ingresos_egresos_view)
        self.contenido_principal.addWidget(self.ajustes_view)
        self.contenido_principal.addWidget(self.gestion_stock_view)
        self.contenido_principal.addWidget(self.notas_pedido_view)
        self.contenido_principal.addWidget(self.admin_productos_view)
        self.contenido_principal.addWidget(self.registros_movimientos_view)
        self.contenido_principal.addWidget(self.gestion_usuarios_view)

        # Agregar el layout del menú y el contenido principal
        content_layout = QHBoxLayout()
        content_layout.addLayout(menu_layout)  # Menú lateral
        content_layout.addWidget(self.contenido_principal)  # Vistas principales

        # Agregar la barra de navegación y el contenido al layout principal
        main_layout.addLayout(nav_layout)
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    # Funciones para cambiar entre vistas
    def mostrar_ingresos_egresos(self):
        self.contenido_principal.setCurrentWidget(self.ingresos_egresos_view)

    def mostrar_gestion_stock(self):
        self.contenido_principal.setCurrentWidget(self.gestion_stock_view)

    def mostrar_notas_pedido(self):
        self.contenido_principal.setCurrentWidget(self.notas_pedido_view)

    def mostrar_admin_productos(self):
        self.contenido_principal.setCurrentWidget(self.admin_productos_view)

    def mostrar_registros_movimientos(self):
        self.contenido_principal.setCurrentWidget(self.registros_movimientos_view)

    def mostrar_gestion_usuarios(self):
        self.contenido_principal.setCurrentWidget(self.gestion_usuarios_view)

    def mostrar_ajustes(self):
        self.contenido_principal.setCurrentWidget(self.ajustes_view)

