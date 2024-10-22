from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QFormLayout, QStackedWidget
from modules.models.database_operations import obtener_consolidado_stock, realizar_ajuste_stock, mover_pallet
from modules.utils.ui_styles import aplicar_estilos_especiales, crear_contenedor_con_estilo
from modules.views.ajustes.ajustes import AjustesView  # Importa la vista AjustesView

class GestionStockView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Referencia a la ventana principal
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Stock")

        # Crear el contenedor principal con estilo
        main_layout = crear_contenedor_con_estilo()

        # Crear el QStackedWidget
        self.stack = QStackedWidget()

        # Agregar las diferentes vistas al QStackedWidget
        self.consolidado_page = self.consolidado_tab()
        self.ajustes_page = AjustesView(self)  # Instanciar la vista de ajustes
        self.mover_pallet_page = self.mover_pallet_tab()

        self.stack.addWidget(self.consolidado_page)
        self.stack.addWidget(self.ajustes_page)  # Añadir ajustes como una vista
        self.stack.addWidget(self.mover_pallet_page)

        # Agregar el QStackedWidget al layout principal
        main_layout.addWidget(self.stack)

        # Barra inferior personalizada
        botones = [
            {"texto": "Exportar a Excel", "color": "alge", "funcion": self.exportar_excel},
            {"texto": "Exportar a CSV", "color": "alge", "funcion": self.exportar_csv},
            {"texto": "Generar PDF", "color": "alge", "funcion": self.generar_pdf},
            {"texto": "Imprimir Pallet", "color": "alge", "funcion": self.imprimir_pallet}
        ]
        bottom_bar = self.parent.crear_barra_botones_inferiores(botones)
        main_layout.addLayout(bottom_bar)

        self.setLayout(main_layout)

    # Función para cambiar la vista en el QStackedWidget
    def cambiar_vista(self, indice):
        self.stack.setCurrentIndex(indice)
        self.actualizar_barra_inferior(indice)

    # Función para actualizar la barra inferior según la vista activa
    def actualizar_barra_inferior(self, indice):
        if indice == 0:  # Consolidado
            botones = [
                {"texto": "Exportar a Excel", "color": "alge", "funcion": self.exportar_excel},
                {"texto": "Exportar a CSV", "color": "alge", "funcion": self.exportar_csv}
            ]
        elif indice == 1:  # Ajustes
            botones = [
                {"texto": "Cargar CSV", "color": "snow", "funcion": self.ajustes_page.parent.cargar_csv_stock},
                {"texto": "Backup Stock", "color": "snow", "funcion": self.ajustes_page.parent.hacer_backup_stock}
            ]
        elif indice == 2:  # Mover Pallet
            botones = [
                {"texto": "Mover Pallet", "color": "salmon", "funcion": self.mover_pallet}
            ]
        self.parent.actualizar_barra_inferior(botones)

    # Pestaña 1: Consolidado
    def consolidado_tab(self):
        consolidado_widget = QWidget()
        layout = QVBoxLayout()

        # Buscador de stock
        buscar_layout = QHBoxLayout()
        self.buscar_input = QLineEdit()
        buscar_layout.addWidget(QLabel("Buscar:"))
        buscar_layout.addWidget(self.buscar_input)
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(self.buscar_consolidado)
        buscar_layout.addWidget(buscar_button)
        layout.addLayout(buscar_layout)

        # Tabla para mostrar el consolidado de stock
        self.consolidado_table = QTableWidget(0, 5)
        self.consolidado_table.setHorizontalHeaderLabels(["Código", "Descripción", "Ubicación", "Cantidad", "Fecha"])
        layout.addWidget(self.consolidado_table)

        consolidado_widget.setLayout(layout)
        return consolidado_widget

    # Función para buscar y filtrar consolidado
    def buscar_consolidado(self):
        filtro = self.buscar_input.text()
        resultados = obtener_consolidado_stock(filtro)
        self.consolidado_table.setRowCount(0)
        for i, item in enumerate(resultados):
            self.consolidado_table.insertRow(i)
            self.consolidado_table.setItem(i, 0, QTableWidgetItem(item.codigo))
            self.consolidado_table.setItem(i, 1, QTableWidgetItem(item.descripcion))
            self.consolidado_table.setItem(i, 2, QTableWidgetItem(item.ubicacion))
            self.consolidado_table.setItem(i, 3, QTableWidgetItem(str(item.cantidad)))
            self.consolidado_table.setItem(i, 4, QTableWidgetItem(item.fecha.strftime('%d/%m/%Y')))

    # Pestaña 2: Mover Pallet (igual que antes)
    def mover_pallet_tab(self):
        mover_pallet_widget = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.codigo_pallet_input = QLineEdit()
        form_layout.addRow("Código del pallet:", self.codigo_pallet_input)

        self.ubicacion_actual_input = QLineEdit()
        form_layout.addRow("Ubicación actual:", self.ubicacion_actual_input)

        self.ubicacion_nueva_input = QLineEdit()
        form_layout.addRow("Nueva ubicación:", self.ubicacion_nueva_input)

        mover_button = QPushButton("Mover Pallet")
        mover_button.clicked.connect(self.mover_pallet)
        
        # Aplicar estilo especial al botón
        aplicar_estilos_especiales([mover_button], ["salmon"])

        layout.addLayout(form_layout)
        layout.addWidget(mover_button)

        mover_pallet_widget.setLayout(layout)
        return mover_pallet_widget

    # Función para mover pallet (igual que antes)
    def mover_pallet(self):
        codigo_pallet = self.codigo_pallet_input.text()
        ubicacion_actual = self.ubicacion_actual_input.text()
        nueva_ubicacion = self.ubicacion_nueva_input.text()
        mover_pallet(codigo_pallet, ubicacion_actual, nueva_ubicacion, 0)

    # Funciones adicionales
    def exportar_excel(self):
        print("Exportando a Excel...")

    def exportar_csv(self):
        print("Exportando a CSV...")

    def generar_pdf(self):
        print("Generando PDF...")

    def imprimir_pallet(self):
        print("Imprimiendo pallet...")


