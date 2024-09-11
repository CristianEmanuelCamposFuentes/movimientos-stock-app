from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize 

# Estilos para la barra de navegación superior
def aplicar_estilos_barra_navegacion(nav_layout):
    # Aplicar estilos a los widgets dentro del nav_layout
    for i in range(nav_layout.count()):
        widget = nav_layout.itemAt(i).widget()
        if isinstance(widget, QLabel):
            widget.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: #333;
                }
            """)

# Estilos para la barra lateral (menú)
def aplicar_estilos_barra_lateral(botones):
    # Aplicar estilos a los botones dentro del menú
    for boton in botones:
        boton.setStyleSheet("""
            QPushButton {
                background-color: #E8E8E8;
                color: #333;
                font-size: 14px;
                border: 1px solid #CCC;
                padding: 10px;
                margin-bottom: 5px;
                text-align: left;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D0D0D0;
            }
            QPushButton:pressed {
                background-color: #C0C0C0;
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
    # Aplicar los estilos a la ventana principal
    window.setStyleSheet("""
        QWidget {
            background-color: #FAFAFA;
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        QLineEdit {
            border: 1px solid #CCC;
            border-radius: 4px;
            padding: 8px;
            font-size: 14px;
        }
        QLabel {
            font-size: 14px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 14px;
            border: none;
            padding: 10px;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #2e7d32;
        }
    """)

# Estilos para los botones principales de acción
def aplicar_estilos_botones_accion(btn_cargar_ingreso, btn_cargar_egreso, btn_ver_consolidado):
    btn_cargar_ingreso.setStyleSheet("""
        QPushButton {
            background-color: green;
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #2e7d32;
        }
    """)
    btn_cargar_egreso.setStyleSheet("""
        QPushButton {
            background-color: red;
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #d32f2f;
        }
        QPushButton:pressed {
            background-color: #b71c1c;
        }
    """)
    btn_ver_consolidado.setStyleSheet("""
        QPushButton {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #0056b3;
        }
        QPushButton:pressed {
            background-color: #003c82;
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
    # Aquí defines los estilos globales de la aplicación
    app.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QLabel {
            font-size: 14px;
        }
        QMainWindow {
            background-color: #f0f0f0;
        }
    """)
