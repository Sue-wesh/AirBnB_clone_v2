-- script that prepares a MySQL server for the project:
--  creates a dtabase hbnb_dev_db, with user hbnb_dev (in localhost)hbnb_dev
--  grant all privileges for hbnb_dev on hbnb_dev_db
--  grant select privilege for hbnb_dev on performance schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
