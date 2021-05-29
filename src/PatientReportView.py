# Python program to create
# a file explorer in Tkinter
# import all components
# from the tkinter library

import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
# import filedialog module
from tkinter import filedialog
import tkcalendar as tkc
from button import HoverButton
#db connectivity
import sqlite3 as sql
import os

import ProgramVar as pv
#View Buttons code

def PatientReportScreen (root, id):
    conn = sql.connect (pv.databasePath)
    cur = conn.cursor ()
    def fileopen(path):
        print(path)
        os.startfile(path)

    # gets information for reports from the database
    def fetchReportsDB():        
        # query:
        # 'SELECT report.report_id, report.date, patient.first_name, patient.last_name, report.name, report.file
        # FROM report
        # JOIN patient_report ON report.report_id = patient_report.report_id
        # JOIN patient ON patient.patient_id = patient_report.patient_id
        # WHERE patient_report.patient_id = ?;'
        
        print("Hey1")
        result = 0
        try:
            query = 'SELECT report.report_id, report.date, patient.first_name, patient.last_name, report.name, report.file FROM report JOIN patient_report ON report.report_id = patient_report.report_id JOIN patient ON patient.patient_id = patient_report.patient_id WHERE patient_report.patient_id = ?;'
            # patient_id = int(id_select.get())
            # print (id)

            cur.execute (query, (id,))
            result = cur.fetchall()

            print (result)

            conn.commit()
        except Exception as e:
            print(e)

        count=0
        for record in result:
            name=record[2]+" "+record[3]
            view1.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], name, record[4]))
            count+=1
        
        blank=tk.Label(sideframe, text='', background="#2C3A57")
        blank.grid(row=0,column=0)
        
        count=1
        for rec in result:
            action=HoverButton(sideframe, text="View", width='10', command=lambda rec=rec:fileopen(rec[5]), activebackground='#00BE00', font=("Bahnschrift", 9))
            action.grid(row=count, column=0)
            count+=1

    # opens the selected report  
    def openReport ():
        pass

    # root=tk.Tk() #toplevel change
    window=tk.Toplevel(root)
    # frame = tk.LabelFrame (window, padx=10, pady=10, bg="lightblue", text='Enter the details to view reports')
    # frame.grid(row=0, column=0, sticky='news')
    frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="#2C3A57", text='View the Reports', foreground="red", font=("Verdana", 10))
    frame1.grid(row=0, column=0, sticky='news')

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    # frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="#2C3A57", text='View the Reports', foreground="red", font=("Verdana", 10))
    # frame1.grid(row=1, column=0, sticky='wnse')

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4), show='headings', height='5')
    view1.heading(1, text='Report ID')
    view1.heading(2, text='Date')
    view1.heading(3, text='Patient Name')
    view1.heading(4, text='Name of the Report')

    view1.column(1, width=400)
    view1.column(2, width=400)
    view1.column(3, width=400)
    view1.column(4, width=400)

    sideframe=tk.Frame(window, padx=10, pady=10, bg="#2C3A57")
    sideframe.grid(row=0, column=1, sticky='ensw')
    sideframe.columnconfigure(0, weight=0)

    fetchReportsDB()

    view1.grid(row=0,column=0, sticky='ewns')

    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=1)
    frame1.columnconfigure(2, weight=1)
    frame1.columnconfigure(3, weight=1)
    frame1.columnconfigure(4, weight=1)

    pt_id=tk.IntVar()

    conn.commit ()
    conn.close ()
