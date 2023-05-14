--PRIMERA CONSULTA
SELECT b.cedula, b.nombre
FROM BEBEDOR b
WHERE b.cedula NOT IN (
  SELECT g.cedula
  FROM GUSTA g
  INNER JOIN BEBIDA bd ON g.codigo_bebida = bd.codigo_bebida
  WHERE bd.nombre_bebida = 'colombiana'
);

--SEGUNDA CONSULTA
SELECT 	t.nombre_tienda 
FROM TIENDA t
WHERE t.codigo_tienda NOT IN (
  SELECT f.codigo_tienda
  FROM FRECUENTA f
  INNER JOIN BEBEDOR bebedor ON f.cedula = bebedor.cedula
  WHERE bebedor.nombre = 'Andres Camilo Restrepo'
);

--TERCERA CONSULTA
SELECT DISTINCT b.cedula, b.nombre
FROM BEBEDOR b
INNER JOIN GUSTA g ON b.cedula = g.cedula
INNER JOIN FRECUENTA f ON b.cedula = f.cedula;

--CUARTA CONSULTA
SELECT br.cedula, br.nombre, b.nombre_bebida
FROM BEBIDA b, BEBEDOR br
WHERE NOT EXISTS (
  SELECT * 
  FROM GUSTA g 
  WHERE br.cedula = g.cedula AND b.codigo_bebida = g.codigo_bebida
);

--QUINTA CONSULTA
SELECT DISTINCT b.cedula, b.nombre
FROM BEBEDOR b
INNER JOIN FRECUENTA ff ON b.cedula = ff.cedula
WHERE ff.codigo_tienda IN(
  SELECT f.codigo_tienda
  FROM FRECUENTA f
  INNER JOIN BEBEDOR b ON f.cedula = b.cedula
  WHERE b.nombre = 'Luis Perez'
)AND b.nombre != 'Luis Perez';

--SEXTA CONSULTA
SELECT DISTINCT b.cedula, b.nombre
FROM BEBEDOR b
WHERE NOT EXISTS (
    SELECT *
    FROM TIENDA t
    WHERE NOT EXISTS (
        SELECT *
        FROM VENDE v
        WHERE v.codigo_tienda = t.codigo_tienda
          AND v.codigo_bebida IN (
              SELECT g.codigo_bebida
              FROM GUSTA g
              WHERE g.cedula = b.cedula
          )
    ) 
    AND EXISTS (
        SELECT *
        FROM FRECUENTA f
        WHERE f.cedula = b.cedula
          AND f.codigo_tienda = t.codigo_tienda
    )
) AND EXISTS (
    SELECT *
    FROM GUSTA g
    WHERE g.cedula = b.cedula
) AND EXISTS (
    SELECT *
    FROM FRECUENTA f
    WHERE f.cedula = b.cedula
);

