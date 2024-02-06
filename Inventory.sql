DROP TABLE IF EXISTS Inventory;

CREATE TABLE Inventory (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
price DECIMAL(10,2) NOT NULL,
quantity INT NOT NULL,
supplier_name VARCHAR(100) NOT NULL
);

INSERT INTO Inventory (name, price, quantity, supplier_name)
VALUES
    ('Pepperoni', 12.99, 50, 'Acme Inc.'),
    ('Tomato', 11.99, 30, 'Supreme Foods'),
    ('Mozzarella', 13.99, 40, 'Tasty Treats'),
    ('Basil', 14.99, 35, 'FoodMaster'),
    ('Prawn', 10.99, 20, 'Fresh Foods');

select * from Inventory;
