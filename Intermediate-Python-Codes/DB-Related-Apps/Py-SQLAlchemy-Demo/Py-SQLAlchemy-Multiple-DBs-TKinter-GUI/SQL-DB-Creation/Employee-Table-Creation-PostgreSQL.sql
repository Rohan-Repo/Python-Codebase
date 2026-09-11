DROP SCHEMA IF EXISTS CompanyDatabase CASCADE;
CREATE SCHEMA CompanyDatabase;
SET search_path TO CompanyDatabase;

-- Database: companydatabase

-- DROP DATABASE IF EXISTS companydatabase;

CREATE DATABASE companydatabase
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

USE companydatabase;

DROP TABLE IF EXISTS Employee;

-- Create DB user
CREATE ROLE compdbadmin WITH
	LOGIN
	NOSUPERUSER
	CREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'compdbadmin';
    
-- Check Schema of Table:
-- See ALL tables and which schema they are in
SELECT table_schema, table_name FROM information_schema.tables
WHERE table_type = 'BASE TABLE' AND table_name ILIKE 'employee';

-- Grant permission to use the schema - since our table is in the public schema
GRANT USAGE ON SCHEMA public TO compdbadmin;

-- Grant permission to read the employee table
GRANT SELECT ON TABLE public.employee TO compdbadmin;

CREATE TABLE Employee
(
    empId           INT GENERATED ALWAYS AS IDENTITY
                        (START WITH 300)
                        PRIMARY KEY,
    empFirstName    VARCHAR(30),
    empLastName     VARCHAR(30),
    empSalary       INT         NOT NULL CHECK (empSalary > 20000),
    empCity         VARCHAR(50) NOT NULL,
    empCountry      VARCHAR(50) NOT NULL
);

INSERT INTO Employee (empFirstName, empLastName, empSalary, empCity, empCountry)
VALUES 
    ('Harvey',   'Specter',   100000, 'Athens',       'Greece'),
    ('Mike',     'Ross',       50000, 'Thessaloniki', 'Greece'),
    ('Donna',    'Paulsen',    75000, 'Patras',       'Greece'),
    ('Louis',    'Litt',       35000, 'Warsaw',       'Poland'),
    ('Rachel',   'Zane',       25000, 'Krakow',       'Poland'),
    ('Jessica',  'Pearson',    95000, 'Gdansk',       'Poland'),
    ('Robert',   'Zane',       23000, 'Manila',       'Philippines'),
    ('Alex',     'Williams',   54321, 'Cebu City',    'Philippines'),
    ('Katrina',  'Bennett',    62000, 'Davao',        'Philippines'),
    ('Samantha', 'Wheeler',    88000, 'Quezon City',  'Philippines'),
    ('Gretchen', 'Palmer',     45000, 'Heraklion',    'Greece'),
    ('Zane',     'Alexander',  30000, 'Wroclaw',      'Poland');

-- All employees ordered by salary descending
SELECT * FROM Employee ORDER BY empSalary DESC;