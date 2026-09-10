import tkinter as tk
from tkinter import ttk
import pandas as pd

# ── Load CSV data ────────────────────────────────────────────────
df = pd.read_csv("transactions.csv")  

# ── Build the window ─────────────────────────────────────────────
root = tk.Tk()
root.title("CSV Viewer")
root.geometry("800x400")

# Table widget
table = ttk.Treeview(root, columns=list(df.columns), show="headings")

for col in df.columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor="center")

for row in df.itertuples(index=False):
    table.insert("", "end", values=row)

table.pack(fill="both", expand=True)

root.mainloop()