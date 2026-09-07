import tkinter as tk               # tkinter is Python's built-in GUI library
from datetime import datetime       

def show_welcome():
    # Get whatever text the user typed into the entry box
    name = name_entry.get()

    # Get the current date/time and format it as a readable string
    now = datetime.now().strftime("%A, %B %d, %Y  %I:%M %p")

    # Update the label's text to show the welcome message + date/time
    result_label.config(text=f"Welcome, {name}!\n{now}")

# ── Build the window ─────────────────────────────────────────────
root = tk.Tk()                      # create the main application window
root.title("Welcome App")           # set the window's title bar text
root.geometry("350x180")            # set window size: width x height in pixels

# Label prompting the user to enter their name
tk.Label(root, text="Enter your name:").pack(pady=5)   # pady adds vertical spacing

# Entry box where the user types their name
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Button that runs show_welcome() when clicked
tk.Button(root, text="Submit", command=show_welcome).pack(pady=10)

# Label that will display the welcome message (starts empty, filled in later)
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

# Starts the GUI event loop — keeps the window open and responsive to clicks
root.mainloop()