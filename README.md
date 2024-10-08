# Sistema de Gestión de Movimientos de Stock

## Descripción

Este proyecto es un sistema de gestión de stock diseñado para facilitar la administración de movimientos de inventario en una empresa de fabricación de chocolates y golosinas. El sistema permite el registro y seguimiento de movimientos de stock, gestión de productos, y manejo de usuarios, con funcionalidades para importar/exportar datos y realizar ajustes manuales.

## Funcionalidades

- **Inicio de Sesión**: Autenticación de usuarios con perfil Admin.
- **Gestión de Stock**: Visualización del stock actual, ajustes y movimientos.
- **Notas de Pedido**: Generación y carga de notas de pedido.
- **Registro de Movimientos**: Consulta y gestión de movimientos históricos y pendientes.
- **Gestión de Productos**: Añadir, editar y eliminar productos.
- **Gestión de Usuarios**: Crear, editar y eliminar usuarios.
- **Backup y Restauración**: Backup del stock actual y carga desde archivos CSV.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **PyQt6**: Framework para la creación de interfaces gráficas de usuario (GUI).
- **SQLAlchemy**: ORM para manejar la base de datos.
- **SQLite**: Sistema de gestión de base de datos.
- **FPDF**: Generación de archivos PDF.

## Requisitos

- Python 3.6 o superior
- PyQt6
- SQLAlchemy
- SQLite
- FPDF

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu-repositorio
    ```
3. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

## Uso
Ejecuta el archivo principal para iniciar la aplicación:

    ```bash
    python main.py
    ```
La interfaz se abrirá y podrás iniciar sesión con el usuario Admin y contraseña '1234'.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Fork el repositorio.
2. Crea una rama para tu contribución (git checkout -b feature/nueva-funcionalidad).
3. Realiza los cambios y commitea (git commit -am 'Añadir nueva funcionalidad').
4. Empuja los cambios (git push origin feature/nueva-funcionalidad).
5. Crea un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

Este README.md te proporcionará una base sólida para documentar tu proyecto en GitHub y guiará a otros sobre cómo instalar y utilizar tu sistema. ¡Avísame si necesitas más detalles o ajustes!





