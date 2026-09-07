import tkinter as tk
from datetime import datetime

def show_welcome():
    name = name_entry.get()
    now = datetime.now().strftime("%A, %B %d, %Y  %I:%M %p")
    result_label.config(text=f"Welcome, {name}!\n{now}")

# ── Build the window ─────────────────────────────────────────────
root = tk.Tk()
root.title("Welcome App")
root.geometry("350x180")

tk.Label(root, text="Enter your name:").pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Button(root, text="Submit", command=show_welcome).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()