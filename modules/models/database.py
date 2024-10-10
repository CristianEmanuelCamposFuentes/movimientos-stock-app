from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import bcrypt


# Definir la base
Base = declarative_base()

# Tabla Producto
class Producto(Base):
    __tablename__ = 'Producto'

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String, nullable=False, index=True)  # Índice para mejorar la búsqueda
    descripcion = Column(String, nullable=False)
    categoria = Column(String)
    imagen = Column(String)

# Tabla Ubicacion
class Ubicacion(Base):
    __tablename__ = 'Ubicacion'

    id_ubicacion = Column(Integer, primary_key=True, autoincrement=True)
    pasillo = Column(String, nullable=False)
    fila = Column(String, nullable=False)

    __table_args__ = (
        Index('idx_ubicacion_pasillo_fila', 'pasillo', 'fila'),  # Índice combinado
    )

# Tabla Stock
class Stock(Base):
    __tablename__ = 'Stock'

    id_stock = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('Producto.id_producto'), nullable=False)
    id_ubicacion = Column(Integer, ForeignKey('Ubicacion.id_ubicacion'), nullable=False)
    cantidad = Column(Float, nullable=False)

    producto = relationship('Producto', backref='stock')
    ubicacion = relationship('Ubicacion', backref='stock')

# Tabla Movimiento
class Movimiento(Base):
    __tablename__ = 'Movimiento'

    id_movimiento = Column(Integer, primary_key=True, autoincrement=True)
    ubicacion = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    nota_devolucion = Column(String)
    tipo_movimiento = Column(String, nullable=False)
    observaciones = Column(String)

# Tabla Pendiente (para registrar incidentes)
class Pendiente(Base):
    __tablename__ = 'Pendiente'

    id_pendiente = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('Producto.id_producto'), nullable=False)
    id_ubicacion = Column(Integer, ForeignKey('Ubicacion.id_ubicacion'), nullable=False)
    cantidad = Column(Float, nullable=False)
    motivo = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)

    producto = relationship('Producto')
    ubicacion = relationship('Ubicacion')
    
# Tabla NotasPedido (para gestionar las notas de pedido)
class NotasPedido(Base):
    __tablename__ = 'NotasPedido'

    id_nota = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    fecha_pedido = Column(Date, nullable=False)
    fecha_entrega = Column(Date)
    observaciones = Column(String)    
    
# Tabla Usuario (para gestionar usuarios)
class Usuario(Base):
    __tablename__ = 'Usuario'

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False, unique=True)
    contraseña = Column(String, nullable=False)  # Almacena la contraseña encriptada
    rol = Column(String, nullable=False)

    def set_password(self, password: str):
        """Encripta y guarda la contraseña."""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.contraseña = hashed_password.decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Verifica si la contraseña es correcta."""
        return bcrypt.checkpw(password.encode('utf-8'), self.contraseña.encode('utf-8'))


# Conectar con la base de datos
db_path = './data/stock_management.db'
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# Definir una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para crear todas las tablas si no existen
def crear_tablas():
    Base.metadata.create_all(engine)
    print("Tablas creadas con éxito.")

# Función para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

