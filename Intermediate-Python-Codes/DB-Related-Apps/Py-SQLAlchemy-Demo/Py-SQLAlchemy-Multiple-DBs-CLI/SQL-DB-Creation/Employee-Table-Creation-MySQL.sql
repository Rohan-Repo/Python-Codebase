-- CREATE A LOCAL USER
create user 'compdbadmin'@'localhost' IDENTIFIED BY 'compdbadmin';

grant all privileges on *.* to 'compdbadmin'@'localhost' with GRANT option;

-- CREATE A BRAND NEW DATABASE AND TABLES
DROP DATABASE IF EXISTS CompanyDatabase;

CREATE DATABASE CompanyDatabase;

USE CompanyDatabase;

DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee
(
	empId INT PRIMARY KEY AUTO_INCREMENT,
	empFirstName VARCHAR(30),
	empLastName VARCHAR(30),
	empSalary INT NOT NULL CHECK( empSalary > 20000 ),
	empCity VARCHAR(50) NOT NULL,
	empCountry VARCHAR(50) NOT NULL
) AUTO_INCREMENT = 200;

INSERT INTO Employee
(
    empFirstName, empLastName, empSalary, empCity, empCountry
)
VALUES
    ('Chandler', 'Bing',         100000, 'Berlin',    'Germany'),
    ('Joey',     'Tribbiani',     50000, 'Toronto',   'Canada'),
    ('Rachel',   'Greene',        25000, 'Vancouver', 'Canada'),
    ('Phoebe',   'Buffay',        35000, 'Calgary',   'Canada'),
    ('Monica',   'Geller',        70000, 'Munich',    'Germany'),
    ('Janice',   'Hosenstein',    23000, 'Delhi',     'India'),
    ('Gunther',  'Central Perk',  54321, 'Dubai',     'UAE');
	
SELECT * FROM Employee ORDER BY empSalary DESC;