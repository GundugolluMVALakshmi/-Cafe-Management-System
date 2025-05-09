CREATE DATABASE IF NOT EXISTS cafe_db;
USE cafe_db;

CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(100) NOT NULL,
    role ENUM('admin', 'staff') NOT NULL
);

INSERT INTO users (username, password, role)
VALUES
('admin', 'admin123', 'admin'),
('staff', 'staff123', 'staff');

CREATE TABLE IF NOT EXISTS inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT,
    total_price FLOAT,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
