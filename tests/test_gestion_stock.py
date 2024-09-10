from PyQt5.QtWidgets import QApplication
from modules.gestion_stock import GestionStockView

import sys
import os

# Agregar la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    app = QApplication([])
    ventana = GestionStockView()
    ventana.show()
    app.exec_()
