# =============================================================
#  view.py  —  V in MVC
#
#  PURPOSE  : Builds and displays the GUI window.
#             When the user clicks Load Data, it asks the
#             controller for employee data and fills the grid.
#
#  MVC RULE : This file NEVER imports from database.py or
#             model.py directly. All data comes through
#             controller.get_all_employees(). Keeping the GUI
#             separate from the database means you can swap
#             either side without touching the other.
#
#  RUN      : python view.py
#
#  REQUIRES : pip install sqlalchemy pymysql pyodbc psycopg2-binary
#             tkinter is built into Python — no extra install needed.
# =============================================================

# tkinter   → Python's built-in GUI library, no install needed
# tk        → the main module: windows, labels, buttons, frames
# ttk       → themed widgets: Treeview and Scrollbar look more modern
# messagebox→ built-in pop-up dialogs for showing error messages
import tkinter as tk
from tkinter    import ttk, messagebox

# get_all_employees → the only function we call from the controller
# The view only ever talks to the controller, never the database directly
from controller import get_all_employees


# =============================================================
#  load_data()
#  This function runs every time the user clicks "Load Data".
#  It clears the grid, fetches fresh data, and fills it in.
# =============================================================

def load_data():
    """Ask the controller for data and populate the grid."""

    # ── Step 1: Clear all existing rows ──────────────────────
    # tree.get_children() returns a list of IDs for every row
    # currently in the grid. We delete them all before reloading.
    for row in tree.get_children():
        tree.delete(row)

    # ── Step 2: Show "Loading..." while we wait ───────────────
    # status is a tk.StringVar — calling .set() instantly updates
    # the status bar label at the bottom of the window.
    # root.update() forces tkinter to redraw the window immediately
    # so the user sees "Loading..." before the query runs.
    status.set("Loading...")
    root.update()

    # ── Step 3: Ask the controller for data ───────────────────
    # db_choice.get() reads the currently selected radio button value
    # e.g. "SQLite", "MySQL", "SQL Server" or "PostgreSQL"
    # We wrap it in try/except so a failed DB connection shows a
    # friendly error popup instead of crashing the whole program.
    try:
        employees = get_all_employees(db_choice.get())
    except Exception as e:
        # messagebox.showerror() shows a popup dialog with the error text
        messagebox.showerror("Connection Error", str(e))
        status.set("Failed to connect.")
        return   # stop here — don't try to populate an empty grid

    # ── Step 4: Insert each employee as one row in the grid ───
    # enumerate() gives us both:
    #   i   → the row index (0, 1, 2, 3...) used for alternating colours
    #   emp → the Employee object with all the data attributes
    for i, emp in enumerate(employees):

        # Alternating row background colour using tags:
        # i % 2 == 0 means "i is even" (rows 0, 2, 4, 6...)
        # Even-index rows → tag "odd"  (light blue background)
        # Odd-index rows  → tag "even" (white background)
        # The tag colours are defined later with tree.tag_configure()
        tag = "odd" if i % 2 == 0 else "even"

        # tree.insert() adds one row to the Treeview grid
        # ""        → insert at the root level (no parent, not nested)
        # tk.END    → append this row at the bottom of the list
        # tag=tag   → apply the background colour tag to this row
        # values=() → the data for each column, must be in the same
        #             order as the 'columns' tuple defined below
        tree.insert("", tk.END, tag=tag, values=(
            emp.empId,
            emp.empFirstName,
            emp.empLastName,
            f"${emp.empSalary:,}",   # :, adds comma separator → $100,000
            emp.empCity,
            emp.empCountry,
        ))

    # ── Step 5: Update the status bar with the result ─────────
    # len(employees) counts how many rows were returned
    # db_choice.get() shows which database was used
    status.set(f"Total employees: {len(employees)}   |   Source: {db_choice.get()}")


# =============================================================
#  MAIN WINDOW
#  tk.Tk() creates the main application window.
#  All widgets below are placed inside this window.
# =============================================================

root = tk.Tk()
root.title("Employee Viewer")     # text displayed in the window title bar
root.geometry("860x520")          # starting size: 860 pixels wide, 520 tall
root.resizable(True, True)        # allow the user to resize width and height


# ── Title label ───────────────────────────────────────────────
# tk.Label displays static (non-editable) text
# font=("Arial", 14, "bold") → font family, point size, weight
# pady=8 → 8 pixels of empty space above and below the label
# .pack() places the widget in the window, stacking vertically by default
tk.Label(
    root, text="Employee Viewer",
    font=("Arial", 14, "bold"), pady=8
).pack()


