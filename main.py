from PyQt5.QtWidgets import QApplication
from modules.login import LoginWindow  # Importa la ventana de Login
import os
from sqlalchemy import create_engine
from modules.ui_styles import aplicar_estilo_global  # Importa la función de estilos globales
from modules.database import crear_tablas

# Obtener la ruta absoluta del directorio donde está main.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta de la base de datos relativa al directorio de main.py
db_path = os.path.join(base_dir, 'data', 'stock_management.db')

# Crear el motor de SQLAlchemy con la ruta relativa
engine = create_engine(f'sqlite:///{db_path}')

print(f"Ruta de la base de datos: {db_path}")

crear_tablas()

if __name__ == "__main__":
    crear_tablas()
    app = QApplication([])  # Inicializar la aplicación de PyQt
    aplicar_estilo_global(app)  # Aplicar los estilos globales
    ventana_login = LoginWindow()  # Crear una instancia de la ventana de login
    ventana_login.show()  # Mostrar la ventana de login
    app.exec_()  # Ejecutar el bucle principal de la aplicación
