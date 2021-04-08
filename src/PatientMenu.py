import tkinter as tk
from tkinter import ttk
import Book_Appointment
import PatientReportView

def patientMenuScreen (root):
    # root = tk.Tk()
    newWind = tk.Toplevel(root, )

    frame = tk.Frame (newWind, padx=20, pady=20)
    frame.grid(row=0, column=0, sticky='news')

    intro = tk.Label (frame, text="Patient Menu", wraplength=800)
    bookapp = ttk.Button (frame, text="Book Appointments", width=20, command=lambda: Book_Appointment.bookAppointmentScreen(root))
    viewreports = ttk.Button (frame, text="View Reports", width=20, command=lambda: PatientReportView.reportViewScreen (root))

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