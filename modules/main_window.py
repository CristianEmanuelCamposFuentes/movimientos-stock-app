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

        # Barra de navegación superior (actualizable con el nombre de la sección)
        nav_layout = QHBoxLayout()
        self.titulo_seccion = QLabel("Bienvenido")  # Título dinámico de la vista
        nav_layout.addWidget(self.titulo_seccion)
        nav_layout.addStretch()  # Espacio flexible para alinear el texto a la izquierda
        nav_layout.addWidget(QLabel(f"Usuario: {self.usuario}"))  # Nombre del usuario actual

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
        btn_ingresos_egresos.clicked.connect(lambda: self.mostrar_vista(self.ingresos_egresos_view, "Ingresos/Egresos"))
        btn_gestion_stock.clicked.connect(lambda: self.mostrar_vista(self.gestion_stock_view, "Gestión de Stock"))
        btn_ajustes.clicked.connect(lambda: self.mostrar_vista(self.ajustes_view, "Ajustes de Stock"))
        btn_notas_pedido.clicked.connect(lambda: self.mostrar_vista(self.notas_pedido_view, "Notas de Pedido"))
        btn_admin_productos.clicked.connect(lambda: self.mostrar_vista(self.admin_productos_view, "Administrar Productos"))
        btn_registros_movimientos.clicked.connect(lambda: self.mostrar_vista(self.registros_movimientos_view, "Registros de Movimientos"))
        btn_gestion_usuarios.clicked.connect(lambda: self.mostrar_vista(self.gestion_usuarios_view, "Gestión de Usuarios"))
        
        # Agregar botones al menú lateral
        menu_layout.addWidget(btn_ingresos_egresos)
        menu_layout.addWidget(btn_gestion_stock)
        menu_layout.addWidget(btn_ajustes)
        menu_layout.addWidget(btn_notas_pedido)
        menu_layout.addWidget(btn_admin_productos)
        menu_layout.addWidget(btn_registros_movimientos)
        menu_layout.addWidget(btn_gestion_usuarios)

        # Contenido principal (pestañas)
        self.contenido_principal = QStackedWidget()

        # Inicialización de las vistas
        self.ingresos_egresos_view = IngresosEgresosWindow(self.usuario)
        self.ajustes_view = AjustesView()
        self.gestion_stock_view = GestionStockView()
        self.notas_pedido_view = NotasPedidoView()
        self.admin_productos_view = AdminProductosView()
        self.registros_movimientos_view = RegistrosMovimientosView()
        self.gestion_usuarios_view = GestionUsuariosView(self.usuario)

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

    # Función para cambiar entre vistas y actualizar el título
    def mostrar_vista(self, vista, titulo):
        self.contenido_principal.setCurrentWidget(vista)
        self.titulo_seccion.setText(titulo)  # Actualizar el título en la barra de navegación


