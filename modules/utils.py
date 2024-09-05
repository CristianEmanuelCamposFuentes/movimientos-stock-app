import pandas as pd
import sqlite3

def read_csv(file_path):
    return pd.read_csv(file_path)

def write_csv(df, file_path):
    df.to_csv(file_path, index=False)
    
def conectar_bd():
    # Función para conectar con la base de datos
    pass

def obtener_stock():
    # Función para obtener stock de la base de datos
    pass