from sqlalchemy.orm import Session
from modules.database import Stock, Movimiento, get_db, NotasPedido, Producto, Pendiente
from datetime import datetime
import csv
from fpdf import FPDF  # Necesitarás instalar esta librería con `pip install fpdf`
from datetime import datetime



# Obtener el consolidado de stock actual
def obtener_stock(session: Session):
    """Obtiene todos los registros de stock actual"""
    return session.query(Stock).all()

# Registrar un nuevo movimiento
# Registrar un nuevo movimiento
def registrar_movimiento(session: Session, movimiento_data):
    """Registra un nuevo movimiento en la base de datos"""
    try:
        nuevo_movimiento = Movimiento(**movimiento_data)
        session.add(nuevo_movimiento)
        session.commit()
        print("Movimiento registrado con éxito")
    except Exception as e:
        session.rollback()
        print(f"Error al registrar el movimiento: {e}")

# Obtener el consolidado de stock con un filtro opcional
def obtener_consolidado_stock(filtro=None):
    db = next(get_db())
    try:
        if filtro:
            # Aplicar el filtro para buscar registros específicos por código o descripción
            consolidado = db.query(Stock).join(Producto).filter(
                (Producto.codigo.contains(filtro)) | (Producto.descripcion.contains(filtro))
            ).all()
        else:
            # Devolver todos los registros si no hay filtro
            consolidado = db.query(Stock).all()
        print(f"Consolidado encontrado: {consolidado}")
        return consolidado
    except Exception as e:
        print(f"Error al obtener el consolidado de stock: {e}")
        return []
    finally:
        db.close()


# Realizar ajuste de stock
def realizar_ajuste_stock(codigo: str, ubicacion: str, nueva_cantidad: float):
    db = next(get_db())
    try:
        # Buscar el ítem de stock que coincida con el código y la ubicación
        stock_item = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion, Producto.codigo == codigo).first()
        if stock_item:
            stock_item.cantidad = nueva_cantidad  # Actualizar la cantidad de stock
            movimiento = Movimiento(
                ubicacion=ubicacion,
                codigo=codigo,
                cantidad=nueva_cantidad,
                fecha=datetime.now(),
                nota_devolucion="Ajuste manual",
                tipo_movimiento="Ajuste",
                observaciones="Ajuste de stock"
            )
            db.add(movimiento)  # Registrar el ajuste como un movimiento
            db.commit()
            print(f"Stock ajustado correctamente para {codigo} en {ubicacion}")
        else:
            print(f"No se encontró stock para {codigo} en {ubicacion}")
    except Exception as e:
        db.rollback()
        print(f"Error al realizar el ajuste de stock: {e}")
    finally:
        db.close()

# Mover pallet de una ubicación a otra
def mover_pallet(codigo: str, ubicacion_origen: str, ubicacion_destino: str, cantidad: float):
    db = next(get_db())
    try:
        # Buscar el stock en la ubicación de origen
        stock_origen = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion_origen, Producto.codigo == codigo).first()
        if stock_origen and stock_origen.cantidad >= cantidad:
            stock_origen.cantidad -= cantidad  # Descontar la cantidad del origen
            
            # Buscar o crear el stock en la ubicación de destino
            stock_destino = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion_destino, Producto.codigo == codigo).first()
            if stock_destino:
                stock_destino.cantidad += cantidad  # Añadir la cantidad al destino
            else:
                # Si no existe en destino, creamos un nuevo registro
                nuevo_stock = Stock(
                    ubicacion=ubicacion_destino,
                    cantidad=cantidad,
                    id_producto=stock_origen.id_producto,
                    id_ubicacion=stock_origen.id_ubicacion
                )
                db.add(nuevo_stock)

            # Registrar el movimiento como "Movimiento de pallet"
            movimiento = Movimiento(
                ubicacion=ubicacion_origen,
                codigo=codigo,
                cantidad=-cantidad,
                fecha=datetime.now(),
                nota_devolucion="Movimiento de pallet",
                tipo_movimiento="Movimiento",
                observaciones=f"Movido a {ubicacion_destino}"
            )
            db.add(movimiento)

            db.commit()
            print(f"Pallet movido de {ubicacion_origen} a {ubicacion_destino}")
        else:
            print(f"No se encontró suficiente stock para {codigo} en {ubicacion_origen}")
    except Exception as e:
        db.rollback()
        print(f"Error al mover el pallet: {e}")
    finally:
        db.close()

