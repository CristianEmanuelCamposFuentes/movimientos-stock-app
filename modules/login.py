from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from modules.main_window import MainWindow  # Importar la ventana principal
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(400, 200, 300, 200)

        # Crear el formulario de login
        layout = QVBoxLayout()

        self.label_usuario = QLabel("Usuario:")
        layout.addWidget(self.label_usuario)

        self.input_usuario = QLineEdit()
        layout.addWidget(self.input_usuario)

        self.label_contraseña = QLabel("Contraseña:")
        layout.addWidget(self.label_contraseña)

        self.input_contraseña = QLineEdit()
        self.input_contraseña.setEchoMode(QLineEdit.Password)  # Para ocultar la contraseña
        layout.addWidget(self.input_contraseña)

        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.accept_login)  # Conectar el botón al método de login
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def accept_login(self):
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()

        # Validar usuario y contraseña (esto es solo un ejemplo simple)
        if usuario == "Admin" and contraseña == "1234":
            QMessageBox.information(self, "Login Correcto", "Bienvenido, " + usuario)

            # Abrir la ventana principal y pasar el usuario como argumento
            self.abrir_ventana_principal(usuario)
        else:
            QMessageBox.warning(self, "Login Incorrecto", "Usuario o contraseña incorrectos. Intente de nuevo.")

    def abrir_ventana_principal(self, usuario):
        # Cerrar la ventana de login
        self.close()

        # Crear una instancia de la ventana principal y pasar el usuario
        self.ventana_principal = MainWindow(usuario)
        self.ventana_principal.show()
