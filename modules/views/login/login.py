from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.uic import loadUi
from modules.views.main_window.main_window import MainWindow  # Importar la ventana principal después del login
from modules.utils.ui_styles import aplicar_estilos_especiales

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("ruta/al/archivo/login.ui", self)  # Cargar el archivo .ui

        # Conectar el botón de login a la función de validación
        self.btn_login.clicked.connect(self.validar_login)

        # Aplicar estilos al botón
        aplicar_estilos_especiales([self.btn_login], ["green"])

    def validar_login(self):
        """Valida las credenciales de login."""
        usuario = self.input_usuario.text()
        contrasena = self.input_contrasena.text()
        
        if usuario == "admin" and contrasena == "1234":
            QMessageBox.information(self, "Login Exitoso", f"Bienvenido, {usuario}!")
            self.abrir_ventana_principal(usuario)
        else:
            QMessageBox.warning(self, "Login Fallido", "Credenciales incorrectas. Por favor, inténtelo de nuevo.")

    def abrir_ventana_principal(self, usuario):
        """Abre la ventana principal y cierra la de login."""
        self.close()  # Cerrar la ventana de login
        self.ventana_principal = MainWindow(usuario)
        self.ventana_principal.show()

