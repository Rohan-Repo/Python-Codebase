import tkinter as tk
import json

# Load the JSON file
with open("users.json") as f:
    users = json.load(f)

root = tk.Tk()
root.title("User Viewer")

# Loop through each user and display their details
for user in users:
    text = (
        f"{user['firstName']} {user['lastName']}  (Age: {user['age']})\n"
        f"Email: {user['contactDetails']['emailAddress']}\n"
        f"Phone: {user['contactDetails']['phoneNumber']}\n"
        f"Hobbies: {', '.join(user['hobbies'])}\n"
    )
    tk.Label(root, text=text, justify="left", anchor="w", padx=10, pady=10,
             relief="groove", borderwidth=1).pack(fill="x", padx=10, pady=5)

root.mainloop()