from sqlalchemy.orm import Session
from modules.database import StockActual, Movimientos, get_db, NotasPedido, Usuarios, Productos, Pendientes
from datetime import datetime

# Obtener el consolidado de stock actual
def obtener_stock(session: Session):
    """Obtiene todos los registros de stock actual"""
    return session.query(StockActual).all()

# Registrar un nuevo movimiento
def registrar_movimiento(session: Session, movimiento_data):
    """Registra un nuevo movimiento en la base de datos"""
    nuevo_movimiento = Movimientos(**movimiento_data)
    session.add(nuevo_movimiento)
    session.commit()

# Obtener el consolidado de stock con un filtro opcional
def obtener_consolidado_stock(filtro=None):
    db = next(get_db())
    try:
        if filtro:
            # Aplicar el filtro para buscar registros específicos
            consolidado = db.query(StockActual).filter(StockActual.codigo.contains(filtro) | StockActual.descripcion.contains(filtro)).all()
        else:
            # Devolver todos los registros si no hay filtro
            consolidado = db.query(StockActual).all()
        print(f"Consolidado encontrado: {consolidado}")         
        return consolidado
    except Exception as e:
        print(f"Error al obtener el consolidado de stock: {e}")
        return []
    finally:
        db.close()

# Realizar ajuste de stock
def realizar_ajuste_stock(ubicacion: str, codigo: str, nueva_cantidad: float):
    db = next(get_db())
    try:
        stock_item = db.query(StockActual).filter(StockActual.ubicacion == ubicacion, StockActual.codigo == codigo).first()
        if stock_item:
            stock_item.cantidad = nueva_cantidad
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
        stock_origen = db.query(StockActual).filter(StockActual.ubicacion == ubicacion_origen, StockActual.codigo == codigo).first()
        if stock_origen and stock_origen.cantidad >= cantidad:
            stock_origen.cantidad -= cantidad
            stock_destino = db.query(StockActual).filter(StockActual.ubicacion == ubicacion_destino, StockActual.codigo == codigo).first()
            if stock_destino:
                stock_destino.cantidad += cantidad
            else:
                nuevo_stock = StockActual(
                    ubicacion=ubicacion_destino,
                    codigo=codigo,
                    descripcion=stock_origen.descripcion,
                    cantidad=cantidad,
                    pasillo=stock_origen.pasillo,
                    fecha=stock_origen.fecha
                )
                db.add(nuevo_stock)
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
    """Genera una nueva nota de pedido y la guarda en la base de datos"""
    nueva_nota = NotasPedido(
        codigo=codigo,
        descripcion=descripcion,
        cantidad=cantidad,
        fecha=fecha,
        numero_nota=numero_nota
    )
    session.add(nueva_nota)
    session.commit()

# Función para cargar una nota de pedido existente (usada para actualizarla)
def cargar_nota_pedido(session: Session, numero_nota: str):
    """Carga una nota de pedido por su número"""
    return session.query(NotasPedido).filter(NotasPedido.numero_nota == numero_nota).all()

# Función para obtener todos los registros de notas de pedido
def obtener_registros_notas(session: Session):
    """Obtiene todas las notas de pedido"""
    return session.query(NotasPedido).all()

# Función para agregar un producto
def agregar_producto(session: Session, codigo: str, descripcion: str, categoria: str, imagen: str = None):
    """Agregar un nuevo producto a la base de datos"""
    nuevo_producto = Productos(
        codigo=codigo,
        descripcion=descripcion,
        categoria=categoria,
        imagen=imagen
    )
    session.add(nuevo_producto)
    session.commit()

# Función para obtener todos los productos
def obtener_productos(session: Session):
    """Obtener todos los productos de la base de datos"""
    return session.query(Productos).all()

# Función para editar un producto existente
def editar_producto(session: Session, producto_id: int, datos_actualizados: dict):
    """Editar un producto existente en la base de datos"""
    producto = session.query(Productos).filter(Productos.id_producto == producto_id).first()
    if producto:
        for key, value in datos_actualizados.items():
            setattr(producto, key, value)
        session.commit()

# Función para eliminar un producto
def eliminar_producto(session: Session, producto_id: int):
    """Eliminar un producto de la base de datos"""
    producto = session.query(Productos).filter(Productos.id_producto == producto_id).first()
    if producto:
        session.delete(producto)
        session.commit()
        
def obtener_usuarios():
    """Obtener la lista de usuarios desde la base de datos."""
    db = next(get_db())
    usuarios = db.query(Usuarios).all()
    db.close()
    return usuarios

def agregar_usuario(nombre):
    """Agregar un nuevo usuario a la base de datos."""
    db = next(get_db())
    nuevo_usuario = Usuarios(nombre=nombre, rol="Usuario")  # Puedes cambiar el rol según sea necesario
    db.add(nuevo_usuario)
    db.commit()
    db.close()

