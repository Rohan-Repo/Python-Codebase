CREATE TABLE Products ( productID INTEGER PRIMARY KEY AUTOINCREMENT, productName TEXT, productType TEXT, productPrice REAL );

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'Apple iPhone', 1234, 'SmartPhone' ); 

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'HP Spectre', 2222, 'Laptop' ); 

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'Garmin Watch', 555, 'Smartwatch' ); 

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'Nespresso', 333, 'Coffee Machine' );

SELECT * FROM Products;

CREATE TABLE Orders ( orderID INTEGER PRIMARY KEY AUTOINCREMENT, orderQuantity INTEGER, productID INTEGER, FOREIGN KEY (productID) REFERENCES Products(productID) );

INSERT INTO Orders ( productID, orderQuantity ) VALUES ( 1, 5 ); 

INSERT INTO Orders ( productID, orderQuantity ) VALUES ( 2, 2 );

INSERT INTO Orders ( productID, orderQuantity ) VALUES ( 3, 10 );

SELECT * FROM Orders;

SELECT productName, productType, productPrice, orderQuantity, productPrice * orderQuantity AS totalAmount FROM Products INNER JOIN Orders ON Products.productID = Orders.productID; 