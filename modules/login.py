from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from modules.main_window import MainWindow  # Importar la ventana principal después del login
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login de Usuario")
        self.setGeometry(300, 300, 400, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Campos del formulario de login
        layout.addWidget(QLabel("Usuario:"))
        self.input_usuario = QLineEdit()
        layout.addWidget(self.input_usuario)

        layout.addWidget(QLabel("Contraseña:"))
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_contrasena)

        # Botón de login
        btn_login = QPushButton("Login")
        btn_login.clicked.connect(self.validar_login)
        layout.addWidget(btn_login)

        self.setLayout(layout)

    def validar_login(self):
        # Simulación de login para admin (usuario: admin, contraseña: 1234)
        usuario = self.input_usuario.text()
        contrasena = self.input_contrasena.text()
        
        if usuario == "admin" and contrasena == "1234":
            QMessageBox.information(self, "Login Exitoso", "Bienvenido, Admin!")
            self.abrir_ventana_principal(usuario)  # Abre la ventana principal tras login exitoso
        else:
            QMessageBox.warning(self, "Login Fallido", "Credenciales incorrectas.")

    def abrir_ventana_principal(self, usuario):
        # Ocultar la ventana de login
        self.close()

        # Abrir la ventana principal
        self.ventana_principal = MainWindow(usuario)
        self.ventana_principal.show()

