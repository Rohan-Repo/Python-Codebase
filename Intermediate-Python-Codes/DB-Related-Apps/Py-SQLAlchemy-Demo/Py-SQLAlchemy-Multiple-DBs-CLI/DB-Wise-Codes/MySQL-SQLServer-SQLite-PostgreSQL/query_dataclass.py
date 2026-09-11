# =============================================================
#  query_dataclass.py
#
#  PURPOSE  : Connects to MySQL, SQL Server, PostgreSQL or
#             SQLite, fetches all employees sorted by salary
#             (highest first), and stores results as Python
#             dataclasses.
#
#  APPROACH : Dataclass Objects — after fetching from the DB,
#             each row is immediately converted into a plain
#             EmployeeRecord dataclass. The dataclass has NO
#             database connection, making it safe to use
#             anywhere in your code after the session closes.
#
#  DIFFERENCE vs query_normal.py:
#    query_normal.py   → rows stay as SQLAlchemy ORM objects
#    query_dataclass.py→ rows are converted to plain dataclasses
#
#  RUN      : python query_dataclass.py
#
#  REQUIRES : pip install sqlalchemy pymysql pyodbc psycopg2-binary
#             SQLite needs no install — built into Python.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# dataclasses     → standard Python module for working with dataclasses
# dataclass       → the @dataclass decorator that auto-generates
#                   __init__, __repr__ and __eq__ for a class
# Column etc.     → SQLAlchemy tools for describing table structure
# pick_database   → our menu function in connectToDB.py

import dataclasses
from dataclasses    import dataclass
from sqlalchemy     import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from connectToDB    import pick_database


# ── Base class ───────────────────────────────────────────────
# Required parent class for all SQLAlchemy ORM table classes.
class Base(DeclarativeBase):
    pass


# ── Step 1: Ask user which database to use ───────────────────
# pick_database() shows the menu and returns:
#   engine → the active database connection
#   db     → string identifying the DB ("mysql", "postgresql", etc.)

engine, db = pick_database()


# ── Step 2: Define the correct Employee ORM model ─────────────
# PostgreSQL lowercases all names → needs a model with lowercase columns.
# MySQL, SQL Server, SQLite keep original casing → share one model.
#
# This model is ONLY used to fetch data from the database.
# Once fetched, rows are converted to EmployeeRecord dataclasses below.

if db == "postgresql":
    # PostgreSQL: all column and table names must be lowercase
    class Employee(Base):
        __tablename__ = "employee"
        empId        = Column("empid",        Integer, primary_key=True)
        empFirstName = Column("empfirstname", String(30))
        empLastName  = Column("emplastname",  String(30))
        empSalary    = Column("empsalary",    Integer)
        empCity      = Column("empcity",      String(50))
        empCountry   = Column("empcountry",   String(50))
else:
    # MySQL / SQL Server / SQLite: use original mixed casing
    class Employee(Base):
        __tablename__ = "Employee"
        empId        = Column("empId",        Integer, primary_key=True)
        empFirstName = Column("empFirstName", String(30))
        empLastName  = Column("empLastName",  String(30))
        empSalary    = Column("empSalary",    Integer)
        empCity      = Column("empCity",      String(50))
        empCountry   = Column("empCountry",   String(50))


# ── Step 3: Define the EmployeeRecord dataclass ───────────────
# This is a plain Python class — NOT connected to any database.
# @dataclass automatically generates:
#   __init__  → lets you create: EmployeeRecord(empId=1, ...)
#   __repr__  → lets you print:  EmployeeRecord(empId=1, ...)
#   __eq__    → lets you compare: record1 == record2
#
# field_name : type  ← type hints (int, str) tell Python and
# your editor what kind of data each field holds.

@dataclass
class EmployeeRecord:
    empId        : int   # whole number
    empFirstName : str   # text
    empLastName  : str
    empSalary    : int
    empCity      : str
    empCountry   : str


# ── Step 4: Fetch rows and convert to dataclasses ─────────────
# We open the Session, fetch all rows, and immediately convert
# each row to an EmployeeRecord INSIDE the 'with' block.
# This ensures all row data is loaded before the session closes.

with Session(engine) as session:

    # Fetch all employees sorted by salary (high to low)
    # → SELECT * FROM Employee ORDER BY empSalary DESC
    rows = (
        session.query(Employee)
               .order_by(Employee.empSalary.desc())
               .all()
    )

    # Convert each ORM row → EmployeeRecord dataclass.
    # List comprehension: a compact way to build a new list
    # by running a block of code for each item in 'rows'.
    # Equivalent to a for loop that appends to a list.
    records = [
        EmployeeRecord(
            empId        = row.empId,         # copy each field
            empFirstName = row.empFirstName,   # from the ORM row
            empLastName  = row.empLastName,    # into the dataclass
            empSalary    = row.empSalary,
            empCity      = row.empCity,
            empCountry   = row.empCountry,
        )
        for row in rows   # repeat for every row in the result
    ]

# Session is now closed.
# 'records' is a list of EmployeeRecord dataclasses.
# They are plain Python objects — no DB connection, fully portable.


# ── Step 5: Print the results ─────────────────────────────────
# f-string format specifiers:
#   :<5   = left-align  in a  5-character wide field
#   :<12  = left-align  in a 12-character wide field
#   :>10  = right-align in a 10-character wide field
#   :>9,  = right-align, 9 chars wide, comma thousand separator

print()
print(f"{'ID':<5} {'First Name':<12} {'Last Name':<15} {'Salary':>10}  {'City':<16} {'Country'}")
print("-" * 65)

for rec in records:
    print(
        f"{rec.empId:<5} "
        f"{rec.empFirstName:<12} "
        f"{rec.empLastName:<15} "
        f"${rec.empSalary:>9,}  "
        f"{rec.empCity:<16} "
        f"{rec.empCountry}"
    )

print()
print("Total employees:", len(records))

# ── Bonus: dataclass → dictionary ────────────────────────────
# dataclasses.asdict() converts an EmployeeRecord into a plain
# Python dictionary. Useful for JSON, APIs, logging, etc.
# Example output: {"empId": 1, "empFirstName": "Harvey", ...}
print()
print("First record as a dictionary:")
print(dataclasses.asdict(records[0]))
