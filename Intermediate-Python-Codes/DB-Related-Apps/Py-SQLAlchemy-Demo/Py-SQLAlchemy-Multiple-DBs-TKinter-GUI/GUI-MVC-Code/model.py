# =============================================================
#  model.py  —  M in MVC
#
#  PURPOSE  : Describes what the Employee table looks like.
#             SQLAlchemy uses these classes to understand which
#             columns exist and what data types they hold.
#             This file has NO logic — it is purely a description.
#
#  WHY TWO CLASSES?
#    PostgreSQL silently lowercases all column and table names
#    at storage time. A column created as "empId" is stored as
#    "empid". If we ask PostgreSQL for "empId" it says the column
#    does not exist. Fix: a second model with all-lowercase names.
#    MySQL, SQL Server and SQLite keep the original casing, so
#    they share one model.
#
#  USED BY  : controller.py picks the right model based on
#             which database the user selected.
# =============================================================

# Column   → represents one column in the database table
# Integer  → whole number data type  (e.g. 1, 42, 100000)
# String   → text data type with a max character length
from sqlalchemy     import Column, Integer, String

# DeclarativeBase → required parent class for all ORM table classes
# It registers the class with SQLAlchemy's mapping system
from sqlalchemy.orm import DeclarativeBase


# All table classes must inherit from Base
class Base(DeclarativeBase):
    pass


# ── Model 1: SQLite · MySQL · SQL Server ─────────────────────
# These databases keep the exact casing used when the table was created.
# "empId", "empFirstName" etc. are stored and retrieved exactly as written.

class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the table name in the DB

    # Column("db_column_name", DataType, options)
    # The first argument is the column name as it exists in the database.
    # The attribute name on the left (e.g. empId) is what we use in Python.
    # primary_key=True → this column uniquely identifies each row
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number, no decimals
    empCity      = Column("empCity",      String(50))    # max 50 characters
    empCountry   = Column("empCountry",   String(50))


# ── Model 2: PostgreSQL only ──────────────────────────────────
# PostgreSQL lowercases all names at storage time.
# "Employee" → "employee"    "empId" → "empid"    "empSalary" → "empsalary"
# We must use the lowercase versions here so SQLAlchemy sends the
# right column names in its SQL queries to PostgreSQL.
# Note: the Python attribute names (left side) stay the same as above —
# only the DB column name strings (first argument of Column) are lowercase.

class EmployeePG(Base):
    __tablename__ = "employee"                                      # lowercase

    empId        = Column("empid",        Integer, primary_key=True)
    empFirstName = Column("empfirstname", String(30))
    empLastName  = Column("emplastname",  String(30))
    empSalary    = Column("empsalary",    Integer)
    empCity      = Column("empcity",      String(50))
    empCountry   = Column("empcountry",   String(50))