# ── Top bar: radio buttons + Load button ──────────────────────
# tk.Frame is an invisible container widget used to group other
# widgets and lay them out side by side (left to right)
# pady / padx → empty space outside the frame
# fill=tk.X   → stretch the frame to fill the full window width
top = tk.Frame(root, pady=6, padx=10)
top.pack(fill=tk.X)

# Static label: "Select Database:"
# padx=(0, 10) → 0 pixels left, 10 pixels right of the label
tk.Label(top, text="Select Database:", font=("Arial", 11)).pack(
    side=tk.LEFT, padx=(0, 10)
)

# tk.StringVar is a special tkinter variable.
# Widgets linked to it automatically update when its value changes.
# value="SQLite" → the SQLite radio button is pre-selected on startup
db_choice = tk.StringVar(value="SQLite")

# Create one radio button for each database
# All buttons share the same 'variable=db_choice' — selecting one
# button sets db_choice to that button's 'value' and deselects the others
# side=tk.LEFT → buttons appear left to right inside the top frame
for db_name in ["SQLite", "MySQL", "SQL Server", "PostgreSQL"]:
    tk.Radiobutton(
        top,
        text=db_name,             # the label shown next to the radio circle
        variable=db_choice,       # the shared StringVar all buttons write to
        value=db_name,            # the value stored when this button is selected
        font=("Arial", 11)
    ).pack(side=tk.LEFT, padx=6)

# Load Data button
# command=load_data → call our load_data() function when clicked
# bg / fg → background colour / foreground (text) colour
tk.Button(
    top, text="  Load Data  ",
    font=("Arial", 11, "bold"),
    bg="#2563EB", fg="white",     # blue button, white text
    padx=10, pady=4,
    command=load_data             # function to run on click
).pack(side=tk.LEFT, padx=20)


# ── Grid (Treeview) ───────────────────────────────────────────
# Define the column header names. The order here must match
# the order of values= in tree.insert() inside load_data()
columns = ("ID", "First Name", "Last Name", "Salary", "City", "Country")

# A Frame to hold the Treeview and both scrollbars as a group
# fill=tk.BOTH → stretch in both horizontal and vertical directions
# expand=True  → take up all remaining space in the window
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=4)

# Vertical scrollbar — scrolls the grid up and down
# pack(side=tk.RIGHT) → attaches it to the right edge of the frame
# fill=tk.Y           → stretches it the full height of the frame
scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

# Horizontal scrollbar — scrolls the grid left and right
# pack(side=tk.BOTTOM) → attaches it to the bottom edge of the frame
# fill=tk.X            → stretches it the full width of the frame
scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

# ttk.Treeview is tkinter's built-in table/grid widget
# columns=columns     → define which columns exist
# show="headings"     → hide the default tree icon column, show only our columns
# yscrollcommand      → link the grid to the vertical scrollbar
# xscrollcommand      → link the grid to the horizontal scrollbar
tree = ttk.Treeview(
    frame,
    columns=columns,
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set,
)

# Connect scrollbars back to the grid
# When the grid scrolls, the scrollbar thumb moves — and vice versa
scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)
tree.pack(fill=tk.BOTH, expand=True)

# Set the header label and pixel width for each column
col_widths = {
    "ID"        : 50,    # short — just a number
    "First Name": 110,
    "Last Name" : 130,
    "Salary"    : 100,
    "City"      : 140,
    "Country"   : 120,
}
for col in columns:
    tree.heading(col, text=col)                                    # set header text
    tree.column(col, width=col_widths[col], anchor=tk.CENTER)     # width + centre-align

# Define alternating row colours using named tags
# "odd"  → light blue background  (applied to even-index rows 0, 2, 4...)
# "even" → white background        (applied to odd-index rows 1, 3, 5...)
# Tags are assigned in load_data() using the 'tag=' argument of tree.insert()
tree.tag_configure("odd",  background="#EFF6FF")   # light blue
tree.tag_configure("even", background="#FFFFFF")   # white


# ── Status bar ────────────────────────────────────────────────
# tk.StringVar automatically updates any widget linked to it
# when .set() is called — no need to manually refresh the label
status = tk.StringVar(value="Select a database and click Load Data")

# textvariable=status → this label reads its text from the StringVar
# anchor=tk.W         → align text to the left edge (West)
# fg="grey"           → grey text colour for a subtle appearance
tk.Label(
    root, textvariable=status,
    anchor=tk.W, font=("Arial", 9), fg="grey"
).pack(fill=tk.X, padx=10, pady=6)


# ── Start the application ─────────────────────────────────────
# root.mainloop() starts the tkinter event loop.
# It keeps the window open and continuously listens for user
# actions (button clicks, window resize, typing, closing).
# The program stays here until the user closes the window.
root.mainloop()
