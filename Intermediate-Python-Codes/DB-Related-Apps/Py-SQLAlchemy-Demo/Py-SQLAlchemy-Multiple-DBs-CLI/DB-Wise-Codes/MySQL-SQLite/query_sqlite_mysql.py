# =============================================================
#  query_sqlite_mysql.py
#
#  PURPOSE  : Connects to either MySQL or SQLite, fetches all
#             employees from the Employee table, and prints
#             them sorted by salary (highest first).
#
#  RUN      : python query_sqlite_mysql.py
#
#  REQUIRES : pip install sqlalchemy pymysql
#             SQLite needs no install — it is built into Python.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# Column, Integer, String  → used to describe table columns
# create_engine            → opens a connection to the database
# DeclarativeBase          → base class every table class must inherit
# Session                  → temporary workspace for running queries

from sqlalchemy     import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# ── Step 1: Ask user which database to connect to ────────────
# input() displays the prompt text and waits for the user to type.
# The typed value is stored as a string in the variable 'choice'.

print("Pick a database:")
print("1. MySQL")
print("2. SQLite")

choice = input("Enter 1 or 2: ")


# ── Step 2: Build the connection (engine) ────────────────────
# create_engine() sets up the connection to the database.
# The connection string format is:
#   dialect+driver://username:password@host/database_name
#
# dialect = which database  (mysql, sqlite, postgresql, etc.)
# driver  = which library   (pymysql, psycopg2, pyodbc, etc.)

if choice == "1":
    # MySQL connection
    # Update compdbadmin:compdbadmin if your username/password differs
    # Update CompanyDatabase if your database name differs
    engine = create_engine("mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase")

elif choice == "2":
    # SQLite connection — no username or password needed
    # EmpDB.db is the local database file in the same folder as this script
    engine = create_engine("sqlite:///EmpDB.db")

else:
    # Fallback to SQLite if user enters anything other than 1 or 2
    print("Invalid choice. Using SQLite by default.")
    engine = create_engine("sqlite:///EmpDB.db")


# ── Step 3: Describe the Employee table ──────────────────────
# SQLAlchemy needs to know what the table looks like before it
# can query it. We describe it by creating a Python class.
# Each Column() maps directly to one column in the database.

class Base(DeclarativeBase):
    # DeclarativeBase is the required parent class for all table classes.
    # It links the class to SQLAlchemy's mapping system.
    pass

class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the table name in the DB

    # Column("db_column_name", DataType, options)
    # primary_key=True → this column uniquely identifies each row
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number, no decimals
    empCity      = Column("empCity",      String(50))    # max 50 characters
    empCountry   = Column("empCountry",   String(50))


# ── Step 4: Fetch data ────────────────────────────────────────
# Session is a temporary connection to the database.
# Using 'with' ensures the session is closed automatically
# when the block finishes, even if an error occurs.

with Session(engine) as session:

    # session.query(Employee)         → SELECT * FROM Employee
    # .order_by(Employee.empSalary.desc()) → ORDER BY empSalary DESC
    # .all()                          → fetch ALL matching rows as a list
    employees = (
        session.query(Employee)
               .order_by(Employee.empSalary.desc())
               .all()
    )

# At this point the session is closed.
# 'employees' is a plain Python list of Employee objects.


# ── Step 5: Print the results ────────────────────────────────
# f-strings let us embed variables directly inside a string.
# The format specifiers control alignment and width:
#   :<5   = left-align  in a field 5  characters wide
#   :<12  = left-align  in a field 12 characters wide
#   :>10  = right-align in a field 10 characters wide
#   :>9,  = right-align in a field 9  characters wide, with comma separator
#           e.g. 100000 → 100,000

print()
print(f"{'ID':<5} {'First Name':<12} {'Last Name':<15} {'Salary':>10}  {'City':<16} {'Country'}")
print("-" * 65)   # print a divider line 65 characters wide

# Loop through every employee object and print one line per row
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
print("Total employees:", len(employees))   # len() counts items in the list
