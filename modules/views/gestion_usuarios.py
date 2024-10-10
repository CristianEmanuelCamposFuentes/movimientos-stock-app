from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QInputDialog
from modules.models.database_operations import obtener_usuarios, agregar_usuario, editar_usuario, eliminar_usuario
from modules.models.database import get_db
from modules.utils.ui_styles import aplicar_estilos_especiales

class GestionUsuariosView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario = parent.usuario if parent else None  # Obtener usuario desde el parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Usuarios")

        # Layout principal
        main_layout = QVBoxLayout()

        # Tabla de usuarios
        self.table_usuarios = QTableWidget()
        self.table_usuarios.setColumnCount(3)  # ID, Nombre de usuario, Rol
        self.table_usuarios.setHorizontalHeaderLabels(["ID", "Nombre de Usuario", "Rol"])
        main_layout.addWidget(self.table_usuarios)

        # Cargar usuarios en la tabla
        self.cargar_usuarios()

        # Generar la barra de botones inferior personalizada para esta vista
        botones = [
            {"texto": "Agregar Usuario", "color": "green", "funcion": self.agregar_usuario},
            {"texto": "Editar Usuario", "color": "blue", "funcion": self.editar_usuario},
            {"texto": "Eliminar Usuario", "color": "red", "funcion": self.eliminar_usuario},
        ]
        bottom_bar = self.parent.crear_barra_botones_inferiores(botones)

        # Añadir la barra de botones al layout principal
        main_layout.addLayout(bottom_bar)

        # Aplicar el layout final a la ventana
        self.setLayout(main_layout)

    def cargar_usuarios(self):
        """Cargar los usuarios desde la base de datos y mostrarlos en la tabla."""
        db = next(get_db())  # Obtener la sesión de la base de datos
        try:
            usuarios = obtener_usuarios(db)  # Obtener los usuarios
            self.table_usuarios.setRowCount(0)
            for row_idx, usuario in enumerate(usuarios):
                self.table_usuarios.insertRow(row_idx)
                self.table_usuarios.setItem(row_idx, 0, QTableWidgetItem(str(usuario.id_usuario)))
                self.table_usuarios.setItem(row_idx, 1, QTableWidgetItem(usuario.nombre))
                self.table_usuarios.setItem(row_idx, 2, QTableWidgetItem(usuario.rol))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar usuarios: {e}")
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
                        agregar_usuario(db, nombre_usuario, rol_usuario, password_usuario)
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
                            editar_usuario(db, id_usuario, nuevo_nombre, nuevo_rol, nueva_password)
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
                eliminar_usuario(db, id_usuario)
                QMessageBox.information(self, "Éxito", "Usuario eliminado exitosamente.")
                self.cargar_usuarios()  # Actualizar la tabla
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar usuario: {e}")
            finally:
                db.close()
        else:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para eliminar.")
