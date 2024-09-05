
def aplicar_estilos(botones):
    button_style = """
    QPushButton {
        background-color: #4CAF50;
        color: white;
        font-size: 14px;
        border: none;
        padding: 10px;
        text-align: left;
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