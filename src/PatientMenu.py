import tkinter as tk
from tkinter import ttk
import Book_Appointment
import PatientReportView
from button import HoverButton

def patientMenuScreen (root):
    # root = tk.Tk()
    newWind = tk.Toplevel(root, )

    frame = tk.Frame (newWind, padx=20, pady=20, bg="#2C3A57")
    frame.grid(row=0, column=0, sticky='news')

    intro = tk.Label (frame, text="Patient Menu", wraplength=800, font=("Verdana", 10), bg = "#2C3A57", fg = "red")
    #bookapp = ttk.Button (frame, text="Book Appointments", width=20, command=lambda: Book_Appointment.bookAppointmentScreen(root))
    #viewreports = ttk.Button (frame, text="View Reports", width=20, command=lambda: PatientReportView.reportViewScreen (root))
    bookapp = HoverButton (frame, text="Book Appointments", width=20, activebackground='#00BE00',
                           font=("Bahnschrift", 9), command=lambda: Book_Appointment.bookAppointmentScreen(root))
    viewreports = HoverButton (frame, text="View Reports",activebackground='#00BE00', font=("Bahnschrift", 9),
                               width=20, command=lambda: PatientReportView.reportViewScreen (root))

    intro.grid(row=0, column=0)
    bookapp.grid(row=1, column=0)
    viewreports.grid(row=2, column=0)

    newWind.rowconfigure (0, weight=1, minsize=600)
    newWind.columnconfigure (0, weight=1, minsize=800)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.columnconfigure (0, weight=1)

    # root.mainloop()