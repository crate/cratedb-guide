-- https://cratedb.com/docs/guide/integrate/oracle/

DROP TABLE demo;
CREATE TABLE IF NOT EXISTS demo (id LONG, temperature FLOAT, humidity FLOAT);
INSERT INTO demo (id, temperature, humidity) VALUES (1, 42.84, 83.1);
INSERT INTO demo (id, temperature, humidity) VALUES (2, 84.84, 56.99);
SELECT * FROM demo;
exit;
