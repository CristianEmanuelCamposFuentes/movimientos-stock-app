from PyQt6.QtWidgets import QApplication
from modules.login import LoginWindow  # Importa la ventana de Login
import os
from sqlalchemy import create_engine
from modules.ui_styles import aplicar_estilos_ventana_principal  # Importa la función de estilos globales
from modules.database import crear_tablas

def setup_database():
    """Configurar la base de datos y las tablas."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'data', 'stock_management.db')
    engine = create_engine(f'sqlite:///{db_path}')
    print(f"Ruta de la base de datos: {db_path}")

    try:
        crear_tablas()
        print("Tablas creadas con éxito.")
    except Exception as e:
        print(f"Error al crear tablas en la base de datos: {e}")

if __name__ == "__main__":
    try:
        # Asegúrate de no crear ningún widget antes de esta línea
        app = QApplication([])  # Inicializar la aplicación de PyQt6
        
        setup_database()  # Ahora es seguro inicializar la base de datos

        aplicar_estilos_ventana_principal(app)  # Aplicar los estilos globales
        ventana_login = LoginWindow()  # Crear una instancia de la ventana de login
        ventana_login.show()  # Mostrar la ventana de login
        app.exec()  # Ejecutar el bucle principal de la aplicación
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
