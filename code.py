"""A simple digital clock with a green background."""

from datetime import datetime
import tkinter as tk


BACKGROUND = "#2e8b57"


def update_clock() -> None:
    time_label.config(text=datetime.now().strftime("%I:%M:%S %p"))
    date_label.config(text=datetime.now().strftime("%A, %B %d, %Y"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Green Digital Clock")
root.configure(bg=BACKGROUND)
root.geometry("500x220")
root.resizable(False, False)

time_label = tk.Label(
    root,
    font=("Arial", 48, "bold"),
    bg=BACKGROUND,
    fg="white",
)
time_label.pack(expand=True, pady=(20, 0))

date_label = tk.Label(
    root,
    font=("Arial", 16),
    bg=BACKGROUND,
    fg="white",
)
date_label.pack(pady=(0, 25))

update_clock()
root.mainloop()
