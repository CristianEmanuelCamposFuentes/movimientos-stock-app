from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QInputDialog
from modules.database_operations import obtener_usuarios, agregar_usuario, editar_usuario, eliminar_usuario
from modules.database import get_db

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
        db = next(get_db())  # Obtener la sesión de la base de datos
        try:
            usuarios = obtener_usuarios(db)  # Pasar la sesión activa
            self.table_usuarios.setRowCount(0)
            for row_idx, usuario in enumerate(usuarios):
                self.table_usuarios.insertRow(row_idx)
                self.table_usuarios.setItem(row_idx, 0, QTableWidgetItem(str(usuario.id_usuario)))
                self.table_usuarios.setItem(row_idx, 1, QTableWidgetItem(usuario.nombre))
                self.table_usuarios.setItem(row_idx, 2, QTableWidgetItem(usuario.rol))
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")
        finally:
            db.close()

    def agregar_usuario(self):
        """Función para agregar un nuevo usuario."""
        nombre_usuario, ok = QInputDialog.getText(self, "Agregar Usuario", "Nombre de Usuario:")
        if ok and nombre_usuario:
            rol_usuario, ok = QInputDialog.getText(self, "Agregar Usuario", "Rol del Usuario:")
            if ok and rol_usuario:
                password_usuario, ok = QInputDialog.getText(self, "Agregar Usuario", "Contraseña del Usuario:")
                if ok and password_usuario:
                    db = next(get_db())  # Obtener la sesión de la base de datos
                    try:
                        agregar_usuario(db, nombre_usuario, rol_usuario, password_usuario)  # Pasar la sesión
                        QMessageBox.information(self, "Éxito", "Usuario agregado exitosamente.")
                        self.cargar_usuarios()  # Actualizar la tabla
                    except Exception as e:
                        QMessageBox.critical(self, "Error", f"Error al agregar usuario: {e}")
                    finally:
                        db.close()

    def editar_usuario(self):
        """Función para editar un usuario seleccionado."""
        row = self.table_usuarios.currentRow()
        if row >= 0:
            id_usuario = self.table_usuarios.item(row, 0).text()
            nuevo_nombre, ok = QInputDialog.getText(self, "Editar Usuario", "Nuevo Nombre de Usuario:")
            if ok and nuevo_nombre:
                nuevo_rol, ok = QInputDialog.getText(self, "Editar Usuario", "Nuevo Rol del Usuario:")
                if ok and nuevo_rol:
                    nueva_password, ok = QInputDialog.getText(self, "Editar Usuario", "Nueva Contraseña (opcional):", QLineEdit.Normal)
                    if ok:
                        db = next(get_db())  # Obtener la sesión de la base de datos
                        try:
                            editar_usuario(db, id_usuario, nuevo_nombre, nuevo_rol, nueva_password)  # Pasar la sesión
                            QMessageBox.information(self, "Éxito", "Usuario editado exitosamente.")
                            self.cargar_usuarios()  # Actualizar la tabla
                        except Exception as e:
                            QMessageBox.critical(self, "Error", f"Error al editar usuario: {e}")
                        finally:
                            db.close()
        else:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para editar.")

    def eliminar_usuario(self):
        """Función para eliminar un usuario seleccionado."""
        row = self.table_usuarios.currentRow()
        if row >= 0:
            id_usuario = self.table_usuarios.item(row, 0).text()
            db = next(get_db())  # Obtener la sesión de la base de datos
            try:
                eliminar_usuario(db, id_usuario)  # Pasar la sesión
                QMessageBox.information(self, "Éxito", "Usuario eliminado exitosamente.")
                self.cargar_usuarios()  # Actualizar la tabla
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar usuario: {e}")
            finally:
                db.close()
        else:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para eliminar.")
