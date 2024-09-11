from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize 

# Estilos para la barra de navegación superior
def aplicar_estilos_barra_navegacion(nav_layout):
    for i in range(nav_layout.count()):
        widget = nav_layout.itemAt(i).widget()
        if isinstance(widget, QLabel):
            widget.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: #333;
                    text-transform: uppercase;  /* Todas las letras en mayúsculas */
                }
            """)

# Estilos para la barra lateral (menú)
def aplicar_estilos_barra_lateral(botones):
    # Aplicar estilos a los botones dentro del menú
    for boton in botones:
        boton.setStyleSheet("""
            QPushButton {
                background-color: #2C3E50;  /* Gris oscuro */
                color: white;
                font-size: 14px;
                border: none;
                padding: 10px;
                margin-bottom: 5px;
                text-align: left;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #34495E;  /* Ligeramente más claro al pasar el mouse */
            }
            QPushButton:pressed {
                background-color: #1B2631;  /* Aún más oscuro al presionar */
            }
        """)
    
    # Aplicar íconos a los botones
    botones[0].setIcon(QIcon("img/icono_ingresos.png"))
    botones[1].setIcon(QIcon("img/icono_gestion.png"))
    botones[2].setIcon(QIcon("img/icono_nota_pedido.png"))
    botones[3].setIcon(QIcon("img/icono_admin.png"))
    botones[4].setIcon(QIcon("img/icono_registros.png"))
    botones[5].setIcon(QIcon("img/icono_usuarios.png"))
    botones[6].setIcon(QIcon("img/icono_ajustes.png"))
    
    # Ajustar tamaño del ícono
    for boton in botones:
        boton.setIconSize(QSize(24, 24))

# Estilos globales de la ventana principal
def aplicar_estilos_ventana_principal(window):
    window.setStyleSheet("""
        QWidget {
            background-color: #ECF0F1;  /* Fondo gris claro */
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        QLineEdit {
            border: 1px solid #BDC3C7;  /* Bordes grises claros */
            border-radius: 4px;
            padding: 8px;
            font-size: 14px;
        }
        QLabel {
            font-size: 14px;
        }
        QPushButton {
            background-color: #3498DB;  /* Azul para botones */
            color: white;
            font-size: 14px;
            border: none;
            padding: 10px;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #2980B9;  /* Azul más oscuro al pasar el mouse */
        }
        QPushButton:pressed {
            background-color: #1F618D;  /* Aún más oscuro al presionar */
        }
    """)

# Estilos para los botones principales de acción
def aplicar_estilos_botones_accion(btn_cargar_ingreso, btn_cargar_egreso, btn_ver_consolidado):
    btn_cargar_ingreso.setStyleSheet("""
        QPushButton {
            background-color: #27AE60;  /* Verde para ingresos */
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #229954;
        }
        QPushButton:pressed {
            background-color: #1E8449;
        }
    """)
    btn_cargar_egreso.setStyleSheet("""
        QPushButton {
            background-color: #E74C3C;  /* Rojo para egresos */
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #C0392B;
        }
        QPushButton:pressed {
            background-color: #A93226;
        }
    """)
    btn_ver_consolidado.setStyleSheet("""
        QPushButton {
            background-color: #3498DB;  /* Azul para ver consolidado */
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #2980B9;
        }
        QPushButton:pressed {
            background-color: #1F618D;
        }
    """)

# Estilos personalizados para botones con colores especiales
def aplicar_estilos_especiales(botones, colores):
    for i, btn in enumerate(botones):
        color = colores[i]
        btn.setStyleSheet(f"""
        QPushButton {{
            background-color: {color};
            color: white;
            font-size: 14px;
            border: none;
            padding: 10px;
            text-align: left;
            text-transform: uppercase;  /* Mayúsculas en los botones */
        }}
        QPushButton:hover {{
            background-color: {color};
            opacity: 0.8;
        }}
        QPushButton:pressed {{
            background-color: #2e7d32;
        }}
        """)

# Estilos globales
def aplicar_estilo_global(app):
    app.setStyleSheet("""
        /* Estilos globales */
        QWidget {
            background-color: #F7F7F7;  /* Fondo muy suave */
            font-family: 'Arial', sans-serif;
            color: #333;  /* Texto en gris oscuro */
        }
        QLineEdit, QComboBox, QDateEdit {
            border: 1px solid #CCC;
            border-radius: 5px;
            padding: 8px;
            background-color: #FFF;
            font-size: 14px;
        }
        QLabel {
            font-size: 14px;
            font-weight: normal;
            color: #444;
        }
        QPushButton {
            background-color: #E0E0E0;  /* Botón gris claro */
            color: #333;
            font-size: 14px;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #D5D5D5;  /* Hover: gris un poco más oscuro */
        }
        QPushButton:pressed {
            background-color: #C0C0C0;  /* Presionado: gris suave */
        }
        /* Estilos para tablas */
        QTableWidget {
            background-color: #FFF;
            border: 1px solid #DDD;
            gridline-color: #EEE;
            font-size: 14px;
        }
        QHeaderView::section {
            background-color: #F0F0F0;  /* Cabeceras en gris claro */
            padding: 8px;
            border: none;
            font-weight: bold;
        }
        QTableWidget::item {
            padding: 8px;
            border-bottom: 1px solid #EEE;
        }
        QTableWidget::item:selected {
            background-color: #DFF0D8;  /* Selección verde suave */
            color: #333;
        }
        /* Estilos para elementos flotantes */
        QDialog {
            background-color: #FFF;
            border: 1px solid #DDD;
            padding: 15px;
            border-radius: 8px;
        }
        /* Botones especiales */
        QPushButton.special {
            background-color: #B4D4F6;  /* Azul muy claro */
            color: white;
        }
        QPushButton.special:hover {
            background-color: #A4C4E6;  /* Hover en azul suave */
        }
        QPushButton.special:pressed {
            background-color: #8AA8D2;  /* Presionado en azul suave */
        }
    """)