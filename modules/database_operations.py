from modules.database import StockActual, Movimientos, get_db
from sqlalchemy.orm import Session

def obtener_stock(session: Session):
    """Obtiene todos los registros de stock actual"""
    return session.query(StockActual).all()

def registrar_movimiento(session: Session, movimiento_data):
    """Registra un nuevo movimiento en la base de datos"""
    nuevo_movimiento = Movimientos(**movimiento_data)
    session.add(nuevo_movimiento)
    session.commit()
