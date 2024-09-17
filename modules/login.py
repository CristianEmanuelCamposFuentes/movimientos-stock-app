from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from modules.main_window import MainWindow  # Importar la ventana principal después del login
from PyQt5.QtCore import Qt
from modules.ui_styles import aplicar_estilos_especiales

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login de Usuario")
        self.setGeometry(300, 300, 400, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Etiquetas y campos de entrada
        usuario_label = QLabel("Usuario:")
        self.input_usuario = QLineEdit()
        contrasena_label = QLabel("Contraseña:")
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setEchoMode(QLineEdit.Password)

        # Añadir etiquetas y campos al layout
        layout.addWidget(usuario_label)
        layout.addWidget(self.input_usuario)
        layout.addWidget(contrasena_label)
        layout.addWidget(self.input_contrasena)

        # Botón de login
        btn_login = QPushButton("Login")
        btn_login.clicked.connect(self.validar_login)

        # Aplicar estilo especial al botón
        aplicar_estilos_especiales([btn_login], ["green"])

        # Añadir el botón al layout
        layout.addWidget(btn_login)

        # Establecer layout en la ventana
        self.setLayout(layout)

    def validar_login(self):
        """Valida las credenciales de login."""
        usuario = self.input_usuario.text()
        contrasena = self.input_contrasena.text()
        
        if usuario == "admin" and contrasena == "1234":
            QMessageBox.information(self, "Login Exitoso", f"Bienvenido, {usuario}!")
            self.abrir_ventana_principal(usuario)  # Abre la ventana principal tras login exitoso
        else:
            QMessageBox.warning(self, "Login Fallido", "Credenciales incorrectas. Por favor, inténtelo de nuevo.")

    def abrir_ventana_principal(self, usuario):
        """Abre la ventana principal y cierra la de login."""
        self.close()  # Cerrar la ventana de login

        # Abrir la ventana principal
        self.ventana_principal = MainWindow(usuario)
        self.ventana_principal.show()
