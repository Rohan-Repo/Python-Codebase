# =============================================================
#  gui_grid_all_DBs.py
#
#  PURPOSE  : Connects to SQLite, MySQL, SQL Server or PostgreSQL,
#             fetches all employees and displays them in a GUI
#             grid window with radio button database selection.
#
#  APPROACH : Single file — all database config, ORM models,
#             data fetching and GUI code in one place.
#             See GUI-MVC-Code folder for the same app split
#             into separate Model / Controller / View files.
#
#  RUN      : python gui_grid_all_DBs.py
#
#  REQUIRES : pip install sqlalchemy pymysql pyodbc psycopg2-binary
#             tkinter is built into Python — no install needed.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# tkinter   → Python's built-in GUI library, ships with Python
# tk        → the main module: windows, labels, buttons, frames
# ttk       → themed widgets: Treeview and Scrollbar look cleaner
# messagebox→ pop-up dialog boxes for showing errors
import tkinter as tk
from tkinter import ttk, messagebox

# SQLAlchemy — the library that lets Python talk to databases
# Column, Integer, String → describe the shape of table columns
# create_engine           → builds the DB connection from a URL string
# DeclarativeBase         → required parent for all ORM table classes
# Session                 → temporary workspace for running queries
from sqlalchemy     import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# =============================================================
#  DATABASE CONNECTION STRINGS
#
#  DB_URLS is a Python dictionary.
#  Keys   → the label shown on each radio button in the GUI
#  Values → another dictionary with:
#    "url"        → the connection string SQLAlchemy uses to connect
#    "postgresql" → True/False flag to select the right ORM model
#
#  Connection string format:
#    dialect+driver://username:password@host/database_name
#    dialect → type of database  (sqlite, mysql, mssql, postgresql)
#    driver  → Python library    (pymysql, pyodbc, psycopg2)
#
#  UPDATE the credentials below to match your own setup.
# =============================================================

DB_URLS = {
    "SQLite": {
        # Local file — no server, no username, no password needed.
        # sqlite:/// (3 slashes) = path relative to the current folder.
        "url"       : "sqlite:///EmpDB.db",
        "postgresql": False
    },
    "MySQL": {
        # Update compdbadmin:compdbadmin → your MySQL username:password
        # Update CompanyDatabase         → your MySQL database name
        "url"       : "mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase",
        "postgresql": False
    },
    "SQL Server": {
        # trusted_connection=yes → Windows Authentication, no password needed.
        # Update CompanyDatabase → your SQL Server database name.
        # For username/password: mssql+pyodbc://USER:PASS@host/DB?driver=...
        "url"       : "mssql+pyodbc://localhost/CompanyDatabase?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes",
        "postgresql": False
    },
    "PostgreSQL": {
        # Update compdbadmin:compdbadmin → your PostgreSQL username:password
        # Update companydatabase         → your PostgreSQL database name
        # postgresql=True → tells fetch_employees() to use EmployeePG below
        "url"       : "postgresql+psycopg2://compdbadmin:compdbadmin@localhost/companydatabase",
        "postgresql": True
    },
}


# =============================================================
#  ORM MODELS
#
#  WHY TWO MODELS?
#  PostgreSQL lowercases all table and column names at storage time.
#  A column created as "empId" is stored as "empid".
#  Asking PostgreSQL for "empId" causes a "column not found" error.
#  Fix: use a second model with all-lowercase names for PostgreSQL.
#  MySQL, SQL Server and SQLite keep original casing → one shared model.
# =============================================================

# All SQLAlchemy table classes must inherit from Base
class Base(DeclarativeBase):
    pass


# ── Model for SQLite · MySQL · SQL Server ────────────────────
# These databases keep the original column name casing.
class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the DB table name

    # Column("db_column_name", DataType, options)
    # primary_key=True → uniquely identifies each row
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number
    empCity      = Column("empCity",      String(50))    # max 50 characters
    empCountry   = Column("empCountry",   String(50))


