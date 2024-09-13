from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

# Colores principales
colors = {
    "dark": "#161616",
    "ocean": "#416dea",
    "grass": "#3dd28d",
    "snow": "#FFFFFF",
    "salmon": "#F32C52",
    "sun": "#feee7d",
    "alge": "#7999a9",
    "flower": "#353866",
    "smoke": "#e4e4e4"
}

# Estilos comunes para todos los botones
button_common_style = """
QPushButton {
    border-radius: 18px;  /* Bordes redondeados */
    font-size: 13px;
    font-weight: 500;
    padding: 12px;
    text-align: center;
    color: #FFF;  /* Texto blanco por defecto */
    text-transform: capitalize;
}

QPushButton:hover {
    opacity: 0.85;  /* Opacidad al pasar el mouse */
}

QPushButton:pressed {
    opacity: 0.75;  /* Opacidad al presionar */
}
"""

# Estilos personalizados para cada botón
button_styles = {
    "regular": """
    QPushButton {
        background-color: #f2f2f2;
        color: #202129;
    }
    QPushButton:hover {
        background-color: #e1e2e2;
    }
    QPushButton:pressed {
        background-color: #d5d6d6;
    }
    """,
    "dark": """
    QPushButton {
        background-color: #161616;
        color: white;
    }
    QPushButton:hover {
        background-color: #1e1e1e;
    }
    QPushButton:pressed {
        background-color: #0f0f0f;
    }
    """,
    "green": """
    QPushButton#btn-cargar-ingreso {
        background-color: #3dd28d;  /* Fondo verde */
        color: white;
    }
    QPushButton#btn-cargar-ingreso:hover {
        background-color: #35b880;
    }
    QPushButton#btn-cargar-ingreso:pressed {
        background-color: #2cae74;
    }
    """,
    "red": """
    QPushButton#btn-cargar-egreso {
        background-color: #F32C52;  /* Fondo rojo */
        color: white;
    }
    QPushButton#btn-cargar-egreso:hover {
        background-color: #db2848;
    }
    QPushButton#btn-cargar-egreso:pressed {
        background-color: #c4243d;
    }
    """,
    "blue": """
    QPushButton#btn-ver-consolidado, QPushButton#btn-mover-pallet {
        background-color: #416dea;  /* Fondo azul */
        color: white;
    }
    QPushButton#btn-ver-consolidado:hover, QPushButton#btn-mover-pallet:hover {
        background-color: #3b62d2;
    }
    QPushButton#btn-ver-consolidado:pressed, QPushButton#btn-mover-pallet:pressed {
        background-color: #3356bb;
    }
    """,
    "salmon": """
    QPushButton {
        background-color: #F32C52;  /* Fondo rojo */
        color: white;
    }
    QPushButton:hover {
        background-color: #db2848;
    }
    QPushButton:pressed {
        background-color: #c4243d;
    }
    """,
    "sun": """
    QPushButton {
        background-color: #feee7d;  /* Fondo amarillo */
        color: #f15c5c;  /* Texto rojo suave */
    }
    QPushButton:hover {
        background-color: #f9e567;
    }
    QPushButton:pressed {
        background-color: #f5db50;
    }
    """,
    "alge": """
    QPushButton {
        background-color: #7999a9;  /* Fondo gris azulado */
        color: #e7ff20;  /* Texto amarillo */
    }
    QPushButton:hover {
        background-color: #6e8b98;
    }
    QPushButton:pressed {
        background-color: #647d88;
    }
    """,
    "flower": """
    QPushButton {
        background-color: #353866;  /* Fondo púrpura */
        color: #FE8CDF;  /* Texto rosa */
    }
    QPushButton:hover {
        background-color: #303260;
    }
    QPushButton:pressed {
        background-color: #292c59;
    }
    """
}

# Función para aplicar el estilo a un botón según el tipo
def aplicar_estilo_boton(boton, tipo):
    estilo = button_common_style + button_styles.get(tipo, "")
    boton.setStyleSheet(estilo)
    # Política de tamaño para que los botones se expandan correctamente
    boton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

# Aplicar estilos a un conjunto de botones
def aplicar_estilos_a_botones(botones, tipos):
    for boton, tipo in zip(botones, tipos):
        aplicar_estilo_boton(boton, tipo)
        
# Ejemplo de cómo aplicar estilos en tu ventana
def aplicar_estilos_especiales(botones, colores):
    for i, boton in enumerate(botones):
        aplicar_estilo_boton(boton, colores[i])

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
                    text-transform: uppercase;  /* Mayúsculas en los títulos */
                    text-align: center;
                }
            """)        

# Aplicar estilos globales a la ventana principal
def aplicar_estilos_ventana_principal(window):
    window.setStyleSheet("""
        QWidget {
            background-color: #ECF0F1;
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        QLineEdit {
            border: 1px solid #BDC3C7;
            border-radius: 4px;
            padding: 8px;
            font-size: 14px;
        }
        QLabel {
            font-size: 14px;
        }
        QPushButton {
            background-color: #3498DB;
            color: white;
            font-size: 14px;
            border: none;
            padding: 10px;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #2980B9;
        }
        QPushButton:pressed {
            background-color: #1F618D;
        }

        .nav-bar {
            background-color: #34495E;
            padding: 10px;
            border-bottom: 2px solid #BDC3C7;
        }
        
        .side-menu {
            background-color: #2C3E50;
            border-right: 2px solid #BDC3C7;
            padding: 20px;
        }
        
        .main-content {
            padding: 20px;
            background-color: #F7F7F7;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
        }

        .bottom-bar {
            background-color: #E0E0E0;
            padding: 15px;
            border-top: 2px solid #BDC3C7;
        }
    """)

# Aplicar estilos a la barra lateral (menú)
def aplicar_estilos_barra_lateral(botones):
    for boton in botones:
        boton.setStyleSheet("""
        QPushButton {
            background-color: #2C3E50;
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
            background-color: #34495E;
        }
        QPushButton:pressed {
            background-color: #1B2631;
        }
        """)
        boton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    # Aplicar íconos
    for i, boton in enumerate(botones):
        iconos = ["img/icono_ingresos.png", "img/icono_gestion.png", "img/icono_nota_pedido.png",
                  "img/icono_admin.png", "img/icono_registros.png", "img/icono_usuarios.png", "img/icono_ajustes.png"]
        boton.setIcon(QIcon(iconos[i]))
        boton.setIconSize(QSize(24, 24))

# Función para ajustar la política de tamaño de las tablas
def ajustar_estilos_tablas(tabla):
    tabla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    tabla.horizontalHeader().setStretchLastSection(True)
    tabla.verticalHeader().setVisible(False)
    
    


