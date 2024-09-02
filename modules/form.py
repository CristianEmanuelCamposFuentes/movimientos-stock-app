import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from modules.stock_manager import process_data, get_description_by_code
from modules.database import get_db

def create_form():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gestión de Movimientos de Stock")
    root.geometry("500x400")
    root.minsize(400, 300)
    root.maxsize(800, 600)
    root.iconbitmap("img/inventario.png")
    root.configure(bg="skyblue")

    # Conectar con la base de datos
    db = next(get_db())

    # Crear los campos del formulario
    tk.Label(root, text="UBICACIÓN:").grid(row=0, column=0, padx=10, pady=5)
    entry_ubicacion = tk.Entry(root)
    entry_ubicacion.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="CÓDIGO:").grid(row=1, column=0, padx=10, pady=5)
    entry_codigo = tk.Entry(root)
    entry_codigo.grid(row=1, column=1, padx=10, pady=5)
    
    # Evento para autocompletar la descripción
    def on_codigo_change(event):
        codigo = entry_codigo.get()
        descripcion = get_description_by_code(db, codigo)
        if descripcion:
            entry_descripcion.delete(0, tk.END)
            entry_descripcion.insert(0, descripcion)
    
    entry_codigo.bind("<FocusOut>", on_codigo_change)

    tk.Label(root, text="DESCRIPCIÓN:").grid(row=2, column=0, padx=10, pady=5)
    entry_descripcion = tk.Entry(root)
    entry_descripcion.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="CANTIDAD:").grid(row=3, column=0, padx=10, pady=5)
    entry_cantidad = tk.Entry(root)
    entry_cantidad.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="FECHA (DD/MM/YYYY):").grid(row=4, column=0, padx=10, pady=5)
    entry_fecha = tk.Entry(root)
    entry_fecha.grid(row=4, column=1, padx=10, pady=5)
    entry_fecha.insert(0, datetime.now().strftime('%d/%m/%Y'))

    tk.Label(root, text="NOTA/DEVOLUCIÓN:").grid(row=5, column=0, padx=10, pady=5)
    entry_nota_devolucion = tk.Entry(root)
    entry_nota_devolucion.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(root, text="TIPO DE MOVIMIENTO:").grid(row=6, column=0, padx=10, pady=5)
    combo_tipo_movimiento = ttk.Combobox(root, values=["Ingreso", "Egreso"])
    combo_tipo_movimiento.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(root, text="OBSERVACIONES:").grid(row=7, column=0, padx=10, pady=5)
    entry_observaciones = tk.Entry(root)
    entry_observaciones.grid(row=7, column=1, padx=10, pady=5)

    # Validación de campos vacíos
    def validate_fields():
        if not entry_ubicacion.get() or not entry_codigo.get() or not entry_cantidad.get() or not combo_tipo_movimiento.get():
            messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
            return False
        return True

    # Botón para enviar los datos
    submit_button = tk.Button(root, text="Registrar Movimiento", 
                              command=lambda: process_data(
                                  entry_ubicacion.get(), 
                                  entry_codigo.get(), 
                                  entry_cantidad.get(), 
                                  validate_fecha(entry_fecha.get()), 
                                  entry_nota_devolucion.get(), 
                                  combo_tipo_movimiento.get(), 
                                  entry_observaciones.get()) if validate_fields() else None)
    submit_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Iniciar la aplicación
    root.mainloop()

def validate_fecha(fecha):
    try:
        if len(fecha) == 5:  # Si solo se ingresa dd/mm
            fecha += f"/{datetime.now().year}"  # Añadir el año actual
        # Convertir la fecha al formato dd/mm/yyyy
        datetime_obj = datetime.strptime(fecha, "%d/%m/%Y")
        return datetime_obj.strftime('%d/%m/%Y')
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha inválido. Usa dd/mm/yyyy.")
        return None

