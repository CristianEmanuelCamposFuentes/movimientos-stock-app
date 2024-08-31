import csv
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
    import_stock_data("../data/stock_actual.csv")
