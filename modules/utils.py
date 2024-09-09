import pandas as pd

def read_csv(file_path):
    """Lee un archivo CSV y lo devuelve como un DataFrame de pandas."""
    return pd.read_csv(file_path)

def write_csv(df, file_path):
    """Escribe un DataFrame de pandas a un archivo CSV."""
    df.to_csv(file_path, index=False)
    
def export_to_excel(df, file_path):
    """Escribe un DataFrame de pandas a un archivo Excel."""
    df.to_excel(file_path, index=False)

def export_to_pdf(data, file_path):
    """Función futura para exportar datos a PDF (placeholder por ahora)."""
    pass
