-- Products Table 
CREATE TABLE Products ( productID INTEGER PRIMARY KEY AUTOINCREMENT, productName TEXT, productType TEXT, productPrice REAL );

-- Insert Product Values
INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'Apple iPhone', 1234, 'SmartPhone' ); 

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'HP Spectre', 2222, 'Laptop' ); 

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'Garmin Watch', 555, 'Smartwatch' ); 

INSERT INTO Products ( productName, productPrice, productType ) VALUES ( 'Nespresso', 333, 'Coffee Machine' );
 
-- Orders Table
CREATE TABLE Orders ( orderID INTEGER PRIMARY KEY AUTOINCREMENT, orderQuantity INTEGER, productID INTEGER, FOREIGN KEY (productID) REFERENCES Products(productID) );

-- Insert Order Values
INSERT INTO Orders ( productID, orderQuantity ) VALUES ( 1, 5 ); 

INSERT INTO Orders ( productID, orderQuantity ) VALUES ( 2, 2 );

INSERT INTO Orders ( productID, orderQuantity ) VALUES ( 3, 10 );

-- AS for Column Alias or Renaming our Output 

-- INNER JOIN - Display Only Common Values - Intersection
-- Inner Join or Join – This is similar to Intersection of two sets 
-- Here, we get just the matching rows from both tables and eliminate others

SELECT productName, productType, productPrice, orderQuantity, productPrice * orderQuantity AS totalAmount FROM Products INNER JOIN Orders ON Products.productID = Orders.productID; 

-- LEFT JOIN - All Values from Left Table and only Matching Values from the Right Table
-- Left Join or Left Outer Join – This is similar to Set Difference. 
-- Here we will get the matching rows in addition to the non-matching rows from the Left table
-- Get the matching rows + non-matching rows from the Left table

SELECT productName, productType, productPrice, orderQuantity, productPrice * orderQuantity AS totalAmount FROM Products LEFT JOIN Orders ON Products.productID = Orders.productID; 

-- RIGHT JOIN - All Values from Right Table and only Matching Values from the Left Table
-- Right Join or Right Outer Join – This is similar to Set Difference.
-- Here we get the matching rows in addition to the non-matching rows from the Right table.
-- Get the matching rows + non-matching rows from the Right table 

SELECT productName, productType, productPrice, orderQuantity, productPrice * orderQuantity AS totalAmount FROM Products RIGHT JOIN Orders ON Products.productID = Orders.productID;

-- Cross Join – Here we get the cartesian product
-- Cartesian Product = number of rows of table1 * number of rows of table2
-- Since Cross Joins give us the Cartesian Product, we don’t need to specify a condition

SELECT * FROM Products CROSS JOIN Orders;