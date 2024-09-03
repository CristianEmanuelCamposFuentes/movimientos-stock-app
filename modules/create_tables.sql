-- Tabla para almacenar la relación entre pasillos y ubicaciones
CREATE TABLE IF NOT EXISTS Pasillos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pasillo TEXT NOT NULL,
    ubicacion TEXT NOT NULL UNIQUE
);

-- Tabla para productos
CREATE TABLE IF NOT EXISTS Productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL,
    categoria TEXT,
    imagen TEXT
);

-- Tabla para ubicaciones
CREATE TABLE IF NOT EXISTS Ubicaciones (
    id_ubicacion INTEGER PRIMARY KEY AUTOINCREMENT,
    pasillo TEXT NOT NULL,
    fila TEXT NOT NULL
);

-- Tabla de stock
CREATE TABLE IF NOT EXISTS Stock (
    id_stock INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER NOT NULL,
    id_ubicacion INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id_ubicacion)
);

-- Tabla para registrar movimientos
CREATE TABLE IF NOT EXISTS Movimientos (
    id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,
    ubicacion TEXT NOT NULL,
    codigo TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    nota_devolucion TEXT,
    tipo_movimiento TEXT NOT NULL,
    observaciones TEXT
);

-- Tabla para registrar incidentes de stock
CREATE TABLE IF NOT EXISTS Pendientes (
    id_pendiente INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER NOT NULL,
    id_ubicacion INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    motivo TEXT NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id_ubicacion)
);
