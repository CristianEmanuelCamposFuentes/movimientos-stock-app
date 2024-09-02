from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from tkinter import messagebox  # <--- Importación agregada
from modules.database import StockActual, Movimiento, get_db

def get_description_by_code(db: Session, codigo: str) -> str:
    """Obtener la descripción del producto dado su código."""
    stock_item = db.query(StockActual).filter(StockActual.codigo == codigo).first()
    if stock_item:
        return stock_item.descripcion
    return None

def process_data(ubicacion: str, codigo: str, cantidad: str, fecha: str, nota_devolucion: str, tipo_movimiento: str, observaciones: str):
    """Procesar el movimiento de stock, actualizando la base de datos."""
    try:
        db = next(get_db())
        
        # Convertir la cantidad a un número
        cantidad = float(cantidad)
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        
        # Validar que la fecha es válida
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        
        # Obtener el registro actual de stock
        stock_item = db.query(StockActual).filter(
            StockActual.ubicacion == ubicacion,
            StockActual.codigo == codigo
        ).first()
        
        if tipo_movimiento == "Ingreso":
            if stock_item:
                stock_item.cantidad += cantidad
                stock_item.fecha = fecha
            else:
                # Si no existe el registro, creamos uno nuevo
                stock_item = StockActual(
                    pasillo=ubicacion.split('-')[0],  # Ejemplo de cómo extraer pasillo de la ubicación
                    ubicacion=ubicacion,
                    codigo=codigo,
                    descripcion=get_description_by_code(db, codigo),
                    cantidad=cantidad,
                    fecha=fecha
                )
                db.add(stock_item)
        
        elif tipo_movimiento == "Egreso":
            if stock_item:
                if stock_item.cantidad >= cantidad:
                    stock_item.cantidad -= cantidad
                    stock_item.fecha = fecha
                else:
                    raise ValueError("No hay suficiente stock para realizar el egreso.")
            else:
                raise ValueError("No se encontró stock para el código y la ubicación especificados.")
        
        # Registrar el movimiento en la tabla de históricos
        movimiento = Movimiento(
            ubicacion=ubicacion,
            codigo=codigo,
            descripcion=stock_item.descripcion if stock_item else get_description_by_code(db, codigo),
            cantidad=cantidad,
            fecha=fecha,
            nota_devolucion=nota_devolucion,
            tipo_movimiento=tipo_movimiento,
            observaciones=observaciones
        )
        db.add(movimiento)
        
        # Guardar los cambios en la base de datos
        db.commit()
        messagebox.showinfo("Éxito", "Movimiento registrado con éxito.")
        
    except SQLAlchemyError as e:
        db.rollback()  # Revertir cambios en caso de error
        messagebox.showerror("Error en la base de datos", str(e))
    except ValueError as ve:
        messagebox.showerror("Error de validación", str(ve))
    finally:
        db.close()

