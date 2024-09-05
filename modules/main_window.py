from PyQt5.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import pandas as pd
import sqlite3

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Movimientos de Stock")
        self.setGeometry(100, 100, 1200, 800)

        # Layout principal (vertical)
        main_layout = QVBoxLayout()

        # Barra de navegación (horizontal)
        nav_bar = QHBoxLayout()
        search_label = QLabel("Buscar:")
        search_input = QLineEdit()
        user_section = QLabel("Usuario (inhabilitado)")
        nav_bar.addWidget(search_label)
        nav_bar.addWidget(search_input)
        nav_bar.addStretch()
        nav_bar.addWidget(user_section)

        # Menú lateral (vertical)
        menu_layout = QVBoxLayout()
        btn_ingresos = QPushButton("Ingresos/Egresos")
        btn_gestion_stock = QPushButton("Gestión de Stock")
        btn_admin_productos = QPushButton("Administrar Productos")
        btn_registros_movimientos = QPushButton("Registros de Movimientos")

        # Agregar iconos (asegúrate de tener las imágenes en la carpeta 'img')
        btn_ingresos.setIcon(QIcon('img/icono_ingresos.png'))
        btn_gestion_stock.setIcon(QIcon('img/icono_gestion.png'))
        btn_admin_productos.setIcon(QIcon('img/icono_admin.png'))
        btn_registros_movimientos.setIcon(QIcon('img/icono_registros.png'))

        menu_layout.addWidget(btn_ingresos)
        menu_layout.addWidget(btn_gestion_stock)
        menu_layout.addWidget(btn_admin_productos)
        menu_layout.addWidget(btn_registros_movimientos)
        menu_layout.addStretch()  # Para empujar los botones hacia arriba

        # Contenido central - Implementar Tabs
        tabs = QTabWidget()

        # Pestaña 1: Consolidado de Stock
        tab1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Consolidado del Depósito"))
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
        tabs.addTab(tab1, "Consolidado")
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

