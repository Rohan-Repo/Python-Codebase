# Simple Digital Clock using Tkinter

import tkinter as tk  # GUI library
import time           # Used to get the current system time

# Create the main application window.
root = tk.Tk()
root.title("Digital Clock!")


# Create a label that displays the current time.
label = tk.Label(
    root,
    font=("Arial", 50),
    bg="black",
    fg="aquamarine"
)

# padx and pady add horizontal and vertical spacing around the clock display
label.pack(padx=20, pady=20)


def update_time():
    # Format the current time as hours:minutes:seconds.
    label.config(text=time.strftime("%H:%M:%S"))

    # Run this function again after 1,000 milliseconds (1 second).
    label.after(1000, update_time)


# Start updating the clock.
update_time()

# Keep the window open and responsive.
root.mainloop()