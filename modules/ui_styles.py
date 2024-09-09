from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

# Estilo para los botones principales (Ingresos/Egresos/Ajustes)
def aplicar_estilos(botones):
    """Aplica estilos predeterminados a una lista de botones."""
    button_style = """
    QPushButton {
        background-color: #4CAF50;  /* Verde por defecto */
        color: white;
        font-size: 14px;
        border: none;
        padding: 10px;
        margin: 5px 0;  /* Márgenes entre los botones */
        text-align: center;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #2e7d32;
    }
    """
    for btn in botones:
        btn.setStyleSheet(button_style)

# Estilos especiales para botones de acciones específicas (Ingreso, Egreso, Ajustes)
def aplicar_estilos_especiales(botones, colores):
    """Aplica estilos a botones individuales con colores específicos."""
    for i, btn in enumerate(botones):
        color = colores[i]
        button_style = f"""
        QPushButton {{
            background-color: {color};
            color: white;
            font-size: 14px;
            border: none;
            padding: 10px;
            margin: 5px 0;
            text-align: center;
        }}
        QPushButton:hover {{
            background-color: {color};
            opacity: 0.9;
        }}
        QPushButton:pressed {{
            background-color: #2e7d32;  /* Color fijo al presionar */
        }}
        """
        btn.setStyleSheet(button_style)

# Estilos generales para formularios (inputs y etiquetas)
formulario_estilo = """
QLineEdit {
    padding: 8px;
    margin: 5px 0;
    font-size: 14px;
}

QLabel {
    font-size: 14px;
    margin-bottom: 5px;
}

QPushButton {
    padding: 10px;
    font-size: 14px;
    margin: 10px;
}
"""

# Aplicar estilos a toda la aplicación
def aplicar_estilo_global(app):
    """Aplica el estilo global de la aplicación, como formularios y botones."""
    app.setStyleSheet(formulario_estilo)


