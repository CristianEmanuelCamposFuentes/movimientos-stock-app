from sqlalchemy.orm import Session
from modules.database import Movimiento, get_db
from PyQt5.QtWidgets import QLabel, QLineEdit, QFormLayout

def registrar_movimiento(ubicacion, codigo, cantidad, fecha, tipo_movimiento, nota_devolucion, observaciones):
    """Registra cualquier tipo de movimiento en la base de datos."""
    with next(get_db()) as db:
        try:
            nuevo_movimiento = Movimiento(
                ubicacion=ubicacion.upper(),  # Convertir a mayúsculas
                codigo=codigo.upper(),        # Convertir a mayúsculas
                cantidad=cantidad,
                fecha=fecha,
                tipo_movimiento=tipo_movimiento,  # Tipo de movimiento: Ingreso, Egreso, Ajuste, Movimiento
                nota_devolucion=nota_devolucion,
                observaciones=observaciones
            )
            db.add(nuevo_movimiento)
            db.commit()
            print(f"Movimiento de {tipo_movimiento} registrado exitosamente")
        except Exception as e:
            db.rollback()
            print(f"Error al registrar el movimiento: {e}")

def cargar_ingreso(ubicacion, codigo, cantidad, fecha, nota_devolucion, observaciones):
    """Función específica para registrar un Ingreso."""
    registrar_movimiento(
        ubicacion=ubicacion,
        codigo=codigo,
        cantidad=cantidad,  # Ingresos suman la cantidad
        fecha=fecha,
        tipo_movimiento="Ingreso",
        nota_devolucion=nota_devolucion,
        observaciones=observaciones
    )

def cargar_egreso(ubicacion, codigo, cantidad, fecha, nota_devolucion, observaciones):
    """Función específica para registrar un Egreso."""
    registrar_movimiento(
        ubicacion=ubicacion,
        codigo=codigo,
        cantidad=-float(cantidad),  # Egresos restan la cantidad
        fecha=fecha,
        tipo_movimiento="Egreso",
        nota_devolucion=nota_devolucion,
        observaciones=observaciones
    )

def cargar_ajuste(ubicacion, codigo, cantidad, fecha, observaciones):
    """Función para registrar un ajuste de stock."""
    registrar_movimiento(
        ubicacion=ubicacion,
        codigo=codigo,
        cantidad=cantidad,  # El ajuste puede ser positivo o negativo
        fecha=fecha,
        tipo_movimiento="Ajuste",
        nota_devolucion="Ajuste Manual",  # Ajustes manuales no tienen nota de devolución
        observaciones=observaciones
    )

def mover_pallet(ubicacion_origen, ubicacion_destino, codigo, cantidad, fecha):
    """Función para registrar el movimiento de un pallet."""
    registrar_movimiento(
        ubicacion=ubicacion_origen,
        codigo=codigo,
        cantidad=-float(cantidad),  # En la ubicación de origen se resta
        fecha=fecha,
        tipo_movimiento="Movimiento",
        nota_devolucion=f"Movido a {ubicacion_destino}",
        observaciones="Movimiento de pallet"
    )

    registrar_movimiento(
        ubicacion=ubicacion_destino,
        codigo=codigo,
        cantidad=float(cantidad),  # En la ubicación de destino se suma
        fecha=fecha,
        tipo_movimiento="Movimiento",
        nota_devolucion=f"Recibido desde {ubicacion_origen}",
        observaciones="Movimiento de pallet"
    )

def crear_campo_formulario(label_text, placeholder_text):
    """Crea un campo de formulario con una etiqueta y un QLineEdit."""
    label = QLabel(label_text)
    input_field = QLineEdit()
    input_field.setPlaceholderText(placeholder_text)
    
    # Retornamos la etiqueta y el campo como un tuple
    return label, input_field