# Función para generar una nueva nota de pedido
def generar_nota_pedido(session: Session, codigo: str, descripcion: str, cantidad: float, fecha: str, numero_nota: str = None):
    try:
        nueva_nota = NotasPedido(
            codigo=codigo,
            descripcion=descripcion,
            cantidad=cantidad,
            fecha_pedido=fecha,
            numero_nota=numero_nota
        )
        session.add(nueva_nota)
        session.commit()
        print("Nota de pedido generada con éxito")
    except Exception as e:
        session.rollback()
        print(f"Error al generar la nota de pedido: {e}")

# Función para registrar un pendiente
def registrar_pendiente(session: Session, codigo: str, descripcion: str, cantidad: float, fecha: str, motivo: str, ubicacion: str = None):
    try:
        pendiente = Pendiente(
            codigo=codigo,
            descripcion=descripcion,
            cantidad=cantidad,
            fecha=datetime.strptime(fecha, "%d/%m/%Y"),
            motivo=motivo,
            ubicacion=ubicacion
        )
        session.add(pendiente)
        session.commit()
        print("Pendiente registrado con éxito")
    except Exception as e:
        session.rollback()
        print(f"Error al registrar el pendiente: {e}")

# Función para obtener la descripción del producto dado su código
def get_description_by_code(db: Session, codigo: str) -> str:
    """Obtener la descripción del producto dado su código."""
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if producto:
        return producto.descripcion
    return "Descripción no encontrada"

# Función para cargar una nota de pedido
def cargar_nota_pedido(db: Session, numero_nota: str):
    """
    Carga una nota de pedido por su número.
    :param db: La sesión de base de datos.
    :param numero_nota: El número de la nota de pedido a buscar.
    :return: Lista de productos y detalles asociados a la nota.
    """
    try:
        # Busca la nota de pedido con el número proporcionado
        nota = db.query(NotasPedido).filter(NotasPedido.numero_nota == numero_nota).all()
        
        if not nota:
            return []
        
        # Devuelve la información de la nota de pedido
        return [{
            'codigo': item.codigo,
            'descripcion': db.query(Producto).filter(Producto.codigo == item.codigo).first().descripcion,
            'cantidad': item.cantidad,
            'ubicacion': item.ubicacion  # Este campo se debe ajustar según la estructura de tu DB
        } for item in nota]
        
    except Exception as e:
        print(f"Error al cargar la nota de pedido: {e}")
        return []

# Función para obtener los registros de notas de pedido
def obtener_registros_notas(session: Session, filtro=None):
    """Obtiene todas las notas de pedido con un filtro opcional."""
    try:
        query = session.query(NotasPedido)
        if filtro:
            # Aplicar filtro por código o descripción si es necesario
            query = query.filter(
                (NotasPedido.codigo.contains(filtro)) |
                (NotasPedido.descripcion.contains(filtro))
            )
        notas = query.all()
        return [{
            'numero_nota': nota.numero_nota,
            'codigo': nota.codigo,
            'cantidad': nota.cantidad,
            'ubicacion': session.query(Stock).filter(Stock.codigo == nota.codigo).first().ubicacion if nota else "Sin ubicación",
            'fecha': nota.fecha_pedido.strftime('%d/%m/%Y')
        } for nota in notas]
    except Exception as e:
        print(f"Error al obtener registros de notas de pedido: {e}")
        return []
    
