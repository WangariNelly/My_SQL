CREATE DATABASE IF NOT EXISTs Products_db;
CREATE TABLE IF NOT EXISTS Products_db.Products(
   id int PRIMARY KEY AUTO_INCREMENT,
   Product_name VARCHAR(100),
   Price int,
   Date_stamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
