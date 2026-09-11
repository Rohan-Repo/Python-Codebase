# =============================================================
#  database_MS_SS_S.py
#
#  PURPOSE  : Asks the user which database to connect to
#             (MySQL, SQL Server or SQLite) and returns a
#             ready-to-use database engine plus the DB name.
#
#  USED BY  : query_normal_MS_SS_S.py
#             query_dataclass_MS_SS_S.py
#
#  NOTE     : This folder covers MySQL, SQL Server and SQLite
#             only. For PostgreSQL support see the
#             MySQL-SQLServer-SQLite-PostgreSQL folder.
# =============================================================

# create_engine builds the connection to whichever database
# the user picks. It is the starting point for all DB work.
from sqlalchemy import create_engine


def pick_database():
    # ── Show the menu ─────────────────────────────────────────
    # print() displays text in the terminal.
    # input() shows a prompt and waits for the user to type.
    print("Pick a database:")
    print("1. MySQL")
    print("2. SQL Server")
    print("3. SQLite")

    choice = input("Enter 1, 2 or 3: ")

    # ── Build the connection string based on the choice ───────
    # The connection string (url) tells SQLAlchemy HOW to connect.
    # Format:  dialect+driver://username:password@host/database_name
    #
    # dialect = which database  e.g. mysql, mssql, sqlite
    # driver  = which library   e.g. pymysql, pyodbc
    # We also return 'db' so the query files know which database
    # is active — important because PostgreSQL uses different
    # column name casing (though not needed in this folder).

    if choice == "1":
        # MySQL — update username/password/database name if yours differ
        url = "mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase"
        db  = "mysql"

    elif choice == "2":
        # SQL Server using Windows Authentication (trusted_connection=yes)
        # Change CompanyDatabase to your actual database name
        # If you use a username/password instead of Windows auth, replace with:
        # mssql+pyodbc://USERNAME:PASSWORD@localhost/DATABASE?driver=ODBC+Driver+17+for+SQL+Server
        url = "mssql+pyodbc://localhost/CompanyDatabase?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        db  = "sqlserver"

    elif choice == "3":
        # SQLite — no username or password needed
        # EmpDB.db is the local file in the same folder as this script
        url = "sqlite:///EmpDB.db"
        db  = "sqlite"

    else:
        # If the user types anything other than 1, 2 or 3, default to SQLite
        print("Invalid choice. Using SQLite by default.")
        url = "sqlite:///EmpDB.db"
        db  = "sqlite"

    # ── Create and return the engine ──────────────────────────
    # create_engine() uses the url string to set up the connection.
    # It does NOT open the connection yet — it just prepares it.
    # The actual connection happens when we open a Session later.
    engine = create_engine(url)

    # Return BOTH the engine (for querying) and db (to identify
    # which database was chosen, so query files can act accordingly)
    return engine, db
