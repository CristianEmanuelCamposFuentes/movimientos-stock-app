from PyQt5.QtWidgets import QGridLayout, QWidget, QHBoxLayout, QPushButton, QStackedWidget, QLabel, QFileDialog, QMessageBox
from modules.ingresos_egresos import IngresosEgresosWindow
from modules.ajustes import AjustesView
from modules.gestion_stock import GestionStockView
from modules.notas_pedido import NotasPedidoView
from modules.admin_productos import AdminProductosView
from modules.registros_movimientos import RegistrosMovimientosView
from modules.gestion_usuarios import GestionUsuariosView
from modules.ui_styles import aplicar_estilos_barra_navegacion, aplicar_estilos_ventana_principal, aplicar_estilos_especiales
from PyQt5.QtGui import QIcon
import datetime , csv
from modules.database import get_db, Stock, Movimiento, Producto
from sqlalchemy.orm import Session

class MainWindow(QWidget):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.initUI()
        self.setWindowIcon(QIcon("img/icono_app.png"))

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 1200, 800)

        # Inicialización de las vistas con `parent`
        self.ingresos_egresos_view = IngresosEgresosWindow(self.usuario, self)
        self.ajustes_view = AjustesView(parent=self)
        self.gestion_stock_view = GestionStockView(parent=self)
        self.notas_pedido_view = NotasPedidoView(parent=self)
        self.admin_productos_view = AdminProductosView(parent=self)
        self.registros_movimientos_view = RegistrosMovimientosView(parent=self)
        self.gestion_usuarios_view = GestionUsuariosView(self.usuario, parent=self)

        # Layout principal basado en QGridLayout
        self.grid_layout = QGridLayout()

        # Crear el layout de navegación
        nav_layout = self.crear_barra_navegacion()

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

        # Añadir navbar, contenido principal y bottom-bar al grid layout
        self.grid_layout.addLayout(nav_layout, 0, 0, 1, 3)  # Navbar en la parte superior
        self.grid_layout.addWidget(self.contenido_principal, 1, 0, 1, 3)  # Contenido principal
        self.grid_layout.addLayout(self.crear_barra_botones_inferiores([]), 2, 0, 1, 3)  # Barra inferior (personalizable)

        # Aplicar el layout principal a la ventana
        self.setLayout(self.grid_layout)

    def crear_barra_navegacion(self):
        # Crear la barra de navegación superior con botones para cada vista
        nav_layout = QHBoxLayout()
        
        botones = {
            "Ingresos/Egresos": self.mostrar_ingresos_egresos,
            "Gestión de Stock": self.mostrar_gestion_stock,
            "Notas de Pedido": self.mostrar_notas_pedido,
            "Administrar Productos": self.mostrar_admin_productos,
            "Registros de Movimientos": self.mostrar_registros_movimientos,
            "Gestión de Usuarios": self.mostrar_gestion_usuarios,
            "Ajustes de Stock": self.mostrar_ajustes
        }

        # Añadir los botones a la navbar
        for texto, funcion in botones.items():
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            nav_layout.addWidget(boton)

        nav_layout.addStretch()  # Alinear los botones a la izquierda
        nav_layout.addWidget(QLabel(f"Bienvenido, {self.usuario}"))  # Mostrar nombre de usuario
        nav_layout.setObjectName("nav-bar")

        aplicar_estilos_barra_navegacion(nav_layout)
        return nav_layout

    def crear_barra_botones_inferiores(self, personalizaciones):
        # Crear la bottom-bar personalizable según la vista
        layout = QHBoxLayout()

        botones = []
        colores = []

        for personalizacion in personalizaciones:
            boton = QPushButton(personalizacion["texto"])
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

    def cargar_datos_csv(csv_file, backup_file):
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
    
    def obtener_stock(session: Session):
        """Obtiene todos los registros de stock actual de la base de datos."""
        try:
            stock = session.query(Stock).all()
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