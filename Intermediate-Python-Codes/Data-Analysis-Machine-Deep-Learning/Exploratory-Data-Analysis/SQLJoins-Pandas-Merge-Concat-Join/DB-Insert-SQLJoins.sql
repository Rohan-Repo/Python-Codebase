-- PRODUCTS TABLE
CREATE TABLE Products (
    productID INTEGER PRIMARY KEY AUTOINCREMENT,
    productName TEXT,
    productType TEXT,
    productPrice REAL
);

-- Insert Product Values
INSERT INTO Products (productName, productPrice, productType)
VALUES
('Apple iPhone', 1234, 'Smartphone'),
('HP Spectre', 2222, 'Laptop'),
('Garmin Watch', 555, 'Smartwatch'),
('Nespresso', 333, 'Coffee Machine'),
('Samsung Galaxy S24', 1099, 'Smartphone'),
('Dell XPS 13', 1899, 'Laptop'),
('Apple Watch Ultra', 799, 'Smartwatch'),
('Breville Barista Pro', 999, 'Coffee Machine'),
('Sony WH-1000XM5', 499, 'Headphones'),
('Amazon Echo', 149, 'Smart Speaker'),
('iPad Pro', 1299, 'Tablet'),
('Lenovo ThinkPad X1', 1999, 'Laptop'),
('GoPro Hero 12', 449, 'Camera'),
('Canon EOS R10', 1399, 'Camera'),
('Fitbit Charge 6', 179, 'Smartwatch');



-- CUSTOMERS TABLE
CREATE TABLE Customers (
    customerID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerName TEXT,
    customerEmail TEXT,
    customerCity TEXT
);

-- Insert Customers
INSERT INTO Customers (customerName, customerEmail, customerCity)
VALUES
('chandler.bing', 'chandler.bing@friends.com', 'New York'),
('monica.geller', 'monica.geller@friends.com', 'New York'),
('ross.geller', 'ross.geller@friends.com', 'New York'),
('joey.tribbiani', 'joey.tribbiani@friends.com', 'New York'),
('phoebe.buffay', 'phoebe.buffay@friends.com', 'New York'),
('rachel.greene', 'rachel.greene@friends.com', 'New York'),
('gunther', 'gunther@centralperk.com', 'New York'),
('janice', 'janice@ohmygod.com', 'New York'),
('ms.chanandler bong', 'ms.chanandler.bong@friends.com', 'New York'),
('ken addams', 'ken.addams@friends.com', 'New York'),
('princess consuela bananahammock', 'princess.bananahammock@friends.com', 'New York'),
('mike.hannigan', 'mike.hannigan@friends.com', 'New York'),
('ben.geller', 'ben.geller@friends.com', 'New York'),
('emma.geller', 'emma.geller@friends.com', 'New Jersey'),
('frank.buffay.jr.jr', 'frank.buffay.jr.jr@friends.com', 'Long Island'),
('leslie.buffay', 'leslie.buffay@friends.com', 'Long Island'),
('chandler.buffay', 'chandler.buffay@friends.com', 'Long Island');


-- ORDERS TABLE
CREATE TABLE Orders (
    orderID INTEGER PRIMARY KEY AUTOINCREMENT,
    orderQuantity INTEGER,
    orderDateTime DATETIME,
    productID INTEGER,
    customerID INTEGER,
    FOREIGN KEY (productID) REFERENCES Products(productID),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

-- Insert Order Values
INSERT INTO Orders (productID, customerID, orderQuantity, orderDateTime)
VALUES
(1, 1, 5, '2025-01-15 10:30:00'),   -- Chandler
(2, 2, 2, '2025-01-22 14:45:00'),   -- Monica
(3, 3, 10, '2025-02-05 09:10:00'),  -- Ross
(4, 4, 3, '2025-02-17 16:55:00'),   -- Joey
(5, 5, 7, '2025-03-03 11:22:00'),   -- Phoebe
(6, 6, 1, '2025-03-19 19:40:00'),   -- Rachel
(7, 7, 4, '2025-03-29 08:15:00'),   -- Gunther
(8, 8, 2, '2025-04-10 13:00:00'),   -- Janice
(9, 9, 8, '2025-04-22 17:25:00'),   -- Ms. Chanandler Bong
(10, 10, 12, '2025-05-01 12:05:00'),-- Ken Addams
(11, 11, 6, '2025-05-15 15:15:00'), -- Princess Consuela
(12, 1, 3, '2025-06-01 09:50:00'),
(13, 2, 9, '2025-06-12 11:10:00'),
(14, 3, 1, '2025-07-03 10:00:00'),
(15, 4, 11, '2025-07-20 18:25:00'),
(1, 5, 2, '2025-08-02 20:00:00'),
(5, 6, 3, '2025-08-18 09:45:00'),
(9, 7, 5, '2025-09-01 08:20:00'),
(10, 8, 7, '2025-09-14 12:40:00'),
(11, 9, 1, '2025-09-28 22:15:00');

-- Joins

-- Inner Join
SELECT 
	o.orderDateTime,
    c.customerName,
    p.productName,
	p.productPrice,
    o.orderQuantity,
	p.productPrice * o.orderQuantity AS totalAmount
    
FROM Customers c 
INNER JOIN Orders o ON o.customerID = c.customerID
INNER JOIN Products p ON o.productID = p.productID;

-- SELECT o.orderDateTime, c.customerName, p.productName, p.productPrice, o.orderQuantity, p.productPrice * o.orderQuantity AS totalAmount FROM Customers c INNER JOIN Orders o ON o.customerID = c.customerID INNER JOIN Products p ON o.productID = p.productID; 

-- Right Join
SELECT 
	o.orderDateTime,
    c.customerName,
    p.productName,
	p.productPrice,
    o.orderQuantity,
	p.productPrice * o.orderQuantity AS totalAmount
    
FROM Customers c 
RIGHT JOIN Orders o ON o.customerID = c.customerID
RIGHT JOIN Products p ON o.productID = p.productID;

-- SELECT o.orderDateTime, c.customerName, p.productName, p.productPrice, o.orderQuantity, p.productPrice * o.orderQuantity AS totalAmount FROM Customers c RIGHT JOIN Orders o ON o.customerID = c.customerID RIGHT JOIN Products p ON o.productID = p.productID;

-- Left Join

SELECT 
	o.orderDateTime,
    c.customerName,
    p.productName,
	p.productPrice,
    o.orderQuantity,
	p.productPrice * o.orderQuantity AS totalAmount
    
FROM Customers c 
LEFT JOIN Orders o ON o.customerID = c.customerID
LEFT JOIN Products p ON o.productID = p.productID;

-- SELECT o.orderDateTime, c.customerName, p.productName, p.productPrice, o.orderQuantity, p.productPrice * o.orderQuantity AS totalAmount FROM Customers c LEFT JOIN Orders o ON o.customerID = c.customerID LEFT JOIN Products p ON o.productID = p.productID;

-- Cross Join
SELECT c.customerName, p.productName FROM Customers c CROSS JOIN Products p;


-- DROP TABLE Products;
-- DROP TABLE Orders;
-- DROP TABLE Customers;
