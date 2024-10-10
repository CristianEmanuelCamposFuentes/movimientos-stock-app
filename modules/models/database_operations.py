import csv
import os
from sqlalchemy.orm import Session
from modules.models.database import Stock, Movimiento, NotasPedido, Producto, Pendiente, Usuario, engine
from datetime import datetime
from fpdf import FPDF
import bcrypt  # Para la seguridad en contraseñas
from modules.models.database import get_db

# Obtener el consolidado de stock actual
def obtener_stock(session: Session):
    """Obtiene todos los registros de stock actual"""
    return session.query(Stock).all()

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
            consolidado = db.query(Stock).join(Producto).filter(
                (Producto.codigo.contains(filtro)) | (Producto.descripcion.contains(filtro))
            ).all()
        else:
            consolidado = db.query(Stock).all()
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
        stock_item = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion, Producto.codigo == codigo).first()
        if stock_item:
            stock_item.cantidad = nueva_cantidad
            movimiento = Movimiento(
                ubicacion=ubicacion,
                codigo=codigo,
                cantidad=nueva_cantidad,
                fecha=datetime.now(),
                nota_devolucion="Ajuste manual",
                tipo_movimiento="Ajuste",
                observaciones="Ajuste de stock"
            )
            db.add(movimiento)
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
        stock_origen = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion_origen, Producto.codigo == codigo).first()
        if stock_origen and stock_origen.cantidad >= cantidad:
            stock_origen.cantidad -= cantidad
            stock_destino = db.query(Stock).join(Producto).filter(Stock.ubicacion == ubicacion_destino, Producto.codigo == codigo).first()
            if stock_destino:
                stock_destino.cantidad += cantidad
            else:
                nuevo_stock = Stock(
                    ubicacion=ubicacion_destino,
                    cantidad=cantidad,
                    id_producto=stock_origen.id_producto
                )
                db.add(nuevo_stock)

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

# Exportar movimientos a CSV
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

# Generar PDF con los movimientos
def generar_pdf(movimientos, ruta_pdf):
    """Generar un PDF con los movimientos proporcionados."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar encabezado
    pdf.cell(200, 10, txt="Reporte de Movimientos", ln=True, align="C")

    # Agregar cada movimiento al PDF
    for mov in movimientos:
        pdf.cell(200, 10, txt=f"Ubicación: {mov['ubicacion']}, Código: {mov['codigo']}, Cantidad: {mov['cantidad']}", ln=True)

    pdf.output(ruta_pdf)
    print(f"PDF generado en {ruta_pdf}")

# Función para agregar un nuevo usuario
def agregar_usuario(session: Session, nombre: str, rol: str, password: str):
    """Agrega un nuevo usuario con contraseña encriptada."""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    nuevo_usuario = Usuario(
        nombre=nombre,
        rol=rol,
        password=hashed_password,
        fecha_creacion=datetime.now()
    )
    session.add(nuevo_usuario)
    session.commit()
    print(f"Usuario {nombre} agregado con éxito.")

# Función para editar un usuario existente
def editar_usuario(session: Session, usuario_id: int, nombre: str, rol: str, password: str = None):
    """Edita un usuario existente."""
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        usuario.nombre = nombre
        usuario.rol = rol
        if password:  # Solo actualiza la contraseña si se proporciona
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            usuario.password = hashed_password
        session.commit()
        print(f"Usuario {nombre} actualizado con éxito.")
    else:
        print(f"Usuario con ID {usuario_id} no encontrado.")

# Función para generar una nueva nota de pedido
def generar_nota_pedido(session: Session, codigo: str, descripcion: str, cantidad: float, fecha: str, numero_nota: str = None):
    """
    Registra una nueva nota de pedido en la base de datos.
    """
    try:
        nueva_nota = NotasPedido(
            codigo=codigo,
            descripcion=descripcion,
            cantidad=cantidad,
            fecha_pedido=datetime.strptime(fecha, '%d/%m/%Y'),
            numero_nota=numero_nota
        )
        session.add(nueva_nota)
        session.commit()
        print("Nota de pedido generada con éxito")
    except Exception as e:
        session.rollback()
        print(f"Error al generar la nota de pedido: {e}")

def cargar_nota_pedido(session: Session, numero_nota: str):
    """
    Carga una nota de pedido por su número.
    """
    try:
        nota = session.query(NotasPedido).filter(NotasPedido.numero_nota == numero_nota).all()
        if not nota:
            return []
        
        return [{
            'codigo': item.codigo,
            'descripcion': session.query(Producto).filter(Producto.codigo == item.codigo).first().descripcion,
            'cantidad': item.cantidad,
            'ubicacion': session.query(Stock).filter(Stock.codigo == item.codigo).first().ubicacion if item else "Sin ubicación"
        } for item in nota]
        
    except Exception as e:
        print(f"Error al cargar la nota de pedido: {e}")
        return []

def obtener_registros_notas(session: Session, filtro=None):
    """
    Obtiene todas las notas de pedido con un filtro opcional.
    """
    try:
        query = session.query(NotasPedido)
        if filtro:
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
    """
    Agregar un nuevo producto a la base de datos.
    """
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

def obtener_productos(session: Session):
    """Obtener todos los productos de la base de datos."""
    try:
        productos = session.query(Producto).all()
        return productos
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return []

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

# Obtener los movimientos históricos
def obtener_movimientos_historicos(session: Session):
    """Obtiene todos los movimientos históricos registrados"""
    try:
        movimientos = session.query(Movimiento).all()
        return [{"ubicacion": mov.ubicacion, "codigo": mov.codigo, "cantidad": mov.cantidad, 
                 "fecha": mov.fecha.strftime('%d/%m/%Y'), "nota_devolucion": mov.nota_devolucion, "observaciones": mov.observaciones} 
                for mov in movimientos]
    except Exception as e:
        print(f"Error al obtener movimientos históricos: {e}")
        return []

# Obtener los movimientos pendientes
def obtener_movimientos_pendientes(session: Session):
    """Obtiene todos los movimientos pendientes registrados"""
    try:
        pendientes = session.query(Pendiente).all()
        return [{"ubicacion": p.ubicacion, "codigo": p.codigo, "cantidad": p.cantidad, 
                 "fecha": p.fecha.strftime('%d/%m/%Y'), "motivo": p.motivo} for p in pendientes]
    except Exception as e:
        print(f"Error al obtener movimientos pendientes: {e}")
        return []
    
# Función para obtener todos los usuarios
def obtener_usuarios(session: Session):
    """Obtiene todos los usuarios registrados en la base de datos"""
    try:
        usuarios = session.query(Usuario).all()
        return usuarios
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return []    
# Función para eliminar un usuario
def eliminar_usuario(session: Session, usuario_id: int):
    """Elimina un usuario de la base de datos"""
    usuario = session.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuario {usuario_id} eliminado con éxito")
    else:
        print(f"Usuario con ID {usuario_id} no encontrado.")    