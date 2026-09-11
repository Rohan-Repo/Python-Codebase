DROP DATABASE IF EXISTS CompanyDatabase;

CREATE DATABASE CompanyDatabase;

USE CompanyDatabase;

DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee
(
	empId INT PRIMARY KEY IDENTITY(100,1),
	empFirstName VARCHAR(30),
	empLastName VARCHAR(30),
	empSalary INT NOT NULL CHECK( empSalary > 20000 ),
	empCity VARCHAR(50) NOT NULL,
	empCountry VARCHAR(50) NOT NULL
);

INSERT INTO Employee
(
    empFirstName, empLastName, empSalary, empCity, empCountry
)
VALUES
    ('Albus',    'Dumbledore', 100000, 'London',    'UK'),
    ('Severus',  'Snape',       50000, 'Wembley',   'UK'),
    ('Hermoine', 'Granger',     35000, 'Stockholm', 'Sweden'),
    ('Ron',      'Weasley',     25000, 'Malmo',     'Sweden'),
    ('Rubeus',   'Hagrid',      70000, 'Munich',    'Germany'),
    ('Harry',    'Potter',      23000, 'Muscat',    'Oman'),
    ('Neville',  'Longbottom',  54321, 'Abu Dhabi', 'UAE');
	
SELECT * FROM Employee;

SELECT * FROM Employee ORDER BY empSalary DESC;