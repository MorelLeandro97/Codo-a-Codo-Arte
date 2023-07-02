USE proyectocac;

CREATE TABLE productos_artisticos(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nombre VARCHAR(50) NOT NULL DEFAULT "",
    precio INT NOT NULL DEFAULT 0,
    stock INT NOT NULL DEFAULT 0
);

INSERT INTO productos_artisticos(nombre, precio, stock) VALUES('Atril 1.30', 4000, 10);
INSERT INTO productos_artisticos(nombre, precio, stock) VALUES('Atril 1.80', 8000, 20);
INSERT INTO productos_artisticos(nombre, precio, stock) VALUES('Lienzo 20x30', 3200, 6);
INSERT INTO productos_artisticos(nombre, precio, stock) VALUES('Lienzo 30x28', 4200, 20);
INSERT INTO productos_artisticos(nombre, precio, stock) VALUES('Lienzo 40x60', 6000, 8);


SELECT * FROM productos_artisticos;