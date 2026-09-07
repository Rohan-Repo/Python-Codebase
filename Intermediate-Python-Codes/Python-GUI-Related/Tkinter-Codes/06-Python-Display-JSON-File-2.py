import tkinter as tk
import json   # built-in library used to read .json files into Python objects

# ── Load JSON data ────────────────────────────────────────────────
# json.load() reads the file and converts it into a Python list of
# dictionaries — one dictionary per user, matching the JSON structure
with open("users.json") as f:
    users = json.load(f)

# ── Build the window ─────────────────────────────────────────────
root = tk.Tk()                  # create the main application window
root.title("User Viewer")       # set the window's title bar text

# Loop through each user (each item in the list is one dictionary)
for user in users:
    # Build a multi-line text block for this user
    # user['contactDetails']['emailAddress'] reaches into the nested
    # object, and ', '.join(user['hobbies']) turns the hobbies list
    # into a single comma-separated string
    text = (
        f"{user['firstName']} {user['lastName']}  (Age: {user['age']})\n"
        f"Email: {user['contactDetails']['emailAddress']}\n"
        f"Phone: {user['contactDetails']['phoneNumber']}\n"
        f"Hobbies: {', '.join(user['hobbies'])}\n"
    )

    # Create a bordered label for this user and add it to the window
    # justify="left" keeps text left-aligned, relief="groove" draws a border,
    # fill="x" makes each label stretch across the window width
    tk.Label(root, text=text, justify="left", anchor="w", padx=10, pady=10,
             relief="groove", borderwidth=1).pack(fill="x", padx=10, pady=5)

# Starts the GUI event loop — keeps the window open and responsive
root.mainloop()