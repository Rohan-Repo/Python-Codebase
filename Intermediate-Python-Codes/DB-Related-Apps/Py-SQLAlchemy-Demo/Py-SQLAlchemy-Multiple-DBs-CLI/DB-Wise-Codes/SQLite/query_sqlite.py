# =============================================================
#  query_sqlite.py
#
#  PURPOSE  : Connects to a local SQLite database, fetches all
#             employees from the Employee table, and prints
#             them sorted by salary (highest first).
#
#  RUN      : python query_sqlite.py
#
#  REQUIRES : pip install sqlalchemy
#             SQLite itself needs no install — it is built
#             into Python. No username or password needed.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# Column, Integer, String  → used to describe table columns
# create_engine            → opens the connection to the database
# DeclarativeBase          → required base class for table classes
# Session                  → temporary workspace for running queries

from sqlalchemy     import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# ── Step 1: Connect to the SQLite database ───────────────────
# create_engine() sets up the connection.
# sqlite:///EmpDB.db means:
#   sqlite  → database type
#   ///     → relative path (3 slashes = relative, 4 = absolute)
#   EmpDB.db → the database file in the same folder as this script
#
# SQLite stores the entire database in a single .db file.
# No server, no username, no password needed.

engine = create_engine("sqlite:///EmpDB.db")


# ── Step 2: Describe the Employee table ──────────────────────
# SQLAlchemy needs to know what the table looks like before
# it can query it. We do this by writing a Python class.
# Each Column() maps directly to one column in the database.

class Base(DeclarativeBase):
    # DeclarativeBase is the required parent for all table classes.
    # It connects the class to SQLAlchemy's internal mapping system.
    pass

class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the DB table name

    # Column("db_column_name", DataType)
    # primary_key=True → this column uniquely identifies each row (the ID)
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number
    empCity      = Column("empCity",      String(50))    # max 50 characters
    empCountry   = Column("empCountry",   String(50))


# ── Step 3: Fetch data from the database ─────────────────────
# Session is a temporary connection to the database.
# Using 'with' ensures the session is closed automatically
# when the block finishes, even if an error occurs.

with Session(engine) as session:

    # This is the Python equivalent of:
    # SELECT * FROM Employee ORDER BY empSalary DESC
    #
    # session.query(Employee)              → which table to query
    # .order_by(Employee.empSalary.desc()) → sort by salary, high to low
    # .all()                               → return all rows as a list
    employees = (
        session.query(Employee)
               .order_by(Employee.empSalary.desc())
               .all()
    )

# Session is now closed.
# 'employees' is a plain Python list — each item is one Employee row.


# ── Step 4: Print the results ─────────────────────────────────
# f-strings let us embed variables directly inside a string.
# Format specifiers inside {} control spacing:
#   :<5   = left-align  in 5  character wide field
#   :<12  = left-align  in 12 character wide field
#   :>10  = right-align in 10 character wide field
#   :>9,  = right-align in 9  characters, comma as thousand separator
#           e.g. 100000 prints as 100,000

print()

# Print the header row
print(f"{'ID':<5} {'First Name':<12} {'Last Name':<15} {'Salary':>10}  {'City':<16} {'Country'}")

# Print a divider line 65 dashes wide
print("-" * 65)

# Loop through every Employee object in the list and print one line per row
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
# len() counts the number of items in the list
print("Total employees:", len(employees))
