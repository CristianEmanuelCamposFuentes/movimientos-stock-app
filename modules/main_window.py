from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel
from modules.ingresos_egresos import IngresosEgresosWindow
from modules.ajustes import AjustesView
from modules.gestion_stock import GestionStockView
from modules.notas_pedido import NotasPedidoView
from modules.admin_productos import AdminProductosView
from modules.registros_movimientos import RegistrosMovimientosView
from modules.gestion_usuarios import GestionUsuariosView
from modules.ui_styles import colors, aplicar_estilos_barra_navegacion, aplicar_estilos_barra_lateral, aplicar_estilos_ventana_principal, aplicar_estilos_especiales
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class MainWindow(QWidget):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.initUI()
        self.setWindowIcon(QIcon("img/icono_app.png"))

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 1200, 800)

        # Inicialización de las vistas antes de crear la barra de botones
        self.ingresos_egresos_view = IngresosEgresosWindow(self.usuario, self)
        self.ajustes_view = AjustesView()
        self.gestion_stock_view = GestionStockView()
        self.notas_pedido_view = NotasPedidoView()
        self.admin_productos_view = AdminProductosView()
        self.registros_movimientos_view = RegistrosMovimientosView()
        self.gestion_usuarios_view = GestionUsuariosView(self.usuario)

        # Layout principal
        main_layout = QVBoxLayout()

        # Crear el layout de navegación
        nav_layout = self.crear_barra_navegacion()

        # Crear el menú lateral
        menu_layout = self.crear_menu_lateral()

        # Crear el contenido principal
        self.contenido_principal = QStackedWidget()
        self.contenido_principal.setObjectName("main-content")

        # Añadir las vistas al QStackedWidget
        self.contenido_principal.addWidget(self.ingresos_egresos_view)
        self.contenido_principal.addWidget(self.ajustes_view)
        self.contenido_principal.addWidget(self.gestion_stock_view)
        self.contenido_principal.addWidget(self.notas_pedido_view)
        self.contenido_principal.addWidget(self.admin_productos_view)
        self.contenido_principal.addWidget(self.registros_movimientos_view)
        self.contenido_principal.addWidget(self.gestion_usuarios_view)

        # Crear la barra inferior de botones
        bottom_layout = self.crear_barra_botones_inferiores()

        # Crear el layout horizontal para el menú lateral y contenido principal
        content_layout = QHBoxLayout()
        content_layout.addLayout(menu_layout)  # Agregar el menú lateral
        content_layout.addWidget(self.contenido_principal)  # Agregar el área de contenido principal

        # Agregar todo al layout principal
        main_layout.addLayout(nav_layout)  # Barra de navegación
        #main_layout.addStretch()
        main_layout.addLayout(content_layout)  # Contenido principal
        main_layout.addLayout(bottom_layout)  # Barra inferior de botones

        # Aplicar el layout principal a la ventana
        self.setLayout(main_layout)

    def crear_barra_navegacion(self):
        # Crear la barra de navegación superior
        nav_layout = QHBoxLayout()
        self.titulo_seccion = QLabel("Bienvenido")
        self.titulo_seccion.setObjectName("nav-bar")
        nav_layout.addWidget(self.titulo_seccion)
        nav_layout.addStretch()  # Alinear el texto a la izquierda
        nav_layout.addWidget(QLabel(f"Usuario: {self.usuario}"))
        nav_layout.setObjectName("nav-bar")

        # Aplicar estilos
        aplicar_estilos_barra_navegacion(nav_layout)

        return nav_layout

    def crear_menu_lateral(self):
        # Crear el menú lateral con botones
        menu_layout = QVBoxLayout()
        
        botones = {
            "Ingresos/Egresos": self.mostrar_ingresos_egresos,
            "Gestión de Stock": self.mostrar_gestion_stock,
            "Notas de Pedido": self.mostrar_notas_pedido,
            "Administrar Productos": self.mostrar_admin_productos,
            "Registros de Movimientos": self.mostrar_registros_movimientos,
            "Gestión de Usuarios": self.mostrar_gestion_usuarios,
            "Ajustes de Stock": self.mostrar_ajustes
        }

        # Lista de botones para aplicar los estilos
        botones_widgets = []

        for texto, funcion in botones.items():
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            menu_layout.addWidget(boton)
            botones_widgets.append(boton)

        # Aplicar los estilos al menú lateral
        aplicar_estilos_barra_lateral(botones_widgets)
        
                # Crear un contenedor para el menú
        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)
            # Aplicar fondo a la barra lateral
        menu_widget.setStyleSheet(f"background-color: {colors['alge']};")

        return menu_widget

    def crear_barra_botones_inferiores(self):
        bottom_layout = QHBoxLayout()

        # Botón para cargar Ingreso
        btn_cargar_ingreso = QPushButton("Cargar Ingreso")
        btn_cargar_ingreso.setObjectName("btn-cargar-ingreso")  # Asignar un nombre de objeto para personalizar el estilo
        # En lugar de conectar directamente a la vista, puedes usar un evento genérico
        btn_cargar_ingreso.clicked.connect(lambda: self.mostrar_ingresos_egresos())  # Cambiar función

        # Botón para cargar Egreso
        btn_cargar_egreso = QPushButton("Cargar Egreso")
        btn_cargar_egreso.setObjectName("btn-cargar-egreso")
        btn_cargar_egreso.clicked.connect(lambda: self.mostrar_ingresos_egresos())  # Cambiar función

        # Botón para ver Consolidado
        btn_ver_consolidado = QPushButton("Ver Consolidado")
        btn_ver_consolidado.setObjectName("btn-ver-consolidado")
        btn_ver_consolidado.clicked.connect(lambda: self.mostrar_gestion_stock())  # Cambiar función

        # Botón para mover Pallet
        btn_mover_pallet = QPushButton("Mover Pallet")
        btn_mover_pallet.setObjectName("btn-mover-pallet")
        btn_mover_pallet.clicked.connect(lambda: self.mostrar_gestion_stock())  # Cambiar función

        # Añadir botones al layout inferior
        bottom_layout.addWidget(btn_cargar_ingreso)
        bottom_layout.addWidget(btn_cargar_egreso)
        bottom_layout.addWidget(btn_ver_consolidado)
        bottom_layout.addWidget(btn_mover_pallet)

        # Aplicar estilos especiales a los botones
        botones = [btn_cargar_ingreso, btn_cargar_egreso, btn_ver_consolidado, btn_mover_pallet]
        colores = ["grass", "salmon", "snow", "snow"]  # Definir colores específicos para cada botón
        aplicar_estilos_especiales(botones, colores)

        return bottom_layout

    # Funciones para mostrar cada vista
    def mostrar_ingresos_egresos(self):
        self.mostrar_vista(self.ingresos_egresos_view, "Ingresos/Egresos")

    def mostrar_gestion_stock(self):
        self.mostrar_vista(self.gestion_stock_view, "Gestión de Stock")

    def mostrar_notas_pedido(self):
        self.mostrar_vista(self.notas_pedido_view, "Notas de Pedido")

    def mostrar_admin_productos(self):
        self.mostrar_vista(self.admin_productos_view, "Administrar Productos")

    def mostrar_registros_movimientos(self):
        self.mostrar_vista(self.registros_movimientos_view, "Registros de Movimientos")

    def mostrar_gestion_usuarios(self):
        self.mostrar_vista(self.gestion_usuarios_view, "Gestión de Usuarios")

    def mostrar_ajustes(self):
        self.mostrar_vista(self.ajustes_view, "Ajustes de Stock")

    # Función para cambiar entre vistas y actualizar el título
    def mostrar_vista(self, vista, titulo):
        self.contenido_principal.setCurrentWidget(vista)
        self.titulo_seccion.setText(titulo)  # Actualizar el título en la barra de navegación
