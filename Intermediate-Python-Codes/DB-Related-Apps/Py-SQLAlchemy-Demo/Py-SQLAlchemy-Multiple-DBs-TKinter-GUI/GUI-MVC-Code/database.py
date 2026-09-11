# =============================================================
#  database.py  —  DB Connectivity layer in MVC
#
#  PURPOSE  : Stores all four database connection strings in
#             one place and exposes two helper functions:
#               get_engine()     → returns a live DB connection
#               is_postgresql()  → returns True for PostgreSQL
#
#  WHY CENTRALISE HERE?
#    If credentials or database names ever change, you only
#    edit this one file. model.py, controller.py and view.py
#    stay completely untouched.
#
#  UPDATE   : Replace USERNAME, PASSWORD and database names
#             with your own credentials before running.
# =============================================================

# create_engine → builds the database connection from a URL string
from sqlalchemy import create_engine


# ── DB_URLS: connection config for all four databases ─────────
# This is a Python dictionary of dictionaries.
# Outer keys  → the database name shown in the GUI radio buttons.
# Inner keys:
#   "url"        → the connection string SQLAlchemy uses to connect
#   "postgresql" → True/False flag so controller.py knows which
#                  ORM model to use (PostgreSQL needs lowercase names)
#
# Connection string format:
#   dialect+driver://username:password@host/database_name
#
#   dialect → the type of database   (sqlite, mysql, mssql, postgresql)
#   driver  → the Python library     (pymysql, pyodbc, psycopg2)
#   host    → the server address     (localhost = your own machine)

DB_URLS = {
    "SQLite": {
        # SQLite stores everything in a single local file.
        # No server, no username, no password needed.
        # sqlite:/// (three slashes) = path relative to the current folder.
        # EmpDB.db must be in the same folder as this script.
        "url"        : "sqlite:///EmpDB.db",
        "postgresql" : False
    },
    "MySQL": {
        # Update compdbadmin:compdbadmin → your MySQL username:password
        # Update CompanyDatabase        → your MySQL database name
        "url"        : "mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase",
        "postgresql" : False
    },
    "SQL Server": {
        # trusted_connection=yes → uses Windows Authentication.
        # No username or password needed — uses your Windows login.
        # Update CompanyDatabase → your SQL Server database name.
        # For username/password auth instead, use:
        # mssql+pyodbc://USERNAME:PASSWORD@localhost/DB?driver=ODBC+Driver+17+for+SQL+Server
        "url"        : "mssql+pyodbc://localhost/CompanyDatabase?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes",
        "postgresql" : False
    },
    "PostgreSQL": {
        # Update compdbadmin:compdbadmin → your PostgreSQL username:password
        # Update companydatabase         → your PostgreSQL database name
        # postgresql=True tells the controller to use the EmployeePG model
        # (which has all-lowercase column names to match PostgreSQL storage)
        "url"        : "postgresql+psycopg2://compdbadmin:compdbadmin@localhost/companydatabase",
        "postgresql" : True
    },
}


def get_engine(db_name):
    """
    Build and return a SQLAlchemy engine for the chosen database.

    Parameter:
        db_name (str) → "SQLite", "MySQL", "SQL Server" or "PostgreSQL"
                        This matches the keys in DB_URLS above.

    Returns:
        A SQLAlchemy Engine object ready to be used by a Session.

    Note: create_engine() PREPARES the connection but does NOT open it.
          The connection opens when Session(engine) is called in controller.py.
    """
    url = DB_URLS[db_name]["url"]     # look up the URL for this database
    return create_engine(url)          # build and return the engine


def is_postgresql(db_name):
    """
    Return True if the chosen database is PostgreSQL, False otherwise.

    Used by controller.py to decide which ORM model to use:
        True  → use EmployeePG (all-lowercase column names)
        False → use Employee   (original mixed-case column names)
    """
    return DB_URLS[db_name]["postgresql"]
