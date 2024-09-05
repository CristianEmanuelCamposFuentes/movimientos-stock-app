from PyQt5.QtWidgets import QMessageBox

def abrir_nota_pedido():
    msg = QMessageBox()
    msg.setWindowTitle("Generar Nota de Pedido")
    msg.setText("Se abrirá la ventana para generar una nota de pedido.")
    msg.exec_()