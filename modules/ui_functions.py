from sqlalchemy.orm import Session
from modules.database import Movimiento, get_db
from PyQt5.QtWidgets import QLabel, QLineEdit, QFormLayout

def cargar_ingreso(ubicacion, codigo, cantidad, fecha, nota_devolucion, observaciones):
    # Usar contexto para obtener la sesión de la base de datos
    with next(get_db()) as db:
        nuevo_movimiento = Movimiento(
            ubicacion=ubicacion.upper(),  # Convertir a mayúsculas
            codigo=codigo.upper(),        # Convertir a mayúsculas
            cantidad=cantidad,
            fecha=fecha,
            nota_devolucion=nota_devolucion,
            tipo_movimiento="Ingreso",
            observaciones=observaciones
        )
        db.add(nuevo_movimiento)
        db.commit()

def cargar_egreso(ubicacion, codigo, cantidad, fecha, nota_devolucion, observaciones):
    # Usar contexto para obtener la sesión de la base de datos
    with next(get_db()) as db:
        nuevo_movimiento = Movimiento(
            ubicacion=ubicacion.upper(),  # Convertir a mayúsculas
            codigo=codigo.upper(),        # Convertir a mayúsculas
            cantidad=-float(cantidad),    # El egreso se refleja restando la cantidad
            fecha=fecha,
            nota_devolucion=nota_devolucion,
            tipo_movimiento="Egreso",
            observaciones=observaciones
        )
        db.add(nuevo_movimiento)
        db.commit()
    
def crear_campo_formulario(label_text, placeholder_text):
    """Crea un campo de formulario con una etiqueta y un QLineEdit."""
    label = QLabel(label_text)
    input_field = QLineEdit()
    input_field.setPlaceholderText(placeholder_text)
    
    # Retornamos la etiqueta y el campo como un tuple
    return label, input_field