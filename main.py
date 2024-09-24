from PyQt6.QtWidgets import QApplication
from modules.login import LoginWindow  # Importa la ventana de Login
import os
from sqlalchemy import create_engine
from modules.ui_styles import aplicar_estilos_ventana_principal  # Importa la función de estilos globales
from modules.database import crear_tablas

# Obtener la ruta absoluta del directorio donde está main.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta de la base de datos relativa al directorio de main.py
db_path = os.path.join(base_dir, 'data', 'stock_management.db')
 
# Crear el motor de SQLAlchemy con la ruta relativa
engine = create_engine(f'sqlite:///{db_path}')

# Mostrar la ruta de la base de datos en la consola
print(f"Ruta de la base de datos: {db_path}")

# Crear tablas si no existen
try:
    crear_tablas()
except Exception as e:
    print(f"Error al crear tablas en la base de datos: {e}")

if __name__ == "__main__":
    try:
        app = QApplication([])  # Inicializar la aplicación de PyQt
        aplicar_estilos_ventana_principal(app)  # Aplicar los estilos globales
        ventana_login = LoginWindow()  # Crear una instancia de la ventana de login
        ventana_login.show()  # Mostrar la ventana de login
        app.exec()  # Ejecutar el bucle principal de la aplicación
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

