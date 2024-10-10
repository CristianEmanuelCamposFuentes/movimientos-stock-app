from sqlalchemy.orm import Session
from modules.models.database import Movimiento, get_db
from PyQt5.QtWidgets import QLabel, QLineEdit, QFormLayout, QHBoxLayout, QPushButton
from modules.utils.ui_styles import aplicar_estilos_especiales
import logging
from contextlib import contextmanager

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def obtener_sesion_bd():
    """Manejador de contexto para la sesión de base de datos."""
    db = next(get_db())
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logging.error(f"Error en la base de datos: {e}")
        raise
    finally:
        db.close()
        
def registrar_movimiento(ubicacion, codigo, cantidad, fecha, tipo_movimiento, nota_devolucion, observaciones):
    """Registra cualquier tipo de movimiento en la base de datos."""
    with obtener_sesion_bd() as db:
        nuevo_movimiento = Movimiento(
            ubicacion=ubicacion.upper(),  
            codigo=codigo.upper(),
            cantidad=cantidad,
            fecha=fecha,
            tipo_movimiento=tipo_movimiento,
            nota_devolucion=nota_devolucion,
            observaciones=observaciones
        )
        db.add(nuevo_movimiento)
        logging.info(f"Movimiento de {tipo_movimiento} registrado exitosamente.")
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

def crear_barra_botones(personalizaciones, estilos_adicionales=None):
    """
    Función que crea una barra de botones según las personalizaciones definidas.
    :param personalizaciones: Lista de diccionarios con las propiedades de cada botón:
        [
            {"texto": "Botón 1", "color": "green", "funcion": funcion_boton1, "estilo": "font-size:14px;"},
            {"texto": "Botón 2", "color": "blue", "funcion": funcion_boton2},
        ]
    :param estilos_adicionales: Un diccionario con estilos adicionales (opcional).
    :return: Un layout (QHBoxLayout) con los botones creados.
    """
    layout = QHBoxLayout()

    botones = []
    colores = []
    
    for personalizacion in personalizaciones:
        boton = QPushButton(personalizacion["texto"])
        boton.clicked.connect(personalizacion["funcion"])  # Conectar el evento de clic a la función
        
        # Aplicar estilos individuales si se proporcionan
        if "estilo" in personalizacion:
            boton.setStyleSheet(personalizacion["estilo"])
        
        botones.append(boton)
        colores.append(personalizacion["color"])
    
    aplicar_estilos_especiales(botones, colores)
    
    # Añadir los botones al layout
    for boton in botones:
        layout.addWidget(boton)
    
    return layout


