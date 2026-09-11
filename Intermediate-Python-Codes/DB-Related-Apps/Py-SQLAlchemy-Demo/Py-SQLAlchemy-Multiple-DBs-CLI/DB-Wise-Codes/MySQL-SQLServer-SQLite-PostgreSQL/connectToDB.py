# =============================================================
#  connectToDB.py
#
#  PURPOSE  : Asks the user which database to connect to
#             (MySQL, SQL Server, PostgreSQL or SQLite) and
#             returns a ready-to-use engine plus the DB name.
#
#  USED BY  : query_normal.py
#             query_dataclass.py
#
#  WHY WE RETURN db NAME:
#    PostgreSQL automatically lowercases all column and table
#    names when you create them (unless you use quotes).
#    So "empId" becomes "empid" and "Employee" becomes "employee".
#    MySQL, SQL Server and SQLite keep the original casing.
#    The query files use the db name to pick the correct model.
# =============================================================

# create_engine builds the database connection from a URL string.
from sqlalchemy import create_engine


def pick_database():
    # ── Show the menu ─────────────────────────────────────────
    print("Pick a database:")
    print("1. MySQL")
    print("2. SQL Server")
    print("3. PostgreSQL")
    print("4. SQLite")

    choice = input("Enter 1, 2, 3 or 4: ")

    # ── Build connection string based on user choice ──────────
    # Connection string format:
    #   dialect+driver://username:password@host/database_name
    #
    # dialect → type of database  (mysql, mssql, postgresql, sqlite)
    # driver  → Python library    (pymysql, pyodbc, psycopg2)

    if choice == "1":
        # MySQL — update credentials and database name if needed
        url = "mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase"
        db  = "mysql"

    elif choice == "2":
        # SQL Server with Windows Authentication (no password required)
        # trusted_connection=yes uses your Windows login automatically
        # Change CompanyDatabase to your actual SQL Server database name
        url = "mssql+pyodbc://localhost/CompanyDatabase?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        db  = "sqlserver"

    elif choice == "3":
        # PostgreSQL — update credentials and database name if needed
        # Note: PostgreSQL lowercases all names, so the query files
        # use a different Employee model with lowercase column names
        url = "postgresql+psycopg2://compdbadmin:compdbadmin@localhost/companydatabase"
        db  = "postgresql"

    elif choice == "4":
        # SQLite — just a local file, no server or credentials needed
        # EmpDB.db must be in the same folder as this script
        url = "sqlite:///EmpDB.db"
        db  = "sqlite"

    else:
        # Default to SQLite if input is not 1, 2, 3 or 4
        print("Invalid choice. Using SQLite by default.")
        url = "sqlite:///EmpDB.db"
        db  = "sqlite"

    # ── Create the engine ─────────────────────────────────────
    # create_engine() prepares the connection but does NOT open it yet.
    # The connection opens when a Session is started in the query files.
    engine = create_engine(url)

    # Return the engine (for querying) and db name (for model selection)
    return engine, db
