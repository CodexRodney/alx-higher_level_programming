-- creates table unique_id

DROP TABLE IF EXISTS unique_id;
CREATE TABLE unique_id (id INT UNIQUE  DEFAULT 1, name VARCHAR(256));