# ── Model for PostgreSQL only ─────────────────────────────────
# All names must match what PostgreSQL actually stored (all lowercase).
# The Python attribute names on the left stay the same as above —
# only the DB column name strings (inside Column()) are lowercase.
class EmployeePG(Base):
    __tablename__ = "employee"                                      # lowercase

    empId        = Column("empid",        Integer, primary_key=True)
    empFirstName = Column("empfirstname", String(30))
    empLastName  = Column("emplastname",  String(30))
    empSalary    = Column("empsalary",    Integer)
    empCity      = Column("empcity",      String(50))
    empCountry   = Column("empcountry",   String(50))


# =============================================================
#  DATA FETCHING
# =============================================================

def fetch_employees(db_name):
    """
    Connect to the chosen database and return all employees
    sorted by salary from highest to lowest.

    Parameter:
        db_name (str) → "SQLite", "MySQL", "SQL Server" or "PostgreSQL"
                        This matches the radio button labels and DB_URLS keys.

    Returns:
        A list of Employee or EmployeePG objects.
    """
    # Look up the config dictionary for the chosen database
    config = DB_URLS[db_name]

    # create_engine() builds the connection from the URL string
    engine = create_engine(config["url"])

    # Choose the right model based on the "postgresql" flag:
    # Ternary: result = value_if_true  if  condition  else  value_if_false
    # True  → EmployeePG (lowercase column names for PostgreSQL)
    # False → Employee   (original casing for everyone else)
    model = EmployeePG if config["postgresql"] else Employee

    # Open a session, run the query, close automatically with 'with'
    with Session(engine) as session:
        # SELECT * FROM Employee ORDER BY empSalary DESC
        # .query(model)                     → which table to read
        # .order_by(model.empSalary.desc()) → sort salary high to low
        # .all()                            → return all rows as a list
        return session.query(model).order_by(model.empSalary.desc()).all()


# =============================================================
#  GUI FUNCTIONS
# =============================================================

def load_data():
    """
    Called when the user clicks Load Data.
    Clears the grid, fetches fresh data, fills it back in.
    """

    # Step 1: Clear all existing rows from the grid
    # tree.get_children() returns the IDs of every row currently in the grid
    for row in tree.get_children():
        tree.delete(row)

    # Step 2: Show "Loading..." in the status bar and force a redraw
    # root.update() makes tkinter refresh the window immediately
    # so the user sees the message before the DB query runs
    status.set("Loading...")
    root.update()

    # Step 3: Fetch data from the database
    # db_choice.get() reads the currently selected radio button value
    # try/except shows a friendly popup if the connection fails
    # instead of crashing the whole program
    try:
        employees = fetch_employees(db_choice.get())
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        status.set("Failed to connect.")
        return   # stop here — don't try to fill the grid

    # Step 4: Insert each employee as one row in the Treeview
    # enumerate() gives both the index i (for row colouring) and
    # the employee object emp (for the actual column data)
    for i, emp in enumerate(employees):

        # Alternating row colour:
        # i % 2 == 0 → even index (0, 2, 4...) → light blue ("odd" tag)
        # i % 2 != 0 → odd  index (1, 3, 5...) → white      ("even" tag)
        tag = "odd" if i % 2 == 0 else "even"

        # tree.insert() adds one row to the grid
        # ""        → insert at root level (not nested)
        # tk.END    → append at the bottom
        # tag=tag   → apply the row background colour
        # values=() → column data in same order as 'columns' tuple below
        tree.insert("", tk.END, tag=tag, values=(
            emp.empId,
            emp.empFirstName,
            emp.empLastName,
            f"${emp.empSalary:,}",   # :, adds thousand separator → $100,000
            emp.empCity,
            emp.empCountry,
        ))

    # Step 5: Update the status bar with the final result
    status.set(f"Total employees: {len(employees)}   |   Source: {db_choice.get()}")


# =============================================================
#  GUI LAYOUT
#  Built top to bottom with .pack()
# =============================================================

# ── Main window ───────────────────────────────────────────────
root = tk.Tk()
root.title("Employee Viewer")     # text in the OS title bar
root.geometry("860x520")          # starting size: 860 wide × 520 tall pixels
root.resizable(True, True)        # user can resize both width and height


