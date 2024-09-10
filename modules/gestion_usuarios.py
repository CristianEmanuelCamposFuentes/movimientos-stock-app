from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
from modules.database_operations import obtener_usuarios, agregar_usuario, editar_usuario, eliminar_usuario

class GestionUsuariosView(QWidget):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Usuarios")
        layout = QVBoxLayout()

        # Tabla de usuarios
        self.table_usuarios = QTableWidget()
        self.table_usuarios.setColumnCount(3)  # ID, Nombre de usuario, Rol
        self.table_usuarios.setHorizontalHeaderLabels(["ID", "Nombre de Usuario", "Rol"])
        layout.addWidget(self.table_usuarios)

        # Cargar usuarios en la tabla
        self.cargar_usuarios()

        # Botones de acción
        buttons_layout = QHBoxLayout()

        # Botón para agregar usuario
        btn_agregar_usuario = QPushButton("Agregar Usuario")
        btn_agregar_usuario.clicked.connect(self.agregar_usuario)
        buttons_layout.addWidget(btn_agregar_usuario)

        # Botón para editar usuario
        btn_editar_usuario = QPushButton("Editar Usuario")
        btn_editar_usuario.clicked.connect(self.editar_usuario)
        buttons_layout.addWidget(btn_editar_usuario)

        # Botón para eliminar usuario
        btn_eliminar_usuario = QPushButton("Eliminar Usuario")
        btn_eliminar_usuario.clicked.connect(self.eliminar_usuario)
        buttons_layout.addWidget(btn_eliminar_usuario)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def cargar_usuarios(self):
        """Cargar los usuarios desde la base de datos y mostrarlos en la tabla."""
        usuarios = obtener_usuarios()
        self.table_usuarios.setRowCount(0)
        for row_idx, usuario in enumerate(usuarios):
            self.table_usuarios.insertRow(row_idx)
            self.table_usuarios.setItem(row_idx, 0, QTableWidgetItem(str(usuario.id)))
            self.table_usuarios.setItem(row_idx, 1, QTableWidgetItem(usuario.nombre))
            self.table_usuarios.setItem(row_idx, 2, QTableWidgetItem(usuario.rol))

    def agregar_usuario(self):
        """Función para agregar un nuevo usuario."""
        nombre_usuario, ok = QLineEdit.getText(self, "Agregar Usuario", "Nombre de Usuario:")
        if ok and nombre_usuario:
            agregar_usuario(nombre_usuario)
            QMessageBox.information(self, "Éxito", "Usuario agregado exitosamente.")
            self.cargar_usuarios()

    def editar_usuario(self):
        """Función para editar un usuario seleccionado."""
        row = self.table_usuarios.currentRow()
        if row >= 0:
            id_usuario = self.table_usuarios.item(row, 0).text()
            nuevo_nombre, ok = QLineEdit.getText(self, "Editar Usuario", "Nuevo Nombre de Usuario:")
            if ok and nuevo_nombre:
                editar_usuario(id_usuario, nuevo_nombre)
                QMessageBox.information(self, "Éxito", "Usuario editado exitosamente.")
                self.cargar_usuarios()
        else:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para editar.")

    def eliminar_usuario(self):
        """Función para eliminar un usuario seleccionado."""
        row = self.table_usuarios.currentRow()
        if row >= 0:
            id_usuario = self.table_usuarios.item(row, 0).text()
            eliminar_usuario(id_usuario)
            QMessageBox.information(self, "Éxito", "Usuario eliminado exitosamente.")
            self.cargar_usuarios()
        else:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para eliminar.")
