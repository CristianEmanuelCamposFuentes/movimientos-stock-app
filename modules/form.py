import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from modules.stock_manager import process_data

def create_form():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gestión de Movimientos de Stock")

    # Crear los campos del formulario
    tk.Label(root, text="UBICACIÓN:").grid(row=0, column=0, padx=10, pady=5)
    entry_ubicacion = tk.Entry(root)
    entry_ubicacion.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="CÓDIGO:").grid(row=1, column=0, padx=10, pady=5)
    entry_codigo = tk.Entry(root)
    entry_codigo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="CANTIDAD:").grid(row=2, column=0, padx=10, pady=5)
    entry_cantidad = tk.Entry(root)
    entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="FECHA (DD/MM/YYYY):").grid(row=3, column=0, padx=10, pady=5)
    entry_fecha = tk.Entry(root)
    entry_fecha.grid(row=3, column=1, padx=10, pady=5)
    entry_fecha.insert(0, datetime.now().strftime('%d/%m/%Y'))

    tk.Label(root, text="NOTA/DEVOLUCIÓN:").grid(row=4, column=0, padx=10, pady=5)
    entry_nota_devolucion = tk.Entry(root)
    entry_nota_devolucion.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="TIPO DE MOVIMIENTO:").grid(row=5, column=0, padx=10, pady=5)
    combo_tipo_movimiento = ttk.Combobox(root, values=["Ingreso", "Egreso"])
    combo_tipo_movimiento.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(root, text="OBSERVACIONES:").grid(row=6, column=0, padx=10, pady=5)
    entry_observaciones = tk.Entry(root)
    entry_observaciones.grid(row=6, column=1, padx=10, pady=5)

    # Botón para enviar los datos
    submit_button = tk.Button(root, text="Registrar Movimiento", 
                              command=lambda: process_data(entry_ubicacion.get(), entry_codigo.get(), 
                                                           entry_cantidad.get(), validate_fecha(entry_fecha.get()), 
                                                           entry_nota_devolucion.get(), 
                                                           combo_tipo_movimiento.get(), 
                                                           entry_observaciones.get()))
    submit_button.grid(row=7, column=0, columnspan=2, pady=10)

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
