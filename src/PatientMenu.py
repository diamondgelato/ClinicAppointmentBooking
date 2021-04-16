import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
import Book_Appointment
import PatientReportView

def patientMenuScreen (root, id):
    # root = tk.Tk()

    print (id)

    conn = sql.connect(r'C:\Users\ashuk\Documents\Semester 4\Mini Project\ClinicAppointmentBooking\data.db')
    cur = conn.cursor()

    query = "SELECT * FROM patient WHERE patient_id = ?"
    cur.execute (query, (id, ))
    result = cur.fetchall()

    nameString = 'Patient Name: ' + result[0][1] + ' ' + result[0][2];

    conn.commit()
    conn.close()

    newWind = tk.Toplevel(root, )

    frame = tk.Frame (newWind, padx=20, pady=20)
    frame.grid(row=0, column=0, sticky='news')

    patientname = tk.Label (frame, text=nameString, wraplength=800)
    intro = tk.Label (frame, text="Patient Menu", wraplength=800)
    bookapp = ttk.Button (frame, text="Book Appointments", width=20, command=lambda: Book_Appointment.bookAppointmentScreen(root))
    viewreports = ttk.Button (frame, text="View Reports", width=20, command=lambda: PatientReportView.reportViewScreen (root))

    patientname.grid(row=0, column=0)
    intro.grid(row=1, column=0)
    bookapp.grid(row=2, column=0)
    viewreports.grid(row=3, column=0)

    newWind.rowconfigure (0, weight=1, minsize=600)
    newWind.columnconfigure (0, weight=1, minsize=800)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.columnconfigure (0, weight=1)

    # root.mainloop()