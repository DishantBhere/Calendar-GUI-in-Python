"""
Calendar Viewer App
Author: Dishant
Date: June 2025
"""

import tkinter as tk
from tkinter import ttk
import calendar


def show_calendar():
    """Display calendar for the entered year."""
    try:
        year = int(year_entry.get())
        cal_output.delete('1.0', tk.END)
        cal_output.insert(tk.END, calendar.calendar(year))
    except ValueError:
        cal_output.delete('1.0', tk.END)
        cal_output.insert(tk.END, "Enter a valid year!")


root = tk.Tk()
root.title("📅 Calendar Viewer")
root.geometry("750x700")
root.configure(bg="#ffd800")

tk.Label(root, text="📅 Calendar Viewer", font=("Helvetica", 20, "bold"),
         bg="#ffec05", fg="#0b0b0b").pack(pady=15)

tk.Label(root, text="Enter Year:", font=("Helvetica", 14),
         bg="#0e0d0d", fg="#D8DEE9").pack()

year_entry = tk.Entry(root, font=("Helvetica", 13), bg="#ff7c00", fg="#ffff00",
                      insertbackground="#0b0b0b", justify='center')
year_entry.pack(pady=10)

tk.Button(root, text="Show Calendar", command=show_calendar,
          font=("Helvetica", 12, "bold"), bg="#0e0d0d", fg="white",
          activebackground="#5E81AC", padx=10, pady=5).pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

x_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
y_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)

cal_output = tk.Text(frame, wrap=tk.NONE, font=("Consolas", 10),
                     bg="#ffb200", fg="black", width=80, height=20,
                     xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

x_scroll.config(command=cal_output.xview)
y_scroll.config(command=cal_output.yview)

cal_output.grid(row=0, column=0, sticky="nsew")
x_scroll.grid(row=1, column=0, sticky="ew")
y_scroll.grid(row=0, column=1, sticky="ns")

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

root.mainloop()
