from PyQt6.QtWidgets import QMainWindow,QHBoxLayout, QPushButton, QStackedWidget, QFileDialog, QMessageBox, QWidget
from modules.views.ingresos_egresos.ingresos_egresos import IngresosEgresosWindow
from modules.views.ajustes.ajustes import AjustesView
from modules.views.gestion_stock.gestion_stock import GestionStockView
from modules.views.notas_pedido.notas_pedido import NotasPedidoView
from modules.views.admin_productos.admin_productos import AdminProductosView
from modules.views.registros_movimientos.registros_movimientos import RegistrosMovimientosView
from modules.views.gestion_usuarios.gestion_usuarios import GestionUsuariosView
from modules.utils.ui_styles import aplicar_estilos_barra_navegacion, aplicar_estilos_ventana_principal, aplicar_estilos_especiales
from PyQt6.QtGui import QIcon
import datetime, csv
from modules.models.database import get_db, Stock, Movimiento, Producto
from modules.models.database_operations import obtener_stock, exportar_csv
from PyQt6.uic import loadUi
class MainWindow(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        loadUi("modules\\views\main_window\mainwindow.ui", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setWindowIcon(QIcon("modules\\views\main_window\icon.png"))

        # Obtenemos el QStackedWidget desde el archivo .ui
        self.stack = self.findChild(QStackedWidget, "main_widget")
        
        # Inicialización de las vistas con `parent`
        self.ingresos_egresos_page = self.stack.findChild(QWidget, "ingresos_egresos_page")
        self.ajustes_page = self.stack.findChild(QWidget, "ajustes_page")
        self.gestion_stock_page = self.stack.findChild(QWidget, "gestion_stock_page")
        self.notas_pedido_page = self.stack.findChild(QWidget, "notas_pedido_page")
        self.admin_productos_page = self.stack.findChild(QWidget, "admin_productos_page")
        self.registros_movimientos_page = self.stack.findChild(QWidget, "registros_movimientos_page")
        self.gestion_usuarios_page = self.stack.findChild(QWidget, "gestion_usuarios_page")
        
        # Inicialización de las vistas con `parent`
        self.ingresos_egresos_view = IngresosEgresosWindow(self.usuario, self)
        self.ajustes_view = AjustesView(self)
        self.gestion_stock_view = GestionStockView(self)
        self.notas_pedido_view = NotasPedidoView(self)
        self.admin_productos_view = AdminProductosView(self)
        self.registros_movimientos_view = RegistrosMovimientosView(self)
        self.gestion_usuarios_view = GestionUsuariosView(self)        
        
        # Asignar las vistas personalizadas a las páginas del QStackedWidget
        self.stack.insertWidget(0, self.ingresos_egresos_view)  # Insertar la vista personalizada
        self.stack.insertWidget(1, self.ajustes_view)
        self.stack.insertWidget(2, self.gestion_stock_view)
        self.stack.insertWidget(3, self.notas_pedido_view)
        self.stack.insertWidget(4, self.admin_productos_view)
        self.stack.insertWidget(5, self.registros_movimientos_view)
        self.stack.insertWidget(6, self.gestion_usuarios_view)

        # Configurar los eventos de los botones
        self.crear_eventos()
        #self.cambiar_pestana(0) # Ingresos/Egresos será la vista por defecto al arrancar
        
        # Llamar a la función para actualizar la barra inferior de "Ingresos/Egresos"
        #self.ingresos_egresos_view.actualizar_barra_inferior()
        self.stack.setCurrentIndex(0)  # Ingresos/Egresos será la vista por defecto al arrancar

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
        self.stack.setCurrentWidget(vista)
        # Asegurarse de actualizar el título, si existe
        if hasattr(self, "titulo_seccion"):
            self.titulo_seccion.setText(titulo)
            
    def crear_eventos(self):
        self.findChild(QPushButton, "ingresos_egresos_1").clicked.connect(lambda: self.cambiar_pestana(0))  # Ingresos/Egresos
        self.findChild(QPushButton, "gestion_stock_1").clicked.connect(lambda: self.cambiar_pestana(1))  # Gestión de Stock
        self.findChild(QPushButton, "notas_pedido_1").clicked.connect(lambda: self.cambiar_pestana(2))  # Notas de Pedido
        self.findChild(QPushButton, "productos_1").clicked.connect(lambda: self.cambiar_pestana(3))  # Productos
        self.findChild(QPushButton, "movimientos_1").clicked.connect(lambda: self.cambiar_pestana(4))  # Movimientos
        self.findChild(QPushButton, "usuarios_1").clicked.connect(lambda: self.cambiar_pestana(5))  # Usuarios
        self.findChild(QPushButton, "ingresos_egresos_2").clicked.connect(lambda: self.cambiar_pestana(0))  # Ingresos/Egresos
        self.findChild(QPushButton, "gestion_stock_2").clicked.connect(lambda: self.cambiar_pestana(1))  # Gestión de Stock
        self.findChild(QPushButton, "notas_pedido_2").clicked.connect(lambda: self.cambiar_pestana(2))  # Notas de Pedido
        self.findChild(QPushButton, "productos_2").clicked.connect(lambda: self.cambiar_pestana(3))  # Productos
        self.findChild(QPushButton, "movimientos_2").clicked.connect(lambda: self.cambiar_pestana(4))  # Movimientos
        self.findChild(QPushButton, "usuarios_2").clicked.connect(lambda: self.cambiar_pestana(5))  # Usuarios


    def cambiar_pestana(self, indice):
        """
        Cambia la pestaña activa en el QStackedWidget 'main_widget' según el índice dado.
        """
        self.main_widget.setCurrentIndex(indice)

        # Obtener el layout de la barra inferior correctamente
        bottom_widget = self.findChild(QWidget, "bottombar_widget")
        bottom_layout = bottom_widget.layout() if bottom_widget else None

        if bottom_layout is None:
            print("Error: No se encontró el layout 'bottombar_layout'.")
            return

        # Limpiar la barra inferior
        while bottom_layout.count():
            item = bottom_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Llamar a la función `actualizar_barra_inferior` de la vista seleccionada si existe
        vista = self.main_widget.widget(indice)  # Obtener la vista actual del QStackedWidget
        print(f"Vista seleccionada: {type(vista)}")
        # Verificar si la vista tiene la función `actualizar_barra_inferior`
        if hasattr(vista, 'actualizar_barra_inferior'):
            vista.actualizar_barra_inferior(indice)  # Llamar a la función para actualizar la barra inferior
        else:
            print(f"La vista en el índice {indice} no tiene la función 'actualizar_barra_inferior'.")
            
    def actualizar_barra_inferior(self, personalizaciones):
        """
        Actualiza los botones de la barra inferior en función de la vista seleccionada.
        """
        # Obtener el layout existente del widget "bottombar_widget"
        bottom_layout = self.bottombar_widget.layout()

        # Limpiar los widgets actuales
        while bottom_layout.count():
            item = bottom_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Crear y agregar los nuevos botones personalizados
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
            bottom_layout.addWidget(boton)

        # Establecer el layout en el widget (esto se asegura de que use el layout existente)
        self.bottombar_widget.setLayout(bottom_layout)
    
    
                
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