# Función para agregar un producto
def agregar_producto(session: Session, codigo: str, descripcion: str, categoria: str, imagen: str = None):
    """Agregar un nuevo producto a la base de datos."""
    try:
        nuevo_producto = Producto(
            codigo=codigo,
            descripcion=descripcion,
            categoria=categoria,
            imagen=imagen
        )
        session.add(nuevo_producto)
        session.commit()
        print("Producto agregado con éxito")
    except Exception as e:
        session.rollback()
        print(f"Error al agregar el producto: {e}")

# Función para obtener todos los productos
def obtener_productos(session: Session):
    """Obtener todos los productos de la base de datos."""
    try:
        productos = session.query(Producto).all()
        return productos
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return []

# Función para editar un producto existente
def editar_producto(session: Session, producto_id: int, datos_actualizados: dict):
    """Editar un producto existente en la base de datos."""
    try:
        producto = session.query(Producto).filter(Producto.id_producto == producto_id).first()
        if producto:
            for key, value in datos_actualizados.items():
                setattr(producto, key, value)
            session.commit()
            print(f"Producto {producto_id} editado con éxito")
        else:
            print(f"No se encontró el producto con ID {producto_id}")
    except Exception as e:
        session.rollback()
        print(f"Error al editar el producto: {e}")

# Función para eliminar un producto
def eliminar_producto(session: Session, producto_id: int):
    """Eliminar un producto de la base de datos."""
    try:
        producto = session.query(Producto).filter(Producto.id_producto == producto_id).first()
        if producto:
            session.delete(producto)
            session.commit()
            print(f"Producto {producto_id} eliminado con éxito")
        else:
            print(f"No se encontró el producto con ID {producto_id}")
    except Exception as e:
        session.rollback()
        print(f"Error al eliminar el producto: {e}")    



# Obtener movimientos históricos
def obtener_movimientos_historicos():
    db = next(get_db())  # Obtener sesión
    try:
        movimientos = db.query(Movimiento).all()  # Obtener todos los movimientos
        return [{"ubicacion": mov.ubicacion, "codigo": mov.codigo, "cantidad": mov.cantidad, 
                 "fecha": mov.fecha, "nota_devolucion": mov.nota_devolucion, "observaciones": mov.observaciones} 
                 for mov in movimientos]
    except Exception as e:
        print(f"Error al obtener movimientos históricos: {e}")
        return []
    finally:
        db.close()

# Obtener movimientos pendientes
def obtener_movimientos_pendientes():
    db = next(get_db())  # Obtener sesión
    try:
        pendientes = db.query(Pendiente).all()  # Obtener todos los pendientes
        return [{"ubicacion": p.ubicacion, "codigo": p.codigo, "cantidad": p.cantidad, 
                 "fecha": p.fecha, "motivo": p.motivo} for p in pendientes]
    except Exception as e:
        print(f"Error al obtener movimientos pendientes: {e}")
        return []
    finally:
        db.close()

# Generar un PDF con los movimientos proporcionados
def generar_pdf(movimientos, ruta_pdf):
    """Generar un PDF con los movimientos proporcionados."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar encabezado
    pdf.cell(200, 10, txt="Reporte de Movimientos", ln=True, align="C")

    # Agregar cada movimiento al PDF
    for mov in movimientos:
        pdf.cell(200, 10, txt=f"Ubicación: {mov.ubicacion}, Código: {mov.codigo}, Cantidad: {mov.cantidad}", ln=True)

    pdf.output(ruta_pdf)

# Exportar movimientos a un archivo CSV
def exportar_csv(movimientos, file_path):
    """Exportar movimientos a un archivo CSV."""
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Ubicación', 'Código', 'Cantidad', 'Fecha', 'Nota/Devolución', 'Observaciones'])
            for mov in movimientos:
                writer.writerow([mov.ubicacion, mov.codigo, mov.cantidad, mov.fecha, mov.nota_devolucion, mov.observaciones])
        print(f"CSV exportado a {file_path}")
    except Exception as e:
        print(f"Error al exportar CSV: {e}")