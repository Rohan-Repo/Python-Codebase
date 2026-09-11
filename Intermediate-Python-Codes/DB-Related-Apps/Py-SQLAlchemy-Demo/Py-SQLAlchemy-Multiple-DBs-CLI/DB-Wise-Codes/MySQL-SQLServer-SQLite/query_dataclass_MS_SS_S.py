# =============================================================
#  query_dataclass_MS_SS_S.py
#
#  PURPOSE  : Connects to MySQL, SQL Server or SQLite, fetches
#             all employees sorted by salary (highest first),
#             and stores the results as Python dataclasses.
#
#  APPROACH : Dataclass Objects — after fetching rows from the
#             DB, each row is immediately converted into an
#             EmployeeRecord dataclass. The dataclass is a
#             plain Python object with NO database connection.
#             This makes it safe to pass around your code,
#             compare with ==, and convert to a dictionary.
#
#  DIFFERENCE vs query_normal_MS_SS_S.py:
#    query_normal   → rows stay as SQLAlchemy ORM objects
#    query_dataclass→ rows are converted to plain dataclasses
#
#  RUN      : python query_dataclass_MS_SS_S.py
#
#  REQUIRES : pip install sqlalchemy pymysql pyodbc
#             SQLite needs no install — built into Python.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# dataclasses          → the standard Python module for dataclasses
# dataclass            → the @dataclass decorator that auto-generates
#                        __init__, __repr__ and __eq__ for a class
# Column, Integer, String → describe the shape of table columns
# DeclarativeBase      → required parent class for table classes
# Session              → temporary workspace for running queries
# pick_database        → our menu function from database_MS_SS_S.py

import dataclasses
from dataclasses    import dataclass
from sqlalchemy     import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from database_MS_SS_S import pick_database


# ── Base class ───────────────────────────────────────────────
# Every SQLAlchemy table class must inherit from DeclarativeBase.
class Base(DeclarativeBase):
    pass


# ── Step 1: Ask user which DB to connect to ──────────────────
# pick_database() shows the menu and returns:
#   engine → the active database connection object
#   db     → a string identifying the database ("mysql", "sqlserver", "sqlite")

engine, db = pick_database()


# ── Step 2: Define the Employee table model ──────────────────
# This class tells SQLAlchemy what the Employee table looks like.
# MySQL, SQL Server and SQLite all keep the original column name
# casing, so we use "empId", "empFirstName" etc. as-is.

class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the DB table name

    # Column("db_column_name", DataType, options)
    # primary_key=True → uniquely identifies each row
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number
    empCity      = Column("empCity",      String(50))
    empCountry   = Column("empCountry",   String(50))


# ── Step 3: Define the EmployeeRecord dataclass ───────────────
# A dataclass is a plain Python class that just holds data.
# @dataclass automatically creates:
#   __init__  → so you can write EmployeeRecord(empId=1, ...)
#   __repr__  → so print(record) shows something readable
#   __eq__    → so you can compare two records with ==
#
# Unlike the Employee ORM class above, EmployeeRecord has NO
# connection to the database. It is just a Python container.
# This makes it much safer to use outside of a database session.

@dataclass
class EmployeeRecord:
    # field_name : type  ← Python type hints (int, str, etc.)
    # These tell Python (and your editor) what type of data each field holds.
    empId        : int
    empFirstName : str
    empLastName  : str
    empSalary    : int
    empCity      : str
    empCountry   : str


# ── Step 4: Fetch rows and convert to dataclasses ─────────────
# We open a Session to talk to the database, fetch all rows,
# and immediately convert each one into an EmployeeRecord.
# We do the conversion INSIDE the 'with' block to make sure
# all attribute values are loaded before the session closes.

with Session(engine) as session:

    # Fetch all employees sorted by salary, high to low
    # SELECT * FROM Employee ORDER BY empSalary DESC
    rows = (
        session.query(Employee)
               .order_by(Employee.empSalary.desc())
               .all()
    )

    # Convert each ORM row into a plain EmployeeRecord dataclass.
    # This is a list comprehension — a compact way to build a list.
    # It is the same as writing a for loop and appending each item.
    records = [
        EmployeeRecord(
            empId        = row.empId,
            empFirstName = row.empFirstName,
            empLastName  = row.empLastName,
            empSalary    = row.empSalary,
            empCity      = row.empCity,
            empCountry   = row.empCountry,
        )
        for row in rows   # for every row fetched from the database
    ]

# Session is now closed.
# 'records' is a list of EmployeeRecord dataclasses — plain Python,
# no database dependency. Safe to use anywhere in your code.


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

# ── Bonus: convert a dataclass to a dictionary ────────────────
# dataclasses.asdict() turns an EmployeeRecord into a plain
# Python dictionary — useful for JSON output, APIs, logging, etc.
# Example: {"empId": 1, "empFirstName": "Harvey", ...}
print()
print("First record as a dictionary:")
print(dataclasses.asdict(records[0]))
