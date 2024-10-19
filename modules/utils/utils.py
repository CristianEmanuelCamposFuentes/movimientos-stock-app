import pandas as pd
from PyQt6.QtWidgets import QMessageBox

def read_csv(file_path):
    """
    Lee un archivo CSV y lo devuelve como un DataFrame de pandas.
    Muestra un mensaje de error si ocurre algún problema.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Error al leer el archivo CSV: {e}")
        return None

def write_csv(df, file_path):
    """
    Escribe un DataFrame de pandas a un archivo CSV.
    Muestra un mensaje de error si ocurre algún problema.
    """
    try:
        df.to_csv(file_path, index=False)
        QMessageBox.information(None, "Éxito", f"CSV guardado exitosamente en {file_path}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Error al guardar el archivo CSV: {e}")

def export_to_excel(df, file_path):
    """
    Escribe un DataFrame de pandas a un archivo Excel.
    Muestra un mensaje de éxito o error dependiendo del resultado.
    """
    try:
        df.to_excel(file_path, index=False)
        QMessageBox.information(None, "Éxito", f"Excel guardado exitosamente en {file_path}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Error al guardar el archivo Excel: {e}")

def export_to_pdf(data, file_path):
    """
    Placeholder para la función de exportar a PDF.
    Actualmente no implementada.
    """
    QMessageBox.information(None, "Función no disponible", "La exportación a PDF está en desarrollo.")

def validate_dataframe(df):
    """
    Valida un DataFrame de pandas para asegurarse de que tiene contenido válido.
    """
    if df is None or df.empty:
        QMessageBox.critical(None, "Error", "El DataFrame está vacío o no es válido.")
        return False
    return True
