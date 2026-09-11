DROP TABLE IF EXISTS Experts;

CREATE TABLE Experts (
    expertID INTEGER PRIMARY KEY AUTOINCREMENT,
    birthDate DATETIME,
    expertName TEXT,
    technology TEXT
);

INSERT INTO Experts (birthDate, expertName, technology)
VALUES
('1956-01-31 10:30:00', 'Guido van Rossum', 'Python'),
('1961-04-09 01:09:11', 'Dr. Richard Hipp', 'SQLite'),
('1948-09-10 08:40:00', 'Charles Simonyi', 'Microsoft Word & Excel'),
('1791-12-26 16:05:00', 'Charles Babbage', 'Analytical Engine'),
('1941-09-09 12:00:00', 'Dennis Ritchie', 'C'),
('1955-06-08 12:00:00', 'Sir Tim Berners-Lee', 'World Wide Web');

-- Sort Ascending
SELECT * FROM Experts ORDER BY birthDate DESC;

-- Sort Descending
SELECT * FROM Experts ORDER BY birthDate DESC;