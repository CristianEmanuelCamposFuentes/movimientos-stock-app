from modules.form import create_form
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
    create_form()
