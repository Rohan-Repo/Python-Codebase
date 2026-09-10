import tkinter as tk
from tkinter import ttk   # ttk provides the Treeview widget used for table display
import pandas as pd       # pandas makes reading and handling CSV data simple

# ── Load CSV data with pd.read_csv() ────────────────────────────────────────────────
df = pd.read_csv("transactions.csv")  

# ── Build the window ─────────────────────────────────────────────
root = tk.Tk()                  # create the main application window
root.title("CSV Viewer")        # set the window's title bar text
root.geometry("800x400")        # set window size: width x height in pixels

# Treeview widget displays data in rows and columns, like a spreadsheet
# columns=list(df.columns) tells it to use the CSV's column names
# show="headings" hides the default empty first column
table = ttk.Treeview(root, columns=list(df.columns), show="headings")

# Set up each column's header text and width
for col in df.columns:
    table.heading(col, text=col)              # column header label
    table.column(col, width=100, anchor="center")  # column width and text alignment

# Insert each row of the DataFrame into the table
# itertuples(index=False) loops through rows as tuples, skipping the row index
for row in df.itertuples(index=False):
    table.insert("", "end", values=row)

# Make the table fill the whole window and resize with it
table.pack(fill="both", expand=True)

# Starts the GUI event loop — keeps the window open and responsive
root.mainloop()