import tkinter as tk
import Report_Upload
from button import HoverButton

"""
Admin Menu
edit appointments
view appointments
upload reports
view reports
set reminders
"""
def adminMenuScreen(root):
    # root = tk.Tk()
    newWind = tk.Toplevel(root, )

    frame = tk.Frame(newWind, padx=20, pady=20, bg="#2C3A57")
    frame.grid(row=0, column=0, sticky='news')

    intro = tk.Label(frame, text="Admin Menu", wraplength=800, font=("Verdana", 10), bg="#2C3A57", fg="red")
    viewapp = HoverButton(frame, text="View Appointments", activebackground='#00BE00', font=("Bahnschrift", 9))
    editapp = HoverButton(frame, text="Edit Appointments", activebackground='#00BE00', font=("Bahnschrift", 9))
    uploadreports = HoverButton(frame, text="Upload Reports", activebackground='#00BE00', font=("Bahnschrift", 9),
                             command=lambda: Report_Upload.reportUploadScreen(root))
    viewreports = HoverButton(frame, text="View Reports", activebackground='#00BE00', font=("Bahnschrift", 9))
    setreminder = HoverButton(frame, text="Set Reminder", activebackground='#00BE00', font=("Bahnschrift", 9))

    # viewapp = tk.Button (frame, text="View and Edit Appointments")
    # editapp = tk.Button (frame, text="Edit Appointments")
    # addreports = tk.Button (frame, text="Add and View Reports", command = lambda: Report_Upload.reportUploadScreen(root))

    intro.grid(row=0, column=0)
    viewapp.grid(row=1, column=0)
    # editapp.grid(row=2, column=0)
    uploadreports.grid(row=2, column=0)
    viewreports.grid(row=3, column=0)
    setreminder.grid(row=4, column=0)

    newWind.rowconfigure(0, weight=1, minsize=200)
    newWind.columnconfigure(0, weight=1, minsize=300)

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.columnconfigure(0, weight=1)

    # root.mainloop()
