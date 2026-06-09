-- Industry Convention : Since we will be storing Employee Information we prefix emp to all the values, to DB Name, to Column Names etc.

-- CREATE - How to create a new table. 
CREATE TABLE Employee( empId INT PRIMARY KEY, empName TEXT, empDept TEXT, empSalary REAL, empCity TEXT, empCountry TEXT );

-- INSERT - Add a new record in a table
INSERT INTO Employee VALUES ( 1, 'Harvey Specter', 'Legal', 100000, 'New York', 'USA' ); 
INSERT INTO Employee VALUES ( 2, 'Jessica Pearson', 'CEO', 200000, 'Seattle', 'USA' ); 
INSERT INTO Employee VALUES ( 3, 'Mike Ross', 'Research', 75000, 'Toronto', 'Canada' ); 
INSERT INTO Employee VALUES ( 4, 'Louis Litt', 'COO', 150000, 'London', 'UK' ); 

-- READ - How to retrieve data from a table.
SELECT * FROM Employee ORDER BY empSalary DESC;

-- To see Autoincremented Values
SELECT * FROM sqlite_sequence;