# =============================================================
#  gui_grid_sqlite_mysql.py
#
#  PURPOSE  : Connects to SQLite or MySQL, fetches all employees
#             and displays them in a GUI grid window.
#
#  APPROACH : Single file — database connection, table model,
#             data fetching and GUI all in one place.
#             Great for learning before moving to MVC structure.
#
#  RUN      : python gui_grid_sqlite_mysql.py
#
#  REQUIRES : pip install sqlalchemy pymysql
#             tkinter is built into Python — no install needed.
# =============================================================

# ── Imports ──────────────────────────────────────────────────
# tkinter   → Python's built-in GUI library
# tk        → main module: windows, widgets, layout
# ttk       → themed widgets: Treeview and Scrollbar look cleaner
# messagebox→ pop-up error dialogs
import tkinter as tk
from tkinter import ttk, messagebox

# SQLAlchemy tools for database connectivity
# Column, Integer, String → describe the shape of each table column
# create_engine           → builds the database connection from a URL
# DeclarativeBase         → required parent class for ORM table classes
# Session                 → temporary workspace for running DB queries
from sqlalchemy     import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# =============================================================
#  DATABASE SETUP
# =============================================================

# Every SQLAlchemy table class must inherit from Base
class Base(DeclarativeBase):
    pass


# Employee class mirrors the Employee table in the database.
# Each Column() maps one Python attribute to one database column.
class Employee(Base):
    __tablename__ = "Employee"   # must exactly match the DB table name

    # Column("db_column_name", DataType, options)
    # primary_key=True → uniquely identifies each row (the ID column)
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))   # max 30 characters
    empLastName  = Column("empLastName",  String(30))
    empSalary    = Column("empSalary",    Integer)       # whole number salary
    empCity      = Column("empCity",      String(50))    # max 50 characters
    empCountry   = Column("empCountry",   String(50))


def get_engine(choice):
    """
    Build and return a SQLAlchemy engine based on the DB choice.

    choice → "MySQL" or "SQLite" (from the GUI radio buttons)

    Connection string format:
      dialect+driver://username:password@host/database_name
    """
    if choice == "MySQL":
        # Update compdbadmin:compdbadmin → your MySQL username:password
        # Update CompanyDatabase         → your MySQL database name
        return create_engine("mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase")
    else:
        # SQLite — no server, no credentials needed
        # EmpDB.db is a local file in the same folder as this script
        return create_engine("sqlite:///EmpDB.db")


def fetch_employees(choice):
    """
    Connect to the chosen database and return all employees
    sorted by salary from highest to lowest.

    Returns a list of Employee objects.
    Each object has attributes: empId, empFirstName, empLastName,
    empSalary, empCity, empCountry — accessible with dot notation.
    """
    engine = get_engine(choice)

    # 'with Session' opens a temporary connection and closes it
    # automatically when the indented block finishes
    with Session(engine) as session:
        # SELECT * FROM Employee ORDER BY empSalary DESC
        # .query(Employee) → which table to read
        # .order_by(...)   → sort by salary, high to low
        # .all()           → fetch every matching row as a list
        return session.query(Employee).order_by(Employee.empSalary.desc()).all()


# =============================================================
#  GUI FUNCTIONS
# =============================================================

def load_data():
    """
    Called when the user clicks Load Data.
    Clears the grid, fetches fresh data from the DB, fills it in.
    """

    # Step 1: Remove all existing rows from the grid
    # tree.get_children() returns the internal IDs of all current rows
    for row in tree.get_children():
        tree.delete(row)

    # Step 2: Fetch employees — if the connection fails, show a popup
    # db_choice.get() reads the currently selected radio button value
    # try/except catches any error and shows it in a dialog box
    try:
        employees = fetch_employees(db_choice.get())
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        return   # stop here — nothing to display if the query failed

    # Step 3: Insert each employee as one row in the Treeview grid
    for emp in employees:
        # tree.insert() adds one row
        # ""        → root-level row (not nested inside another row)
        # tk.END    → append at the bottom of the existing rows
        # values=() → the data for each column, in the same order
        #             as the 'columns' tuple defined below
        tree.insert("", tk.END, values=(
            emp.empId,
            emp.empFirstName,
            emp.empLastName,
            f"${emp.empSalary:,}",   # :, formats with comma → $100,000
            emp.empCity,
            emp.empCountry,
        ))

    # Step 4: Update the status bar with how many rows were loaded
    status.set(f"Total employees: {len(employees)}  |  Source: {db_choice.get()}")


