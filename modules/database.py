from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Definir la base
Base = declarative_base()

# Tabla Productos
class Producto(Base):
    __tablename__ = 'Productos'

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    categoria = Column(String)
    imagen = Column(String)

# Tabla Ubicaciones
class Ubicacion(Base):
    __tablename__ = 'Ubicaciones'

    id_ubicacion = Column(Integer, primary_key=True, autoincrement=True)
    pasillo = Column(String, nullable=False)
    fila = Column(String, nullable=False)

# Tabla Stock
class Stock(Base):
    __tablename__ = 'Stock'

    id_stock = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('Productos.id_producto'), nullable=False)
    id_ubicacion = Column(Integer, ForeignKey('Ubicaciones.id_ubicacion'), nullable=False)
    cantidad = Column(Float, nullable=False)

    producto = relationship('Producto', backref='stock')
    ubicacion = relationship('Ubicacion', backref='stock')

# Tabla Movimientos
class Movimiento(Base):
    __tablename__ = 'Movimientos'

    id_movimiento = Column(Integer, primary_key=True, autoincrement=True)
    ubicacion = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    nota_devolucion = Column(String)
    tipo_movimiento = Column(String, nullable=False)
    observaciones = Column(String)

# Tabla Pendientes (para registrar incidentes)
class Pendiente(Base):
    __tablename__ = 'Pendientes'

    id_pendiente = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('Productos.id_producto'), nullable=False)
    id_ubicacion = Column(Integer, ForeignKey('Ubicaciones.id_ubicacion'), nullable=False)
    cantidad = Column(Float, nullable=False)
    motivo = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)

# Conectar con la base de datos
db_path = './data/stock_management.db'
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# Crear todas las tablas si no existen
Base.metadata.create_all(engine)