def editar_usuario(id_usuario, nuevo_nombre):
    """Editar un usuario existente."""
    db = next(get_db())
    usuario = db.query(Usuarios).filter(Usuarios.id == id_usuario).first()
    if usuario:
        usuario.nombre = nuevo_nombre
        db.commit()
    db.close()

def eliminar_usuario(id_usuario):
    """Eliminar un usuario de la base de datos."""
    db = next(get_db())
    usuario = db.query(Usuarios).filter(Usuarios.id == id_usuario).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    db.close()        
    
    
# Obtener los movimientos históricos
def obtener_movimientos_historicos():
    """Obtener la lista de movimientos históricos."""
    db = next(get_db())
    movimientos = db.query(Movimientos).all()
    db.close()
    return movimientos

# Obtener los movimientos pendientes
def obtener_movimientos_pendientes():
    """Obtener la lista de movimientos pendientes."""
    # Aquí asumo que hay un campo o tabla que guarda los pendientes
    # Si no, se debería agregar una tabla o campo específico
    db = next(get_db())
    pendientes = db.query(Movimientos).filter(Movimientos.tipo_movimiento == 'Pendiente').all()
    db.close()
    return pendientes

# Función para generar PDF (requerirá una librería como ReportLab o similar)
def generar_pdf(movimientos):
    """Generar un PDF con los movimientos proporcionados."""
    # Implementar la lógica para generar un PDF usando movimientos
    pass

# Función para exportar CSV
def exportar_csv(movimientos, file_path):
    """Exportar movimientos a un archivo CSV."""
    import csv
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Ubicación', 'Código', 'Cantidad', 'Fecha', 'Nota/Devolución', 'Tipo Movimiento', 'Observaciones'])
        for mov in movimientos:
            writer.writerow([mov.id, mov.ubicacion, mov.codigo, mov.cantidad, mov.fecha, mov.nota_devolucion, mov.tipo_movimiento, mov.observaciones])    
            
# Función para registrar un movimiento pendiente
def registrar_pendiente(session: Session, codigo: str, descripcion: str, cantidad: float, fecha: str, motivo: str, ubicacion: str = None):
    pendiente = Pendientes(
        codigo=codigo,
        descripcion=descripcion,
        cantidad=cantidad,
        fecha=datetime.strptime(fecha, "%d/%m/%Y"),
        motivo=motivo,
        ubicacion=ubicacion
    )
    session.add(pendiente)
    session.commit()

# Función para procesar movimientos con la opción "Sin ubicación"
def process_movement(ubicacion: str, codigo: str, cantidad: float, fecha: str, tipo_movimiento: str, motivo: str, observaciones: str):
    db = next(get_db())
    try:
        cantidad = float(cantidad)
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        
        # Opción "Sin ubicación"
        if ubicacion == "Sin ubicación":
            registrar_pendiente(db, codigo, get_description_by_code(db, codigo), cantidad, fecha.strftime('%d/%m/%Y'), motivo, ubicacion)
            return "Movimiento registrado como 'Sin ubicación' en la tabla de pendientes."
        
        # Caso normal (ubicación regular)
        stock_item = db.query(StockActual).filter(StockActual.ubicacion == ubicacion, StockActual.codigo == codigo).first()

        if tipo_movimiento == "Ingreso":
            if stock_item:
                stock_item.cantidad += cantidad
            else:
                # Crear un nuevo registro si no existe
                new_stock = StockActual(
                    pasillo='Pasillo desconocido',  # Ajustar esto con el valor adecuado
                    ubicacion=ubicacion,
                    codigo=codigo,
                    descripcion=get_description_by_code(db, codigo),
                    cantidad=cantidad,
                    fecha=fecha
                )
                db.add(new_stock)
        elif tipo_movimiento == "Egreso":
            if stock_item and stock_item.cantidad >= cantidad:
                stock_item.cantidad -= cantidad
            else:
                registrar_pendiente(db, codigo, get_description_by_code(db, codigo), cantidad, fecha.strftime('%d/%m/%Y'), "Cantidad insuficiente", ubicacion)
                return "Movimiento registrado como pendiente por cantidad insuficiente."

        # Registrar el movimiento
        movimiento = Movimientos(
            ubicacion=ubicacion,
            codigo=codigo,
            cantidad=cantidad,
            fecha=fecha,
            nota_devolucion=motivo,
            tipo_movimiento=tipo_movimiento,
            observaciones=observaciones
        )
        db.add(movimiento)
        db.commit()
        return "Movimiento registrado con éxito."
    
    except Exception as e:
        db.rollback()
        return str(e)
    finally:
        db.close()      
        
# Función para obtener la descripción del producto dado su código
def get_description_by_code(db: Session, codigo: str) -> str:
    """Obtener la descripción del producto dado su código."""
    stock_item = db.query(StockActual).filter(StockActual.codigo == codigo).first()
    if stock_item:
        return stock_item.descripcion
    return "Descripción no encontrada"              