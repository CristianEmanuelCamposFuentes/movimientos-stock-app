import csv
import os
from sqlalchemy.orm import Session
from modules.database import StockActual, engine

def import_stock_data(csv_file):
    session = Session(bind=engine)
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            stock_item = StockActual(
                pasillo=row['PASILLO'],
                ubicacion=row['UBICACION'],
                codigo=row['CODIGO'],
                descripcion=row['DESCRIPCION'],
                cantidad=float(row['CANTIDAD']),
                fecha=row['FECHA']
            )
            session.add(stock_item)
        session.commit()
    session.close()

if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio de este script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construir la ruta del archivo CSV relativa al directorio de este script
    csv_path = os.path.join(base_dir, '..', 'data', 'stock_actual.csv')
    
    import_stock_data(csv_path)

