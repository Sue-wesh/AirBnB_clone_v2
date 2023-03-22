-- script that prepares MySQL server for the project
--  db: hbnb_test_db, user: hbnb_test (in localhost), pwd: hbnb_test_pwd
--  hbnb_test shld have all privileges on db hbnb_test_db
--  the should also have SELECT privilege on performance_schema 
--  if the db and user already exis, script shoul not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
