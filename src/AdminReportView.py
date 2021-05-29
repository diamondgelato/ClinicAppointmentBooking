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

        frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="#2C3A57", text='View the Reports', foreground="red", font = ("Verdana", 10))
        frame1.grid(row=1, column=0, sticky='wnse')
        frame1.columnconfigure(0, weight=1)
        frame1.columnconfigure(1, weight=1)
        frame1.columnconfigure(2, weight=1)
        frame1.columnconfigure(3, weight=1)
        frame1.columnconfigure(4, weight=1)

        view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4), show='headings', height='5')
        view1.grid(row=0,column=0, sticky='ew')
        sideframe=tk.Frame(window, padx=10, pady=10, bg="#2C3A57")
        sideframe.grid(row=1, column=1, sticky='enws')
        sideframe.columnconfigure(0, weight=0)

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
        if len(result) > 0:
            for record in result:
                name=record[2]+" "+record[3]
                view1.insert('', index='end', iid=count, text="", values=(record[0], record[1], name, record[4]))
                count+=1
            
            blank=tk.Label(sideframe, text='',background="#2C3A57", fg = "white")
            blank.grid(row=0,column=0)
            count=1
            
            for rec in result:
                action=HoverButton(sideframe, text="View", width='10', command=lambda rec=rec:fileopen(rec[5]), activebackground='#00BE00', font=("Bahnschrift", 9))
                action.grid(row=count, column=0)
                count+=1
        else:
            print ("No records found")

        view1.column(1, width=400)
        view1.column(2, width=400)
        view1.column(3, width=400)
        view1.column(4, width=400)

            


    def view_patient():
        # query:
        # 'SELECT report.report_id, report.date, patient.first_name, patient.last_name, report.name, report.file
        # FROM report
        # JOIN patient_report ON report.report_id = patient_report.report_id
        # JOIN patient ON patient.patient_id = patient_report.patient_id
        # WHERE patient_report.patient_id = ?;'
        frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="#2C3A57", text='View the Reports', foreground="red", font = ("Verdana", 10))
        frame1.grid(row=1, column=0, sticky='wnse')
        frame1.columnconfigure(0, weight=1)
        frame1.columnconfigure(1, weight=1)
        frame1.columnconfigure(2, weight=1)
        frame1.columnconfigure(3, weight=1)
        frame1.columnconfigure(4, weight=1)

        view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4), show='headings', height='5')
        view1.grid(row=0,column=0, sticky='ew')
        
        sideframe=tk.Frame(window, padx=10, pady=10, bg="#2C3A57")
        sideframe.grid(row=1, column=1, sticky='wens')
        sideframe.columnconfigure(0, weight=0)

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

        view1.column(1, width=400)
        view1.column(2, width=400)
        view1.column(3, width=400)
        view1.column(4, width=400)
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
        
        blank=tk.Label(sideframe, text='', background="#2C3A57", fg = 'white')
        blank.grid(row=0,column=0)
        
        count=1
        for rec in result:
            action=HoverButton(sideframe, text="View", width='10', command=lambda rec=rec:fileopen(rec[5]), activebackground='#00BE00', font=("Bahnschrift", 9))
            action.grid(row=count, column=0)
            count+=1

        #add the loop here- for printing the rows and patient ID


    # root=tk.Tk() #toplevel change
    window=tk.Toplevel(root)
    frame = tk.LabelFrame (window, padx=10, pady=10, bg="#2C3A57", text='Enter the details to view reports', foreground="red", font = ("Verdana", 10))
    frame.grid(row=0, column=0, sticky='news', columnspan=2)

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1) 

    pt_id=tk.IntVar()
    date_label=tk.Label(frame, text="Select the date: ", font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    date_select=tkc.DateEntry(frame)
    date_label.grid(row=0, column =0)
    date_select.grid(row=0, column=1)
    submit = HoverButton(frame, text='View', command=view_date, activebackground='#00BE00', font=("Bahnschrift", 9)) #onClick=sub(date,time)
    submit.grid(row=0, column=2)

    id_label=tk.Label(frame, text="Enter the Patient ID: ", font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    id_select=tk.Entry(frame, width=30, textvariable=pt_id, bg = "#A3A3B1")
    id_label.grid(row=1, column =0)
    id_select.grid(row=1, column=1)
    submit = HoverButton(frame, text='View Patient\'s Reports', command=view_patient, activebackground='#00BE00', font=("Bahnschrift", 9)) #onClick=sub(date,time)
    submit.grid(row=1, column=2)

    # window.mainloop()
    # delete()



# root=tk.Tk()
# AdminReportScreen(root)
# root.mainloop()
