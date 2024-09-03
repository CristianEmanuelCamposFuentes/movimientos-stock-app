import os
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Obtener la ruta absoluta del directorio de este script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta de la base de datos relativa al directorio de este script
db_path = os.path.join(base_dir, '..', 'data', 'stock_management.db')

# Configuración de SQLAlchemy con la ruta relativa
engine = create_engine(f'sqlite:///{db_path}', echo=True)
Base = declarative_base()

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de la tabla de stock actual
class StockActual(Base):
    __tablename__ = "stock_actual"
    id = Column(Integer, primary_key=True, index=True)
    pasillo = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    codigo = Column(String, nullable=False)  # Eliminé `unique=True` para permitir duplicados
    descripcion = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)

# Modelo de la tabla de movimientos
class Movimientos(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    ubicacion = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    nota_devolucion = Column(String, nullable=False)
    tipo_movimiento = Column(String, nullable=False)
    observaciones = Column(String)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

