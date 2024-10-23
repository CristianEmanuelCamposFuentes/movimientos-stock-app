from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
import os
from modules.models.database_operations import importar_stock_con_backup

class ImportDataView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sobreescribir Stock desde CSV")

        # Layout principal
        main_layout = QVBoxLayout()

        # Botón para sobreescribir stock
        btn_sobreescribir_stock = QPushButton("Sobreescribir Stock desde CSV")
        btn_sobreescribir_stock.clicked.connect(self.confirmar_sobreescritura_stock)
        main_layout.addWidget(btn_sobreescribir_stock)

        self.setLayout(main_layout)

    def confirmar_sobreescritura_stock(self):
        """Mostrar cuadro de confirmación para sobreescribir el stock."""
        reply = QMessageBox.question(self, 'Confirmación de Sobreescritura', 
                                     "¿Estás seguro de que deseas sobreescribir el stock actual?\n"
                                     "Se realizará un backup antes de proceder.", 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.sobreescribir_stock()

    def sobreescribir_stock(self):
        """Función para sobreescribir el stock desde un archivo CSV."""
        # Ruta del archivo CSV
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'stock_actual.csv')

        try:
            # Llamar a la función que realiza el backup y sobreescribe el stock
            importar_stock_con_backup(csv_path)
            QMessageBox.information(self, "Éxito", "El stock ha sido sobreescrito y se ha realizado un backup.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al sobreescribir el stock: {str(e)}")
