DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee ( empId INTEGER PRIMARY KEY AUTOINCREMENT, empFirstName TEXT, empLastName TEXT, 
empSalary INT NOT NULL CHECK( empSalary > 20000 ), empCity TEXT NOT NULL, empCountry TEXT NOT NULL );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'Larry', 'Stine', 100000, 'Mumbai', 'India' );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'John', 'Doe', 50000, 'Toronto', 'Canada' );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'Jane', 'Doe', 35000, 'Vancouver', 'Canada' );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'Mary', 'Smith', 25000, 'Calgary', 'Canada' );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'Janice', 'Walker', 70000, 'Kolkata', 'India' );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'Adam', 'West', 23000, 'Delhi', 'India' );

INSERT INTO Employee ( empFirstName, empLastName, empSalary, empCity, empCountry ) 
VALUES ( 'Robert', 'King', 54321, 'Riyadh', 'KSA' );

SELECT * FROM Employee;

SELECT * FROM Employee ORDER BY empSalary DESC;