# ── Title label ───────────────────────────────────────────────
# tk.Label shows static text
# font=("Arial", 14, "bold") → family, point size, weight
# pady=8 → 8 pixels of space above and below
tk.Label(
    root, text="Employee Viewer",
    font=("Arial", 14, "bold"), pady=8
).pack()   # .pack() stacks vertically inside the window


# ── Top bar: radio buttons + Load button ──────────────────────
# tk.Frame is an invisible container; fill=tk.X stretches it full width
top = tk.Frame(root, pady=6, padx=10)
top.pack(fill=tk.X)

# "Select Database:" label
tk.Label(top, text="Select Database:", font=("Arial", 11)).pack(
    side=tk.LEFT, padx=(0, 10)   # 0 left padding, 10 right padding
)

# tk.StringVar stores the active radio button selection as text
# value="SQLite" → SQLite is pre-selected when the window opens
db_choice = tk.StringVar(value="SQLite")

# Create one radio button for each database in DB_URLS
# All share db_choice so only one can be selected at a time
# DB_URLS.keys() → ["SQLite", "MySQL", "SQL Server", "PostgreSQL"]
for db_name in DB_URLS.keys():
    tk.Radiobutton(
        top,
        text=db_name,             # label shown next to the button
        variable=db_choice,       # shared variable — all buttons write here
        value=db_name,            # value stored when this button is selected
        font=("Arial", 11)
    ).pack(side=tk.LEFT, padx=6)

# Load Data button — blue, runs load_data() on click
tk.Button(
    top, text="  Load Data  ",
    font=("Arial", 11, "bold"),
    bg="#2563EB", fg="white",     # blue background, white label text
    padx=10, pady=4,
    command=load_data             # function called when button is clicked
).pack(side=tk.LEFT, padx=20)


# ── Grid (Treeview) ───────────────────────────────────────────
# Column header names — order must match values= in tree.insert()
columns = ("ID", "First Name", "Last Name", "Salary", "City", "Country")

# Container frame for the Treeview and both scrollbars
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=4)
# fill=tk.BOTH → grow in both directions
# expand=True  → use all remaining window space

# Vertical scrollbar — up/down
scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)    # right edge, full height

# Horizontal scrollbar — left/right
scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)   # bottom edge, full width

# ttk.Treeview — the actual data grid widget
# show="headings" → hide the default tree icon column
# yscrollcommand / xscrollcommand → link the scrollbars to the grid
tree = ttk.Treeview(
    frame,
    columns=columns,
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set,
)

# Connect scrollbars back to the grid so they move together
scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)
tree.pack(fill=tk.BOTH, expand=True)

# Set the header text and pixel width for each column
col_widths = {
    "ID"        : 50,     # narrow — just a number
    "First Name": 110,
    "Last Name" : 130,
    "Salary"    : 100,
    "City"      : 140,
    "Country"   : 120,
}
for col in columns:
    tree.heading(col, text=col)                                   # column header label
    tree.column(col, width=col_widths[col], anchor=tk.CENTER)    # width, centred text

# Define alternating row colours using named tags
# Applied in load_data() via tag= in tree.insert()
tree.tag_configure("odd",  background="#EFF6FF")   # light blue
tree.tag_configure("even", background="#FFFFFF")   # white


# ── Status bar ────────────────────────────────────────────────
# tk.StringVar → status.set("text") instantly updates the linked label
status = tk.StringVar(value="Select a database and click Load Data")

# textvariable=status → label text is driven by the StringVar
# anchor=tk.W         → left-align text (West side of the label)
tk.Label(
    root, textvariable=status,
    anchor=tk.W, font=("Arial", 9), fg="grey"
).pack(fill=tk.X, padx=10, pady=6)


# ── Start the application ─────────────────────────────────────
# root.mainloop() starts the tkinter event loop.
# It keeps the window alive and responds to every user action
# (button clicks, resizing, closing) until the window is shut.
root.mainloop()
