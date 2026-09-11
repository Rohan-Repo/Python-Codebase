# =============================================================
#  query_normal_MS_SS_S.py
#
#  PURPOSE  : Connects to MySQL, SQL Server or SQLite, fetches
#             all employees sorted by salary (highest first),
#             and prints them as plain Python ORM objects.
#
#  APPROACH : Normal Python Objects — each row returned from
#             the database becomes an Employee object whose
#             attributes you access with dot notation:
#             emp.empFirstName, emp.empSalary, etc.
#
#  RUN      : python query_normal_MS_SS_S.py
#
#  REQUIRES : pip install sqlalchemy pymysql pyodbc
#             SQLite needs no install — built into Python.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# Column, Integer, String  → describe the shape of table columns
# DeclarativeBase          → required parent class for table classes
# Session                  → temporary workspace for running queries
# pick_database            → our own function from database_MS_SS_S.py
#                            that shows the menu and returns the engine

from sqlalchemy     import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from database_MS_SS_S import pick_database


# ── Base class ───────────────────────────────────────────────
# Every table class must inherit from DeclarativeBase.
# It registers the class with SQLAlchemy's mapping system.
class Base(DeclarativeBase):
    pass


# ── Step 1: Ask user which DB to connect to ──────────────────
# pick_database() shows the menu, builds the engine, and
# returns two values:
#   engine → the active database connection
#   db     → a string like "mysql", "sqlserver", "sqlite"
# We capture both with:  engine, db = pick_database()

engine, db = pick_database()


# ── Step 2: Define the Employee table model ──────────────────
# MySQL, SQL Server and SQLite all preserve the original casing
# of column names, so "empId", "empFirstName" etc. work as-is.
#
# (PostgreSQL is different — it lowercases everything. That is
# handled in the MySQL-SQLServer-SQLite-PostgreSQL folder.)
#
# Each Column("db_column_name", DataType) maps one Python
# attribute to one column in the actual database table.

class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the DB table name

    # primary_key=True → this column uniquely identifies each row
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number
    empCity      = Column("empCity",      String(50))    # max 50 characters
    empCountry   = Column("empCountry",   String(50))


# ── Step 3: Fetch data from the database ─────────────────────
# Session is a temporary workspace for talking to the database.
# 'with Session(engine) as session' opens it and automatically
# closes it when the indented block finishes.

with Session(engine) as session:

    # This is the Python equivalent of:
    #   SELECT * FROM Employee ORDER BY empSalary DESC
    #
    # .query(Employee)              → which table to read from
    # .order_by(empSalary.desc())   → sort by salary, high to low
    # .all()                        → fetch every matching row as a list
    employees = (
        session.query(Employee)
               .order_by(Employee.empSalary.desc())
               .all()
    )

# Session is now closed.
# 'employees' is a plain Python list of Employee objects.
# Each object has attributes: empId, empFirstName, empLastName,
# empSalary, empCity, empCountry — accessed with dot notation.


# ── Step 4: Print the results ─────────────────────────────────
# f-strings embed variables directly inside a string.
# The format specifiers inside {} control alignment and width:
#   :<5   = left-align  in a  5-character wide field
#   :<12  = left-align  in a 12-character wide field
#   :>10  = right-align in a 10-character wide field
#   :>9,  = right-align in a  9-character wide field,
#           with comma as thousand separator (100000 → 100,000)

print()

# Header row
print(f"{'ID':<5} {'First Name':<12} {'Last Name':<15} {'Salary':>10}  {'City':<16} {'Country'}")

# Divider line — "-" * 65 repeats the dash character 65 times
print("-" * 65)

# Loop through each Employee object and print one line per row
for emp in employees:
    print(
        f"{emp.empId:<5} "
        f"{emp.empFirstName:<12} "
        f"{emp.empLastName:<15} "
        f"${emp.empSalary:>9,}  "
        f"{emp.empCity:<16} "
        f"{emp.empCountry}"
    )

print()
# len() returns the number of items in the list
print("Total employees:", len(employees))
