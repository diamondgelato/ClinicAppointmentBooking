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
import sqlite3 as sql
import os

import ProgramVar as pv
#db connectivity
#View Buttons code

def AdminReportScreen (root):
    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()
    def fileopen(path):
        print(path)
        os.startfile(path)


    def view_date():
        # query = 'SELECT report.report_id, patient_report.patient_id, patient.first_name, patient.last_name, report.name, report.file
        #          FROM report
        #          JOIN patient_report ON report.report_id = patient_report.report_id
        #          JOIN patient ON patient.patient_id = patient_report.patient_id
        #          WHERE report.date = ?;'

        try:
            query = 'SELECT report.report_id, patient_report.patient_id, patient.first_name, patient.last_name, report.name, report.file FROM report JOIN patient_report ON report.report_id = patient_report.report_id JOIN patient ON patient.patient_id = patient_report.patient_id WHERE report.date = ?;'
            date = date_select.get_date().isoformat()
            # print (date)
            cur.execute (query, (date,))
            result = cur.fetchall()
            print (result)
            conn.commit()
        except Exception as e:
            print(e)

        view1.heading(1, text='Report ID')
        view1.heading(2, text='Patient ID')
        view1.heading(3, text='Patient Name')
        view1.heading(4, text='Name of the Report')
        # view1.heading(5, text='Click here to view')

        #Add the loop here! for the date entry and printing the result
        count=0
        for record in result:
            name=record[2]+" "+record[3]
            view1.insert(frame1, index='end', iid=count, text="", values=(record[0], record[1], name, record[4]))
            count+=1
        
        count=0
        for rec in result:
            
            action=tk.Button(sideframe, text="View", width='15', command=lambda rec:fileopen(rec[5]))
            action.grid(row=count, column=0)
            count+=1


            


    def view_patient():
        # query:
        # 'SELECT report.report_id, report.date, patient.first_name, patient.last_name, report.name, report.file
        # FROM report
        # JOIN patient_report ON report.report_id = patient_report.report_id
        # JOIN patient ON patient.patient_id = patient_report.patient_id
        # WHERE patient_report.patient_id = ?;'

        try:
            query = 'SELECT report.report_id, report.date, patient.first_name, patient.last_name, report.name, report.file FROM report JOIN patient_report ON report.report_id = patient_report.report_id JOIN patient ON patient.patient_id = patient_report.patient_id WHERE patient_report.patient_id = ?;'
            patient_id = int(id_select.get())
            print (patient_id)

            cur.execute (query, (patient_id,))
            result = cur.fetchall()

            print (result)

            conn.commit()
        except Exception as e:
            print(e)
        view1.column(1, width=15)
        view1.heading(1, text='Report ID')
        view1.heading(2, text='Date')
        view1.heading(3, text='Patient Name')
        view1.heading(4, text='Name of the Report')
        # view1.heading(5, text='Click here to view')
        count=0
        for record in result:
            name=record[2]+" "+record[3]
            view1.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], name, record[4]))
            count+=1
        
        count=0
        for rec in result:
            action=tk.Button(sideframe, text="View", width='15', command=lambda:fileopen(rec[5]))
            action.grid(row=count, column=0)
            count+=1

        #add the loop here- for printing the rows and patient ID


    # root=tk.Tk() #toplevel change
    window=tk.Toplevel(root)
    frame = tk.LabelFrame (window, padx=10, pady=10, bg="lightblue", text='Enter the details to view reports')
    frame.grid(row=0, column=0, sticky='news', columnspan=2)
    frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="white", text='View the Reports')
    frame1.grid(row=1, column=0, sticky='wns')
    sideframe=tk.Frame(window, padx=10, pady=10, bg="blue")
    sideframe.grid(row=1, column=1, sticky='ens')

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=1)
    frame1.columnconfigure(2, weight=1)
    frame1.columnconfigure(3, weight=1)
    frame1.columnconfigure(4, weight=1)

    sideframe.columnconfigure(0, weight=0)

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4), show='headings', height='3')
    view1.grid(row=0,column=0, sticky='ew')

    pt_id=tk.IntVar()
    date_label=tk.Label(frame, text="Select the date: ")
    date_select=tkc.DateEntry(frame)
    date_label.grid(row=0, column =0)
    date_select.grid(row=0, column=1)
    submit = ttk.Button(frame, text='View', command=view_date) #onClick=sub(date,time)
    submit.grid(row=0, column=2)

    id_label=tk.Label(frame, text="Enter the Patient ID: ")
    id_select=tk.Entry(frame, width=30, textvariable=pt_id )
    id_label.grid(row=1, column =0)
    id_select.grid(row=1, column=1)
    submit = ttk.Button(frame, text='View Patient\'s Reports', command=view_patient) #onClick=sub(date,time)
    submit.grid(row=1, column=2)

    # window.mainloop()
    # delete()



root=tk.Tk()
AdminReportScreen(root)
root.mainloop()
