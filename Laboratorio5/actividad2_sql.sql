CREATE TABLE Estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT
);

INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
('Juan', 20, 'Bogotá'),
('Ana', 22, 'Medellín'),
('Luis', 19, 'Cali');

SELECT * FROM Estudiantes;
SELECT * FROM Estudiantes WHERE ciudad = 'Medellín';
SELECT * FROM Estudiantes WHERE edad > 20;
