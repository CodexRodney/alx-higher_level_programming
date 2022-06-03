-- creates database hbtn_0d_usa
-- also creates table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
DROP TABLE IF EXISTS states;
CREATE TABLE states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));
