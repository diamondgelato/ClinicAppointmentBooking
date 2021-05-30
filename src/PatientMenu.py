import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
from button import HoverButton

import ProgramVar as pv
import Book_Appointment
import PatientReportView

def patientMenuScreen (root, id):
    # root = tk.Tk()

    def logout ():
        root.deiconify()
        newWind.withdraw()

    print (id)

    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()

    query = "SELECT * FROM patient WHERE patient_id = ?"
    cur.execute (query, (id, ))
    result = cur.fetchall()
    nameString = 'Patient Name: ' + result[0][1] + ' ' + result[0][2]

    conn.commit()
    conn.close()
    nameString=result[0][1]+" "+result[0][2]
    newWind = tk.Toplevel(root, )

    frame = tk.Frame (newWind, padx=20, pady=20, bg="#2C3A57")
    frame.grid(row=0, column=0, sticky='news')

    patientname = tk.Label (frame, text=nameString, wraplength=800, font=("Verdana", 10), bg = "#2C3A57", fg = "red")
    intro = tk.Label (frame, text="Patient Menu", wraplength=800, font=("Verdana", 10), bg = "#2C3A57", fg = "red")
    bookapp = HoverButton (frame, text="Book Appointments", width=20, activebackground='#00BE00',
                           font=("Bahnschrift", 9), command=lambda: Book_Appointment.Book_Appointment(root, id))
    viewreports = HoverButton (frame, text="View Reports",activebackground='#00BE00', font=("Bahnschrift", 9),
                               width=20, command=lambda: PatientReportView.PatientReportScreen (root, id))
    logout = HoverButton (frame, text="Log Out",activebackground='#00BE00', font=("Bahnschrift", 9),
                               width=20, command=logout)

    patientname.grid(row=0, column=0)
    intro.grid(row=1, column=0)
    bookapp.grid(row=2, column=0)
    viewreports.grid(row=3, column=0)
    logout.grid(row=4, column=0)

    newWind.rowconfigure (0, weight=1, minsize=600)
    newWind.columnconfigure (0, weight=1, minsize=800)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.rowconfigure (4, weight=1)
    frame.columnconfigure (0, weight=1)

    # root.mainloop()