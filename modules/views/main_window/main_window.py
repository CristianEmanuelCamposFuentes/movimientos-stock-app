from PyQt6.QtWidgets import QGridLayout, QWidget, QHBoxLayout, QPushButton, QStackedWidget, QLabel, QFileDialog, QMessageBox
from modules.views.ingresos_egresos.ingresos_egresos import IngresosEgresosWindow
from modules.views.ajustes.ajustes import AjustesView
from modules.views.gestion_stock.gestion_stock import GestionStockView
from modules.views.notas_pedido.notas_pedido import NotasPedidoView
from modules.views.admin_productos.admin_productos import AdminProductosView
from modules.views.registros_movimientos.registros_movimientos import RegistrosMovimientosView
from modules.views.gestion_usuarios.gestion_usuarios import GestionUsuariosView
from modules.utils.ui_styles import aplicar_estilos_barra_navegacion, aplicar_estilos_ventana_principal, aplicar_estilos_especiales
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import datetime, csv
from modules.models.database import get_db, Stock, Movimiento, Producto
from modules.models.database_operations import obtener_stock, exportar_csv
from PyQt6.uic import loadUi
class MainWindow(QWidget):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        loadUi("modules\\views\main_window\mainwindow.ui", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setWindowIcon(QIcon("modules\\views\main_window\icon.png"))
        # self.crear_eventos()

        # Inicialización de las vistas con `parent`
        self.ingresos_egresos_view = IngresosEgresosWindow(self.usuario, self)
        self.ajustes_view = AjustesView(parent=self)
        self.gestion_stock_view = GestionStockView(parent=self)
        self.notas_pedido_view = NotasPedidoView(parent=self)
        self.admin_productos_view = AdminProductosView(parent=self)
        self.registros_movimientos_view = RegistrosMovimientosView(parent=self)
        self.gestion_usuarios_view = GestionUsuariosView(parent=self)

        # # Layout principal basado en QGridLayout
        # self.grid_layout = QGridLayout()

        # # Crear el widget para la barra de navegación
        # nav_widget = QWidget()  # Crear un widget para la barra de navegación
        # nav_layout = QHBoxLayout(nav_widget)  # Aplicar el layout horizontal al widget
        # self.crear_barra_navegacion(nav_layout)  # Configurar la barra de navegación
        
        # Obtenemos el QStackedWidget desde el archivo .ui
        self.stack = self.findChild(QStackedWidget, "main_widget")

        # # Crear el contenido principal
        # self.contenido_principal = QStackedWidget()
        # self.contenido_principal.setObjectName("main-content")

        # # Añadir las vistas al QStackedWidget
        # self.contenido_principal.addWidget(self.ingresos_egresos_view)
        # self.contenido_principal.addWidget(self.ajustes_view)
        # self.contenido_principal.addWidget(self.gestion_stock_view)
        # self.contenido_principal.addWidget(self.notas_pedido_view)
        # self.contenido_principal.addWidget(self.admin_productos_view)
        # self.contenido_principal.addWidget(self.registros_movimientos_view)
        # self.contenido_principal.addWidget(self.gestion_usuarios_view)

        # Añadir navbar, contenido principal y bottom-bar al grid layout
        #self.grid_layout.addWidget(nav_widget, 0, 0, 1, 3)  # Navbar en la parte superior
        #self.grid_layout.addWidget(self.contenido_principal, 1, 0, 1, 3)  # Contenido principal
        #self.grid_layout.addLayout(self.crear_barra_botones_inferiores([]), 2, 0, 1, 3)  # Barra inferior (personalizable)

        # Aplicar el layout principal a la ventana
        self.setLayout(self.grid_layout)

    # def crear_barra_navegacion(self, layout):
    #     # Crear la barra de navegación superior con botones para cada vista
        
    #     botones = {
    #         "Ingresos/Egresos": self.mostrar_ingresos_egresos,
    #         "Gestión de Stock": self.mostrar_gestion_stock,
    #         "Notas de Pedido": self.mostrar_notas_pedido,
    #         "Administrar Productos": self.mostrar_admin_productos,
    #         "Registros de Movimientos": self.mostrar_registros_movimientos,
    #         "Gestión de Usuarios": self.mostrar_gestion_usuarios,
    #         "Ajustes de Stock": self.mostrar_ajustes
    #     }

    #     # Añadir los botones a la navbar
    #     for texto, funcion in botones.items():
    #         boton = QPushButton(texto)
    #         boton.setFixedHeight(40)
    #         boton.clicked.connect(funcion)
    #         layout.addWidget(boton)

    #     layout.addStretch()  # Alinear los botones a la izquierda
    #     layout.addWidget(QLabel(f"Bienvenido, {self.usuario}"))  # Mostrar nombre de usuario
    #     layout.setObjectName("nav-bar")

    #     aplicar_estilos_barra_navegacion(layout.parentWidget())
    #     return layout

    def crear_barra_botones_inferiores(self, personalizaciones):
        # Crear la bottom-bar personalizable según la vista
        layout = QHBoxLayout()

        botones = []
        colores = []

        for personalizacion in personalizaciones:
            boton = QPushButton(personalizacion["texto"])
            boton.setFixedHeight(40)
            boton.clicked.connect(personalizacion["funcion"])  # Conectar el evento de clic a la función
            botones.append(boton)  # Añadir el botón a la lista para aplicar estilos
            colores.append(personalizacion["color"])  # Añadir el color correspondiente

        aplicar_estilos_especiales(botones, colores)  # Aplicar los estilos personalizados a los botones

        for boton in botones:
            layout.addWidget(boton)

        return layout

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
        # Asegurarse de actualizar el título, si existe
        if hasattr(self, "titulo_seccion"):
            self.titulo_seccion.setText(titulo)
            
    def crear_eventos(self):
        self.findChild(QPushButton, "pushButton_9").clicked.connect(lambda: self.cambiar_pestana(0))  # Ingresos/Egresos
        self.findChild(QPushButton, "pushButton_10").clicked.connect(lambda: self.cambiar_pestana(1))  # Gestión de Stock
        self.findChild(QPushButton, "pushButton_11").clicked.connect(lambda: self.cambiar_pestana(2))  # Notas de Pedido
        self.findChild(QPushButton, "pushButton_12").clicked.connect(lambda: self.cambiar_pestana(3))  # Productos
        self.findChild(QPushButton, "pushButton_13").clicked.connect(lambda: self.cambiar_pestana(4))  # Movimientos
        self.findChild(QPushButton, "pushButton_14").clicked.connect(lambda: self.cambiar_pestana(5))  # Usuarios
        self.findChild(QPushButton, "pushButton_15").clicked.connect(lambda: self.cambiar_pestana(6))  # Ajustes

    def cambiar_pestana(self, indice):
        """
        Cambia la pestaña activa en el QTabWidget 'main_widget' según el índice dado.
        """
        self.main_widget.setCurrentIndex(indice)
        
            # Limpiar la barra inferior
        bottom_layout = self.findChild(QHBoxLayout, "bottom_bar_layout")
        while bottom_layout.count():
            item = bottom_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Actualizar los botones según la vista seleccionada
        if indice == 0:  # Ingresos/Egresos
            botones_personalizados = [
                {"texto": "Guardar Ingreso", "funcion": self.guardar_ingreso, "color": "green"},
                {"texto": "Cancelar", "funcion": self.cancelar_ingreso, "color": "red"}
            ]
        elif indice == 1:  # Gestión de Stock
            botones_personalizados = [
                {"texto": "Exportar CSV", "funcion": self.hacer_backup_stock, "color": "blue"}
            ]
        # ... Agrega botones para cada pestaña según sea necesario.

        # Añadir los botones personalizados a la barra inferior
        barra_inferior = self.crear_barra_botones_inferiores(botones_personalizados)
        bottom_layout.addLayout(barra_inferior)
        
    def actualizar_barra_inferior(self, personalizaciones):
        """
        Actualiza los botones de la barra inferior en función de la vista seleccionada.
        """
        # Limpiar el layout actual
        for i in reversed(range(self.bottombar_widget.layout().count())):
            widget_to_remove = self.bottombar_widget.layout().itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.deleteLater()
        
        # Crear nuevos botones basados en las personalizaciones de la vista actual
        layout = QHBoxLayout(self.bottombar_widget)
        botones = []
        colores = []
        
        for personalizacion in personalizaciones:
            boton = QPushButton(personalizacion["texto"])
            boton.setFixedHeight(40)
            boton.clicked.connect(personalizacion["funcion"])
            botones.append(boton)
            colores.append(personalizacion["color"])
        
        aplicar_estilos_especiales(botones, colores)
        
        for boton in botones:
            layout.addWidget(boton)

        self.bottombar_widget.setLayout(layout)
    
    
                
    # Función para hacer un backup del stock actual
    def hacer_backup_stock(self):
        backup_path = f"backup_stock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            db = next(get_db())
            stock = obtener_stock(db)
            exportar_csv(stock, backup_path)
            QMessageBox.information(self, "Backup exitoso", f"Respaldo creado en: {backup_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear el backup: {e}")
        finally:
            db.close()   

    def cargar_datos_csv(self,csv_file, backup_file):
        """Carga datos desde un archivo CSV a la base de datos y realiza un backup."""
        db = next(get_db())
        try:
            # Realizar un backup de la tabla Stock antes de sobrescribir
            stock_actual = db.query(Stock).all()
            with open(backup_file, mode='w', newline='', encoding='utf-8') as backup:
                writer = csv.writer(backup)
                writer.writerow(['Ubicación', 'Código', 'Cantidad', 'Fecha'])
                for stock in stock_actual:
                    writer.writerow([stock.ubicacion, stock.codigo, stock.cantidad, stock.fecha])

            # Limpiar la tabla Stock antes de cargar los nuevos datos
            db.query(Stock).delete()
            
            # Leer y cargar datos del nuevo archivo CSV
            with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Obtener la información del CSV
                    codigo = row['CODIGO']
                    descripcion = row['DESCRIPCION']
                    ubicacion = row['UBICACION']
                    cantidad = float(row['CANTIDAD'])
                    fecha = row['FECHA']
                    
                    # Verificar si el producto ya existe
                    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
                    if not producto:
                        # Si el producto no existe, agregarlo
                        producto = Producto(codigo=codigo, descripcion=descripcion)
                        db.add(producto)
                        db.commit()
                    
                    # Crear una nueva instancia de Stock
                    nuevo_stock = Stock(
                        ubicacion=ubicacion,
                        codigo=codigo,
                        cantidad=cantidad,
                        fecha=fecha,
                        id_producto=producto.id_producto
                    )
                    db.add(nuevo_stock)
            
            db.commit()
            print("Datos cargados y respaldados exitosamente.")
        except Exception as e:
            db.rollback()
            print(f"Error al cargar datos desde el CSV: {e}")
        finally:
            db.close()                         
    
    def obtener_stock(self):
        """Obtiene todos los registros de stock actual de la base de datos."""
        try:
            stock = self.query(Stock).all()
            return stock
        except Exception as e:
            print(f"Error al obtener stock: {e}")
            return []  
        
    # Función para cargar un archivo CSV y reemplazar el stock en la base de datos
    def cargar_csv_stock(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        csv_file, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "Archivos CSV (*.csv)", options=options)
        
        if csv_file:
            confirmacion = QMessageBox.question(
                self, "Confirmar carga de CSV",
                "Esto sobrescribirá todo el stock actual. ¿Estás seguro?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if confirmacion == QMessageBox.Yes:
                # Realizar un backup antes de sobrescribir
                backup_path = f"backup_stock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                self.cargar_datos_csv(csv_file, backup_path)
                QMessageBox.information(self, "Éxito", f"Datos cargados y respaldo creado en: {backup_path}")
            else:
                QMessageBox.information(self, "Cancelado", "La acción fue cancelada.")          