import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import tkcalendar as tkc
import sqlite3 as sql
import edit_appointments
import ProgramVar as pv
from button import HoverButton

#Add the Calendar button
#Database connectivity
#Connect the Edit Button to the Edit appointments
#when connected the other program runs before this, should be reverse
def ViewAppointmentAdmin(root, id):
    conn = sql.connect(pv.databasePath)
    cur = conn.cursor ()

    def fetchAppointment (date):
        # print (date)
        stringDate = str(date)
        # print (stringDate)
        
        query = "SELECT appointment.app_id, doctor.first_name, doctor.last_name, patient.patient_id, patient.first_name, patient.last_name, appointment.datetime, appointment.purpose FROM scheduled_app as sa INNER JOIN appointment ON appointment.app_id = sa.app_id INNER JOIN patient ON patient.patient_id = sa.patient_id INNER JOIN doctor ON doctor.doctor_id = sa.doctor_id WHERE appointment.datetime LIKE ?;"
        cur.execute (query, ('%' + stringDate + '%', ))

        result = cur.fetchall()
        # print (result)

        listy = [0, 1, 3, 4, 6, 7]

        newrow = []

        for row in result:
            for x in listy:
                if x == 1:
                    newrow.append (str(row[1] + ' ' + row[2]))
                elif x == 4:
                    newrow.append (str(row[4] + ' ' + row[5]))
                else:
                    newrow.append (row[x])
        
        # print (newrow)
        # return newrow

        view1.insert ('', 'end', values=newrow)
        conn.commit()


    def view():
        frame1.grid(row=1, column=0, sticky='news')
        view1.pack()

        # edit = ttk.Button(frame1, text='Edit', command=edit_appointments)
        # edit.pack()

        dateVar = date.get_date()
        fetchAppointment(dateVar)


    window=tk.Toplevel() #toplevel change
    frame = tk.LabelFrame (window, padx=10, pady=10, bg="#2c3a57", text='Enter the Date to view the appointments', fg = "red", font = ("Verdana", 10))
    frame.grid(row=0, column=0, sticky='news')

    date=tkc.DateEntry(window)
    date.grid(row=0, column=0)
    #Date entry
    submit = HoverButton(frame, text='Submit', command=view, activebackground='#00BE00', font=("Bahnschrift", 9)) #onClick=sub(date,time)
    submit.grid(row=3, column=0, columnspan=2)

    frame1 = tk.LabelFrame (window, padx=10, pady=10, text='The Appointments scheduled for the day', bg="#2c3a57", fg = "red", font = ("Verdana", 9))

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6), show='headings', height='3')

    view1.heading(1, text='Appointment ID')
    view1.heading(2, text='Name of the Doctor')
    view1.heading(3, text='Patient ID')
    view1.heading(4, text='Patient Name')
    view1.heading(5, text='Time')
    view1.heading(6, text='Purpose')

    view1.column (1, width=200)
    view1.column (2, width=300)
    view1.column (3, width=200)
    view1.column (4, width=300)
    view1.column (5, width=300)
    view1.column (6, width=200)

    window.rowconfigure(0, weight=1, minsize=500)
    window.columnconfigure(0, weight=1, minsize=1200)

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    window.mainloop()
    # delete()

    conn.commit()
    conn.close ()

# ViewAppointmentAdmin (tk.Tk())