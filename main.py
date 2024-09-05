import sys
from PyQt5.QtWidgets import QApplication
from modules.form import StockMovementApp
from modules.main_window import MainWindow   # Asegúrate de que la clase esté en el archivo correcto
import os
from sqlalchemy import create_engine

# Obtener la ruta absoluta del directorio donde está main.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta de la base de datos relativa al directorio de main.py
db_path = os.path.join(base_dir, 'data', 'stock_management.db')

# Crear el motor de SQLAlchemy con la ruta relativa
engine = create_engine(f'sqlite:///{db_path}')

print(f"Ruta de la base de datos: {db_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()  # Inicializar la aplicación de PyQt
    #ventana = StockMovementApp()    Crear una instancia de la interfaz
    ventana.show()                 # Mostrar la ventana
    sys.exit(app.exec_())          # Ejecutar el bucle principal de la aplicación

app.setStyleSheet("""
QWidget {
    background-color: #F0F0F0;
}
QPushButton {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    border-radius: 5px;
}
""")