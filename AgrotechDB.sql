-- SENTENCIAS DDL
-- ==============

-- Primero creamos la Base de Datos mediante el siguiente comando.

CREATE DATABASE AgrotechDB;

-- Seleccionamos la BBDD a utilizar

USE AgroTechDB;

-- Procedemos a la Creación de las Tablas

-- Tabla "Parcelas"

CREATE TABLE Parcelas (
    Id_Parcela INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Ubicacion VARCHAR(50),
    Latitud DECIMAL(9,6),
    Longitud DECIMAL(9,6),
    Tamaño_Hectareas DECIMAL(10,2),
    Tipo_Cultivo VARCHAR(50)
);

-- Tabla "TipoSensor"

CREATE TABLE TipoSensor (
    Id_Tipo_Sensor INT PRIMARY KEY,
    Nombre_Sensor VARCHAR(50),
    Modelo_Sensor VARCHAR(50)
);

-- Tabla "Sensores"

CREATE TABLE Sensores (
    Id_Sensor INT PRIMARY KEY,
    Id_Parcela INT,
    Id_Tipo_Sensor INT,
    Fecha_Instalacion DATE,
    FOREIGN KEY (Id_Parcela) REFERENCES Parcelas(Id_Parcela),
    FOREIGN KEY (Id_Tipo_Sensor) REFERENCES TipoSensor(Id_Tipo_Sensor)
);

-- Tabla "Medición"

CREATE TABLE Medicion (
    Id_Medida INT PRIMARY KEY,
    Id_Sensor INT,
    Valor_Medicion DECIMAL(10,2),
    Unidad VARCHAR(10),
    Fecha_Hora DATETIME,
    FOREIGN KEY (Id_Sensor) REFERENCES Sensores(Id_Sensor)
);

-- Tabla "Alertas"

CREATE TABLE Alerta (
    Id_Alerta INT PRIMARY KEY,
    Id_Tipo_Sensor INT,
    Umbral_Minimo DECIMAL(10,2),
    Umbral_Maximo DECIMAL(10,2),
    Descripcion_Alerta TEXT,
    Fecha_Creacion DATETIME,
    FOREIGN KEY (Id_Tipo_Sensor) REFERENCES TipoSensor(Id_Tipo_Sensor)
);



-- SENTENCIAS DML - INSERT
-- =======================


-- Insertamos datos parcelas

INSERT INTO Parcelas VALUES
(1, 'Parcela Norte', 'Campo X - Zona 1', -31.420083, -64.188776, 15.50, 'Maíz'),
(2, 'Parcela Sur', 'Campo X - Zona 2', -31.422100, -64.190010, 10.75, 'Soja'),
(3, 'Parcela Este', 'Campo Y - Zona 3', -31.419500, -64.185900, 8.25, 'Trigo');

-- Insertamos tipos de sensores

INSERT INTO TipoSensor VALUES
(1, 'Temperatura', 'TempX-100'),
(2, 'Humedad', 'HumY-200'),
(3, 'pH', 'pHZ-300');

-- Insertamos sensores

INSERT INTO Sensores VALUES
(1, 1, 1, '2024-01-10'),
(2, 1, 2, '2024-01-15'),
(3, 2, 1, '2024-02-01');

-- Insertamos mediciones

INSERT INTO Medicion VALUES
(1, 1, 23.5, '°C', '2024-06-01 08:00:00'),
(2, 2, 45.2, '%', '2024-06-01 08:05:00'),
(3, 3, 22.8, '°C', '2024-06-01 08:10:00');

-- Insertamos alertas

INSERT INTO Alerta VALUES
(1, 1, 5.00, 35.00, 'Temperatura fuera de rango aceptable.', '2024-01-01 00:00:00'),
(2, 2, 30.00, 70.00, 'Humedad crítica para el cultivo.', '2024-01-01 00:00:00'),
(3, 3, 6.00, 7.50, 'Niveles de pH no recomendados.', '2024-01-01 00:00:00');



-- SENTENCIAS DML - SELECT
-- =======================


-- 1. Listamos todos los registros de parcelas de la tabla Parcelas.
SELECT * FROM Parcelas;

-- 2. Mostramos los sensores instalados en una parcela específica.
SELECT * FROM Sensores WHERE Id_Parcela = 3;

-- 3. Mostramos las últimas 2 mediciones registradas
SELECT * FROM Medicion ORDER BY Fecha_Hora DESC LIMIT 2;

-- 4. Listamos los sensores con su tipo de Sensor correspondiente
SELECT s.Id_Sensor, s.Id_Parcela, t.Nombre_Sensor
FROM Sensores s
JOIN TipoSensor t ON s.Id_Tipo_Sensor = t.Id_Tipo_Sensor;

-- 5. Mostrar las mediciones registradas en un rango de fechas específico
SELECT * FROM Medicion WHERE Fecha_Hora BETWEEN '2024-06-01 00:00:00' AND '2024-06-01 23:59:59';

-- 6. Mostrar todas las alertas con umbral maximo mayor a 70
SELECT * FROM Alerta WHERE Umbral_Maximo > 70;

-- 7. Mostra un conteo de las mediciones por Sensor
SELECT Id_Sensor, COUNT(*) AS Total_Mediciones FROM Medicion GROUP BY Id_Sensor;