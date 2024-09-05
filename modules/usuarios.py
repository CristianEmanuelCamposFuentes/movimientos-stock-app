from PyQt5.QtWidgets import QMessageBox

def abrir_gestion_usuarios():
    msg = QMessageBox()
    msg.setWindowTitle("Gestión de Usuarios")
    msg.setText("Se abrirá la ventana para la gestión de usuarios.")
    msg.exec_()