# =============================================================
#  GUI LAYOUT
#  Widgets are built top to bottom using .pack()
# =============================================================

# ── Main window ───────────────────────────────────────────────
# tk.Tk() creates the root application window
root = tk.Tk()
root.title("Employee Viewer")     # text in the OS title bar
root.geometry("800x500")          # starting size: width x height in pixels
root.resizable(True, True)        # allow resizing in both directions


# ── Top bar ───────────────────────────────────────────────────
# tk.Frame groups widgets side by side inside a container
# fill=tk.X → stretch the frame to the full window width
top = tk.Frame(root, pady=8, padx=10)
top.pack(fill=tk.X)

# Static label for the radio button group
tk.Label(top, text="Database:", font=("Arial", 11)).pack(side=tk.LEFT)

# tk.StringVar stores the selected radio button value as a string.
# value="SQLite" → SQLite is selected by default when the window opens.
db_choice = tk.StringVar(value="SQLite")

# Two radio buttons — both share db_choice so only one can be active.
# Clicking a button sets db_choice to that button's value.
tk.Radiobutton(top, text="SQLite", variable=db_choice, value="SQLite", font=("Arial", 11)).pack(side=tk.LEFT, padx=6)
tk.Radiobutton(top, text="MySQL",  variable=db_choice, value="MySQL",  font=("Arial", 11)).pack(side=tk.LEFT, padx=6)

# Load Data button — calls load_data() when clicked
# bg="#2563EB" → blue background    fg="white" → white text
tk.Button(
    top, text="Load Data", font=("Arial", 11),
    bg="#2563EB", fg="white", padx=12, pady=4,
    command=load_data   # function to call when the button is clicked
).pack(side=tk.LEFT, padx=20)


# ── Grid (Treeview) ───────────────────────────────────────────
# Column names — order must match values= in tree.insert() above
columns = ("ID", "First Name", "Last Name", "Salary", "City", "Country")

# Frame to hold the grid and scrollbars together as a unit
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=4)
# fill=tk.BOTH → stretch in both directions
# expand=True  → take up all remaining space in the window

# Vertical scrollbar — up/down scrolling
scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)   # pin to the right edge

# Horizontal scrollbar — left/right scrolling
scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)  # pin to the bottom edge

# ttk.Treeview — the grid widget itself
# show="headings" → hide the default tree icon column
# yscrollcommand / xscrollcommand → link the scrollbars to the grid
tree = ttk.Treeview(
    frame,
    columns=columns,
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set,
)

# Connect scrollbars to the grid so they move in sync
scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)
tree.pack(fill=tk.BOTH, expand=True)

# Set the header label and pixel width for each column
# anchor=tk.CENTER → centre-align the text inside each column
col_widths = {"ID": 50, "First Name": 110, "Last Name": 130, "Salary": 100, "City": 130, "Country": 120}
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=col_widths[col], anchor=tk.CENTER)

# Alternating row background colours using named tags
# "odd"  → light blue (applied to even-index rows: 0, 2, 4...)
# "even" → white      (applied to odd-index rows:  1, 3, 5...)
tree.tag_configure("odd",  background="#F0F4FF")
tree.tag_configure("even", background="#FFFFFF")


# ── Status bar ────────────────────────────────────────────────
# tk.StringVar → calling status.set("text") instantly updates the label
status = tk.StringVar(value="Select a database and click Load Data")

# textvariable=status → the label reads its text from the StringVar
# anchor=tk.W         → left-align the text (West side)
tk.Label(root, textvariable=status, anchor=tk.W, font=("Arial", 9), fg="grey").pack(
    fill=tk.X, padx=10, pady=4
)


# ── Start the application ─────────────────────────────────────
# root.mainloop() starts the tkinter event loop.
# It keeps the window open and listens for user actions
# (clicks, typing, resizing, closing) until the window is closed.
root.mainloop()
