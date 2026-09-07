import tkinter as tk
from datetime import datetime

def show_welcome():
    label.config(text=f"Welcome, {entry.get()}!\n{datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Submit", command=show_welcome).pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()