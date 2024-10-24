from PyQt6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize

colors = {
    "dark": "#161616",
    "ocean": "#416dea",
    "grass": "#3dd28d",
    "snow": "#FFFFFF",  # Blanco puro
    "salmon": "#F32C52",
    "sun": "#feee7d",
    "alge": "#7999a9",
    "flower": "#353866",
    "smoke": "#e4e4e4",
    "nav-bar-bg": "#2C3E50",
    "menu-bg": "#34495E",
    "menu-bg-checked": "#FFFFFF",  # Color del botón seleccionado
    "menu-checked-text": "#d30000",  # Texto del botón seleccionado
    "menu-bg-hover": "rgb(194, 70, 49)",  # Color del botón hover en el menú
    "bottom-bar-bg": "#BDC3C7",
    'background': '#f0f0f0',
    'button-bg': '#3498db',
    'button-hover-bg': '#2980b9',
    'button-text': '#ffffff',
    'label-text': '#2c3e50',
    'input-bg': '#ffffff',
    'input-border': '#bdc3c7',
    'input-text': '#2c3e50',
    'navbar-gradient-start': 'rgb(212, 131, 131)',
    'navbar-gradient-end': 'rgb(225, 186, 187)',
    'search-button-bg': 'rgb(131, 25, 27)',
    'search-input-bg': 'rgb(255, 251, 212)'
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
    background-color: {color};
}

QPushButton:hover {
    opacity: 0.85;
}

QPushButton:pressed {
    opacity: 0.75;
}
"""

# Estilos personalizados para cada botón según el color
button_styles = {
    "green": f"""
    QPushButton {{
        background-color: {colors['grass']};
        color: {colors['snow']};
    }}
    QPushButton:hover {{
        background-color: #35b880;
    }}
    QPushButton:pressed {{
        background-color: #2cae74;
    }}
    """,
    
    "red": f"""
    QPushButton {{
        background-color: {colors['salmon']};
        color: {colors['snow']};
    }}
    QPushButton:hover {{
        background-color: #db2848;
    }}
    QPushButton:pressed {{
        background-color: #c4243d;
    }}
    """,
    
    "blue": f"""
    QPushButton {{
        background-color: {colors['ocean']};
        color: {colors['snow']};
    }}
    QPushButton:hover {{
        background-color: #3b62d2;
    }}
    QPushButton:pressed {{
        background-color: #3356bb;
    }}
    """
}

# Función para aplicar los estilos de color a un botón según el color especificado
def aplicar_estilo_boton(boton, color):
    estilo = button_styles.get(color, "")  # Obtiene el estilo según el color
    print(f"Aplicando estilo para {color}: {estilo}")
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

def aplicar_estilos_barra_navegacion(nav_widget):
    nav_widget.setStyleSheet(f"""
        QWidget {{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {colors['navbar-gradient-start']}, stop:1 {colors['navbar-gradient-end']});
            color: {colors['snow']};
            border-bottom: 2px solid {colors['dark']}; /* Añadir un borde en la parte inferior */
        }}
        QLabel {{
            font-size: 18px;
            color: {colors['snow']};
            font-weight: bold;
        }}
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
                background-color: {colors['menu-bg-hover']};
            }}
            QPushButton:pressed {{
                background-color: {colors['dark']};
            }}
            """)
            boton.setIconSize(QSize(24, 24))  # Asegúrate de que los iconos se ajustan correctamente


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

def aplicar_estilos_barra_inferior(bottom_layout):
    bottom_layout.parentWidget().setStyleSheet(f"""
        QWidget {{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {colors['navbar-gradient-start']}, stop:1 {colors['navbar-gradient-end']});
            color: {colors['snow']};
            border-top: 2px solid {colors['dark']};
            padding: 10px;  /* Añadir padding para los elementos dentro de la barra */
            box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.2);  /* Sombra suave para dar profundidad */
        }}

        QPushButton {{
            background-color: {colors['button-bg']};  /* Color de fondo de los botones */
            color: {colors['button-text']};
            border-radius: 5px;
            padding: 8px 16px;
            font-size: 14px;
        }}
        QPushButton:hover {{
            background-color: {colors['button-hover-bg']};  /* Color hover */
        }}
        QPushButton:pressed {{
            background-color: {colors['dark']};  /* Color cuando se presiona */
        }}
    """)




# Crear contenedores con estilo
def crear_contenedor_con_estilo():
    layout = QVBoxLayout()
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(15)
    return layout

def aplicar_estilos_search_button(search_button):
    search_button.setStyleSheet(f"""
        QPushButton#search_button {{
            background-color: {colors['search-button-bg']};
            border-radius: 8px;
            padding: 10px;
            font: bold 12px;
            color: {colors['snow']};
        }}

        QPushButton#search_button:hover {{
            background-color: {colors['ocean']};
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);  /* Sombra al pasar el mouse */
        }}

        QPushButton#search_button:pressed {{
            background-color: {colors['dark']};
            border: 1px solid {colors['nav-bar-bg']};  /* Bordes más claros cuando el botón es presionado */
        }}
    """)


def aplicar_estilos_search_input(search_input):
    search_input.setStyleSheet(f"""
        QLineEdit {{
            background-color: {colors['search-input-bg']};
        }}
    """)
