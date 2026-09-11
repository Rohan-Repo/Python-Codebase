# =============================================================
#  controller.py  —  C in MVC
#
#  PURPOSE  : The bridge between view.py (the GUI) and the
#             database files (database.py + model.py).
#
#  MVC RULE : The view (GUI) NEVER talks to the database.
#             It calls get_all_employees() here instead.
#             This keeps all database logic in one place and
#             the GUI code clean and easy to understand.
#
#  MVC FLOW :
#    view.py        calls  → get_all_employees(db_name)
#    controller.py  asks   → database.py  for an engine
#                   uses   → model.py     for table structure
#                   runs   → the query
#                   returns→ plain list back to view.py
# =============================================================

# Session → temporary workspace for running database queries
# 'with Session' opens it and closes it automatically when done
from sqlalchemy.orm import Session

# get_engine    → returns a live engine (DB connection) for the chosen DB
# is_postgresql → returns True if PostgreSQL was selected
from database import get_engine, is_postgresql

# Employee   → ORM model for SQLite, MySQL, SQL Server (mixed-case columns)
# EmployeePG → ORM model for PostgreSQL (all-lowercase columns)
from model import Employee, EmployeePG


def get_all_employees(db_name):
    """
    Fetch all employees from the chosen database,
    sorted by salary from highest to lowest.

    Parameter:
        db_name (str) → "SQLite", "MySQL", "SQL Server" or "PostgreSQL"
                        Passed in from the radio button selection in view.py.

    Returns:
        A list of Employee (or EmployeePG) objects.
        Each object has attributes accessible with dot notation:
        emp.empId, emp.empFirstName, emp.empLastName,
        emp.empSalary, emp.empCity, emp.empCountry
    """

    # Step 1: Get the database engine (connection) for the chosen DB
    # get_engine() reads the correct URL from database.py and returns
    # a SQLAlchemy engine ready to be used
    engine = get_engine(db_name)

    # Step 2: Choose the correct ORM model for this database
    # PostgreSQL stores column names in lowercase → use EmployeePG
    # All other databases keep original casing    → use Employee
    #
    # This is a ternary (one-line if/else):
    #   result = value_if_true  if  condition  else  value_if_false
    model = EmployeePG if is_postgresql(db_name) else Employee

    # Step 3: Open a session, run the query, close automatically
    # 'with Session(engine) as session' ensures the connection is
    # closed cleanly even if an error occurs during the query
    with Session(engine) as session:

        # This is the Python equivalent of:
        #   SELECT * FROM Employee ORDER BY empSalary DESC
        #
        # .query(model)                     → which table to read from
        # .order_by(model.empSalary.desc()) → sort salary high to low
        # .all()                            → return every row as a list
        employees = (
            session.query(model)
                   .order_by(model.empSalary.desc())
                   .all()
        )

    # Step 4: Return the list to view.py
    # The session is now closed but the employee objects are still
    # fully accessible — their attribute values are loaded in memory
    return employees
