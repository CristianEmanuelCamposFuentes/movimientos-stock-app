import pandas as pd
from tkinter import messagebox
from modules.utils import read_csv, write_csv

# Función para procesar los datos del formulario
def process_data(ubicacion, codigo, cantidad, fecha, nota_devolucion, tipo_movimiento, observaciones):
    if not ubicacion or not codigo or not cantidad or not fecha:
        messagebox.showerror("Error", "Todos los campos obligatorios deben estar completos")
        return

    cantidad = int(cantidad)

    # Guardar en el archivo de movimientos
    movement_data = {
        "Ubicacion": ubicacion,
        "Codigo": codigo,
        "Cantidad": cantidad,
        "Fecha": fecha,
        "Nota_Devolucion": nota_devolucion,
        "Tipo_Movimiento": tipo_movimiento,
        "Observaciones": observaciones
    }
    
    df_movimientos = pd.DataFrame([movement_data])
    df_movimientos.to_csv('movimientos/movimientos.csv', index=False, mode='a', header=False)

    # Actualizar el archivo de stock
    update_stock(ubicacion, codigo, cantidad, tipo_movimiento, fecha)

    messagebox.showinfo("Éxito", "El movimiento se ha registrado correctamente")

def update_stock(ubicacion, codigo, cantidad, tipo_movimiento, fecha):
    stock_file = 'data/stock_actual.csv'
    
    # Leer la tabla de stock actual
    df_stock = read_csv(stock_file)

    # Filtrar por ubicación y código
    stock_item = df_stock[(df_stock['UBICACION'] == ubicacion) & (df_stock['CODIGO'] == codigo)]

    if not stock_item.empty:
        if tipo_movimiento == "Ingreso":
            df_stock.loc[stock_item.index, 'CANTIDAD'] += cantidad
        elif tipo_movimiento == "Egreso":
            df_stock.loc[stock_item.index, 'CANTIDAD'] -= cantidad

        df_stock.loc[stock_item.index, 'FECHA'] = fecha
    else:
        new_stock = {
            'PASILLO': '',
            'UBICACION': ubicacion,
            'CODIGO': codigo,
            'DESCRIPCION': '',
            'CANTIDAD': cantidad if tipo_movimiento == "Ingreso" else -cantidad,
            'FECHA': fecha
        }
        df_stock = df_stock.append(new_stock, ignore_index=True)

    # Guardar los cambios en el archivo de stock
    write_csv(df_stock, stock_file)
