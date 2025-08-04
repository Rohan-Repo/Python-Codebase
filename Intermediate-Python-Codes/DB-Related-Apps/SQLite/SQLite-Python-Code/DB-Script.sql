-- ON Command Prompt -> sqlite3 suits.db

CREATE TABLE Employee( empId INTEGER PRIMARY KEY AUTOINCREMENT, empName TEXT, empDept TEXT, empSalary REAL, empCity TEXT, empCountry TEXT );

INSERT INTO Employee(empName,empDept,empSalary,empCity,empCountry) VALUES ( 'Harvey Specter', 'Legal', 100000, 'New York', 'USA' ); 

INSERT INTO Employee(empName,empDept,empSalary,empCity,empCountry) VALUES ( 'Jessica Pearson', 'CEO', 200000, 'Seattle', 'USA' ); 

INSERT INTO Employee(empName,empDept,empSalary,empCity,empCountry) VALUES ( 'Mike Ross', 'Research', 50000, 'Toronto', 'Canada' ); 

INSERT INTO Employee(empName,empDept,empSalary,empCity,empCountry) VALUES ( 'Louis Litt', 'COO', 150000, 'London', 'UK' ); 

INSERT INTO Employee(empName,empDept,empSalary,empCity,empCountry) VALUES ( 'Donna Paulson', 'Operations', 75000, 'Paris', 'France' );

SELECT * FROM Employee;