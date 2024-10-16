from PyQt6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize

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
    "smoke": "#e4e4e4",
    "nav-bar-bg": "#2C3E50",
    "menu-bg": "#34495E",
    "bottom-bar-bg": "#BDC3C7",
    'background': '#f0f0f0',
    'button-bg': '#3498db',
    'button-hover-bg': '#2980b9',
    'button-text': '#ffffff',
    'label-text': '#2c3e50',
    'input-bg': '#ffffff',
    'input-border': '#bdc3c7',
    'input-text': '#2c3e50',
}

# Estilos comunes para todos los botones
button_common_style = """
QPushButton {
    border-radius: 18px;
    font-size: 13px;
    font-weight: 500;
    padding: 12px;
    text-align: center;
    color: #FFF;
    text-transform: capitalize;
}

QPushButton:hover {
    opacity: 0.85;
}

QPushButton:pressed {
    opacity: 0.75;
}
"""

# Estilos personalizados para cada botón
button_styles = {
    # Botones específicos
    "green": f"""
    QPushButton#btn-cargar-ingreso {{
        background-color: {colors['grass']};
        color: {colors['snow']};
    }}
    QPushButton#btn-cargar-ingreso:hover {{
        background-color: #35b880;  # Puedes agregar más colores aquí o en el diccionario si son recurrentes
    }}
    QPushButton#btn-cargar-ingreso:pressed {{
        background-color: #2cae74;
    }}
    """,
    
    "red": f"""
    QPushButton#btn-cargar-egreso {{
        background-color: {colors['salmon']};
        color: {colors['snow']};
    }}
    QPushButton#btn-cargar-egreso:hover {{
        background-color: #db2848;  # Puedes mover este al diccionario si lo reutilizas
    }}
    QPushButton#btn-cargar-egreso:pressed {{
        background-color: #c4243d;
    }}
    """,
    
    "blue": f"""
    QPushButton#btn-ver-consolidado, QPushButton#btn-mover-pallet {{
        background-color: {colors['ocean']};
        color: {colors['snow']};
    }}
    QPushButton#btn-ver-consolidado:hover, QPushButton#btn-mover-pallet:hover {{
        background-color: #3b62d2;  # Igual que antes, considera mover al diccionario si es recurrente
    }}
    QPushButton#btn-ver-consolidado:pressed, QPushButton#btn-mover-pallet:pressed {{
        background-color: #3356bb;
    }}
    """
}


# Función para aplicar el estilo a un botón según el tipo
def aplicar_estilo_boton(boton, tipo):
    estilo = button_common_style + button_styles.get(tipo, "")
    boton.setStyleSheet(estilo)
    boton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

# Aplicar estilos a un conjunto de botones
def aplicar_estilos_a_botones(botones, tipos):
    for boton, tipo in zip(botones, tipos):
        aplicar_estilo_boton(boton, tipo)

# Aplicar estilos especiales a botones
def aplicar_estilos_especiales(botones, colores):
    for i, boton in enumerate(botones):
        aplicar_estilo_boton(boton, colores[i])

# Estilos para la barra de navegación superior
def aplicar_estilos_barra_navegacion(nav_widget):
    """
    Aplica los estilos a la barra de navegación contenida en el widget padre (parent_widget).
    """
    nav_widget.setStyleSheet(f"""
        #nav-bar {{
            background-color: {colors['nav-bar-bg']};  /* Fondo de la barra de navegación */
            padding: 10px;
            border-bottom: 2px solid {colors['smoke']};
        }}
    """)
    # Itera sobre los widgets del layout para aplicar estilos individuales
    for i in range(nav_widget.layout().count()):
        widget = nav_widget.layout().itemAt(i).widget()
        if isinstance(widget, QLabel):
            widget.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: #FFF;
                    text-align: center;
                }
            """)


# Estilos para la barra lateral
def aplicar_estilos_barra_lateral(menu_layout):
    menu_layout.parentWidget().setStyleSheet(f"""
        QWidget {{
            background-color: {colors['menu-bg']};  /* Fondo del menú lateral */
            padding: 15px;
            border-right: 2px solid {colors['smoke']};
        }}
    """)
    for boton in menu_layout.children():
        if isinstance(boton, QPushButton):
            boton.setStyleSheet(f"""
            QPushButton {{
                background-color: {colors['menu-bg']};
                color: white;
                font-size: 14px;
                border: none;
                padding: 10px;
                text-align: left;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {colors['ocean']};
            }}
            QPushButton:pressed {{
                background-color: {colors['dark']};
            }}
            """)
            boton.setIconSize(QSize(24, 24))

# Aplicar estilos globales a la ventana principal
def aplicar_estilos_ventana_principal(window):
    window.setStyleSheet(f"""
        QWidget {{
            background-color: {colors['background']};
            font-family: 'Arial', sans-serif;
        }}
        QPushButton {{
            background-color: {colors['button-bg']};
            max-height: 25px;
            color: {colors['button-text']};
            border-radius: 5px;
            padding: 10px;
        }}
        QPushButton:hover {{
            background-color: {colors['button-hover-bg']};
        }}
        QLabel {{
            color: {colors['label-text']};
            font-size: 16px;
            font-weight: bold;
        }}
        QLineEdit {{
            background-color: {colors['input-bg']};
            border: 1px solid {colors['input-border']};
            padding: 5px;
            border-radius: 3px;
            color: {colors['input-text']};
        }}
    """)

# Estilos para la barra inferior
def aplicar_estilos_barra_inferior(bottom_layout):
    bottom_layout.parentWidget().setStyleSheet(f"""
        .bottom-bar {{
            background-color: {colors['bottom-bar-bg']};
            padding: 10px;
            border-top: 2px solid {colors['smoke']};
        }}
    """)

# Crear contenedores con estilo
def crear_contenedor_con_estilo():
    layout = QVBoxLayout()
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(15)
    return layout

