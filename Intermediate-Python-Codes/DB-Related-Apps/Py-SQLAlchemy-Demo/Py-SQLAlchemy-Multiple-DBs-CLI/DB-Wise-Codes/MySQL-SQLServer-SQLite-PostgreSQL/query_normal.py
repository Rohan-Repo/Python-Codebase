# =============================================================
#  query_normal.py
#
#  PURPOSE  : Connects to MySQL, SQL Server, PostgreSQL or
#             SQLite, fetches all employees sorted by salary
#             (highest first), and prints them as plain
#             Python ORM objects.
#
#  APPROACH : Normal Python Objects — each row from the DB
#             becomes an Employee object. Access data using
#             dot notation: emp.empFirstName, emp.empSalary
#
#  RUN      : python query_normal.py
#
#  REQUIRES : pip install sqlalchemy pymysql pyodbc psycopg2-binary
#             SQLite needs no install — built into Python.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# Column, Integer, String  → used to describe table columns
# DeclarativeBase          → required parent class for ORM models
# Session                  → temporary workspace for DB queries
# pick_database            → our menu function from connectToDB.py

from sqlalchemy     import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from connectToDB    import pick_database


# ── Base class ───────────────────────────────────────────────
# All SQLAlchemy table classes must inherit from DeclarativeBase.
# It registers them with SQLAlchemy's internal mapping system.
class Base(DeclarativeBase):
    pass


# ── Step 1: Ask user which database to use ───────────────────
# pick_database() shows the menu, builds the engine, and returns:
#   engine → the active database connection
#   db     → "mysql" / "sqlserver" / "postgresql" / "sqlite"
# We use 'db' below to decide which Employee model to use.

engine, db = pick_database()


# ── Step 2: Define the correct Employee model ─────────────────
# WHY TWO MODELS?
# PostgreSQL silently lowercases all column and table names.
# So a column created as "empId" is stored as "empid".
# If we send "empId" to PostgreSQL it says the column doesn't exist.
# The fix: use lowercase names in the model when PostgreSQL is chosen.
# MySQL, SQL Server and SQLite keep the original casing, so they
# share the same model with "empId", "empFirstName" etc.

if db == "postgresql":
    # PostgreSQL model — all names in lowercase to match DB storage
    class Employee(Base):
        __tablename__ = "employee"                                    # lowercase
        empId        = Column("empid",        Integer, primary_key=True)
        empFirstName = Column("empfirstname", String(30))
        empLastName  = Column("emplastname",  String(30))
        empSalary    = Column("empsalary",    Integer)
        empCity      = Column("empcity",      String(50))
        empCountry   = Column("empcountry",   String(50))
else:
    # MySQL / SQL Server / SQLite model — original mixed casing
    class Employee(Base):
        __tablename__ = "Employee"                                    # mixed case
        empId        = Column("empId",        Integer, primary_key=True)
        empFirstName = Column("empFirstName", String(30))
        empLastName  = Column("empLastName",  String(30))
        empSalary    = Column("empSalary",    Integer)
        empCity      = Column("empCity",      String(50))
        empCountry   = Column("empCountry",   String(50))


# ── Step 3: Fetch data ────────────────────────────────────────
# Open a Session (temporary DB connection), run the query,
# then close it automatically when the 'with' block ends.

with Session(engine) as session:

    # Python equivalent of:
    # SELECT * FROM Employee ORDER BY empSalary DESC
    #
    # .query(Employee)                → which table to read
    # .order_by(Employee.empSalary.desc()) → high salary first
    # .all()                          → return all rows as a list
    employees = (
        session.query(Employee)
               .order_by(Employee.empSalary.desc())
               .all()
    )

# Session closed. 'employees' is now a plain Python list.
# Each item is an Employee object with dot-accessible attributes.


# ── Step 4: Print the results ─────────────────────────────────
# f-string format specifiers:
#   :<5   = left-align  in a  5-character wide field
#   :<12  = left-align  in a 12-character wide field
#   :>10  = right-align in a 10-character wide field
#   :>9,  = right-align, 9 chars wide, comma as thousand separator
#           e.g. 100000 → 100,000

print()
print(f"{'ID':<5} {'First Name':<12} {'Last Name':<15} {'Salary':>10}  {'City':<16} {'Country'}")
print("-" * 65)   # divider line

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
print("Total employees:", len(employees))
