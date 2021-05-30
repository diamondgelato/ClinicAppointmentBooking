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

def PatientReportScreen (root, id):
    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()
    def fileopen(path):
        print(path)
        os.startfile(path)


    def view_patient():
        
        print("Hey1")
        try:
            query = 'SELECT report.report_id, report.date, doctor.first_name, doctor.last_name, report.name, report.file FROM report JOIN patient_report ON report.report_id = patient_report.report_id JOIN patient ON patient.patient_id = patient_report.patient_id JOIN doctor ON doctor.doctor_id= patient_report.doctor_id WHERE patient_report.patient_id = ?;'
            
            print("Hey2")
            cur.execute (query,(id, ))
            result = cur.fetchall()
            print (result)
            conn.commit()

        except Exception as e:
            print(e)

        # view1.column(1, width=70)
        
        # count=0
        # for record in result:
        #     name=record[2]+" "+record[3]
        #     view1.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], name, record[4]), )
        #     count+=1
        
        # blank=tk.Label(sideframe, text='', background="#2C3A57")
        # blank.grid(row=0,column=0)
        
        # count=1
        # for rec in result:
        #     action=HoverButton(sideframe, text="View", width='10', command=lambda rec=rec:fileopen(rec[5]), activebackground='#00BE00', font=("Bahnschrift", 9))
        #     action.grid(row=count, column=0)
        #     count+=1
        #The loop here- for printing the rows and patient ID   
        total_rows = len(result)
        total_columns = len(result[0])-1
        print(total_rows)
        print(total_columns)


        for i in range(total_rows):
            name=result[i][2]+" "+result[i][3]
            for j in range(total_columns):
                print("i: "+str(i))
                print("j: "+str(j))
                if (j == 0):
                    t = result [i][j]
                elif j == 1:
                    t=result[i][j]
                elif j==4:
                    t=result[i][j]
                elif j==2:
                    t=name 
                else:
                    continue

                if(j==4):
                    col=j-1
                else:
                    col=j

                e = tk.Label(frame1, text=str(t), width=15, foreground='white', background="#2C3A57")
                e.grid(row=i+1, column=col)
        

                    
        count=1
        for rec in result:
            action=HoverButton(sideframe, text="View", width='10', command=lambda rec=rec:fileopen(rec[5]), activebackground='#00BE00', font=("Bahnschrift", 9))
            action.grid(row=count, column=0)
            count+=1        

   # root=tk.Tk() #toplevel change
    window=tk.Toplevel(root)
    

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(1, weight=1)
    window.geometry("800x400") #for presentation, might have to change the configuration
    
    frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="#2C3A57", text='View the Reports', foreground="red", font=("Verdana", 10))
    frame1.grid(row=0, column=0, sticky='wnse')
    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=1)
    frame1.columnconfigure(2, weight=1)
    frame1.columnconfigure(3, weight=1)
    frame1.columnconfigure(4, weight=1)

    reportId=tk.Label(frame1, text='Report Id', width=15, foreground='white', background="#2C3A57")
    reportId.grid(row=0,column=0)
    datet=tk.Label(frame1, text='Date', width=15, foreground='white', background="#2C3A57")
    datet.grid(row=0,column=1)
    doc=tk.Label(frame1, text='Doctor Name', width=15, foreground='white', background="#2C3A57")
    doc.grid(row=0,column=2)
    reportname=tk.Label(frame1, text='Report Name', width=15, foreground='white', background="#2C3A57")
    reportname.grid(row=0,column=3)


    # total_rows = len(result)
    # total_columns = len(result[0])-1

    # for i in range(total_rows):
    #     for j in range(total_columns):
    #         if (j == 0):
    #             id = result [i][j]
    #         elif j == 5:
    #             # skip column with photo
    #             pass
    #         else:
    #             if j == 4:
    #                 wid = 30
    #             else:
    #                 wid = 15

    #             e = tk.Label(topFrame, text=str(result[i][j]), width=wid)
    #             e.grid(row=i, column=j-1)

    #             if j == total_columns-1:
    #                     action = ttk.Button(topFrame, text='View', width=10, command=lambda id=id: viewContactCard(id))
    #                     print (id)
    #                     action.grid(row=i, column=j)
   
    # view1 = ttk.Treeview(window, columns=(1, 2, 3, 4), show='headings', height='5')
    # view1.grid(row=0,column=0,sticky='news')
    # view1.column(1, width=100)
    # view1.column(2, width=100)
    # view1.column(3, width=100)
    # view1.column(4, width=100)
    # ttk.Style().configure(view1, rowheight=500)
    
    

    # view1.heading(1, text='Report ID')
    # view1.heading(2, text='Date')
    # view1.heading(3, text='Doctor Name')
    # view1.heading(4, text='Name of the Report')



    sideframe=tk.Frame(window, padx=10, pady=10, bg="#2C3A57")
    sideframe.grid(row=0, column=1, sticky='ensw')
    sideframe.columnconfigure(0, weight=0)
    view_patient()
    

    # window.mainloop()
    # delete()

# root=tk.Tk()
# PatientReportScreen(root, 1)
# root.mainloop()
