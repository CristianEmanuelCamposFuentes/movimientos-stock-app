import csv
import os
from sqlalchemy.orm import Session
from database import Stock, engine
from datetime import datetime

def import_stock_data(csv_file):
    session = Session(bind=engine)
    
    with open(csv_file, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        
        # Verificar los encabezados
        headers = reader.fieldnames
        print(f"Encabezados encontrados: {headers}")  # Mostrar los encabezados

        # Proceso para agregar cada fila a la base de datos
        for row in reader:
            try:
                # Convertir la cantidad reemplazando la coma por un punto
                cantidad = float(row['CANTIDAD'].replace(',', '.')) if row['CANTIDAD'].strip() else 0.0

                # Convertir la fecha al formato adecuado si es necesario
                fecha = procesar_fecha(row['FECHA'])

                # Reemplazar puntos por comas y convertir a mayúsculas en la ubicación
                ubicacion = row['UBICACION'].replace('.', ',').upper()

                # Convertir el código a mayúsculas
                codigo = row['CODIGO'].upper() if row['CODIGO'].strip() else ''

                stock_item = Stock(
                    pasillo=row['PASILLO'].upper(),
                    ubicacion=ubicacion,
                    codigo=codigo,
                    descripcion=row['DESCRIPCION'].upper(),
                    cantidad=cantidad,  # Usamos la cantidad ya convertida
                    fecha=fecha
                )
                session.add(stock_item)
            except KeyError as e:
                print(f"Error: columna {e} no encontrada en el archivo CSV.")
                continue
            except ValueError as e:
                print(f"Error procesando fila {row}: {e}")
                continue
            except Exception as e:
                print(f"Error procesando fila {row}: {e}")
                continue

        session.commit()
    session.close()

def procesar_fecha(fecha_str):
    if not fecha_str.strip():  # Si la fecha está vacía
        return None  # O algún valor por defecto, si es necesario
    return datetime.strptime(fecha_str, '%d/%m/%Y')

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '..', 'data', 'stock_actual.csv')
    import_stock_data(csv_path)
