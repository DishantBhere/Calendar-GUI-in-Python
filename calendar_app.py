from tkinter import *
import calendar

def show_calendar():
    try:
        year = int(year_entry.get())
        cal_output.delete('1.0', END)
        cal_output.insert(END, calendar.calendar(year))
    except ValueError:
        cal_output.delete('1.0', END)
        cal_output.insert(END, "Enter a valid year!")

root = Tk()
root.title("📅 Calendar Viewer")
root.geometry("750x700")
root.configure(bg="#ffd800")

Label(root, text="📅 Calendar Viewer", font=("Helvetica", 20, "bold"),
      bg="#ffec05", fg="#0b0b0b").pack(pady=15)

Label(root, text="Enter Year:", font=("Helvetica", 14),
      bg="#0e0d0d", fg="#D8DEE9").pack()

year_entry = Entry(root, font=("Helvetica", 13), bg="#ff7c00", fg="#ffff00",
                   insertbackground="#0b0b0b", justify='center')
year_entry.pack(pady=10)

Button(root, text="Show Calendar", command=show_calendar,
       font=("Helvetica", 12, "bold"), bg="#0e0d0d", fg="white",
       activebackground="#5E81AC", padx=10, pady=5).pack(pady=10)

# Scrollable text area
frame = Frame(root)
frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

x_scroll = Scrollbar(frame, orient=HORIZONTAL)
y_scroll = Scrollbar(frame, orient=VERTICAL)

cal_output = Text(frame, wrap=NONE, font=("Consolas", 10),
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
"""
📅 Calendar Viewer App
Created by Dishant
Python 3.13 | June 2025
"""

