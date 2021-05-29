# Python program to create
# a file explorer in Tkinter
# import all components
# from the tkinter library

#Doctor name dropdown menu

import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
from button import HoverButton
import sqlite3 as sql
# import filedialog module
from tkinter import filedialog
# for copying files
import shutil
import datetime as dt
import os

import ProgramVar as pv
  
filename = ''

def reportUploadScreen (root):
    # Function for opening the
    # file explorer window
    # window = tk.Tk()
    conn = sql.connect (pv.databasePath)
    cur = conn.cursor ()

    window = tk.Toplevel (root)
    frame = tk.LabelFrame(window, text='Please upload the reports in pdf format only.', padx=10, pady=10,
                          font=("Verdana", 10), bg="#2C3A57",  fg = "red")

    frame.grid(row=0, column=0, sticky='news')

    def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.pdf*"),
                                                        ("all files",
                                                            "*.*")))
        
        # Change label contents
        label_file_explorer.configure(text="File Opened: "+filename)
        button_submit = Button(frame,
                        text = "Submit", command=sub)
        button_submit.grid(column = 0,row = 5, columnspan=2)

    # Set window title
    def sub():
        if(repNameBox.get()!="" and patientIDBox.get()!=""):
            report=repNameBox.get()
            p_id=patientIDBox.get()
            # p_id=str(p_id)
            var1= "Patient ID: "+p_id +"\nName of the report: "+report
            msg=tk.messagebox.askquestion("Are you sure?", var1 )
            if(msg=="yes"):
                copyReportFile()
                addReports()
            #db connectivity
            
        else:
            var2="Please fill in the details"
            msg1=tk.messagebox.showerror("ERROR", var2)

    def copyReportFile ():
        # source folder
        global filename
        # source filename
        name = filename[filename.rfind('/')+1 : len(filename)]

        # destination folder
        newdir = pv.pdfPath
        # destination filename
        newfilename = repNameBox.get() + '.pdf'

        newpath = newdir + '\\' + newfilename

        shutil.copy2 ((filename), newdir)
        os.rename ((newdir+ '\\' +name), (newdir+ '\\' +newfilename))

    def addReports ():
        global filename 

        try:
            query = 'INSERT INTO report (date, name, file) VALUES (?, ?, ?);'
            newfilename = repNameBox.get() + '.pdf'
            newfilepath = pv.pdfPath + '\\' + newfilename
            date = str(dt.date.today())

            cur.execute (query, (date, newfilename, newfilepath))
            result = cur.fetchall ()
            print('Query 1 done')

            query1 = 'SELECT report_id FROM report WHERE name = ?'
            cur.execute (query1, (newfilename, ))

            result = cur.fetchone()
            print(result)
            print('Query 2 done')

            query2 = 'INSERT INTO patient_report (patient_id, doctor_id, report_id) VALUES (?, ?, ?);'
            patientID = (patientIDBox.get())
            print(patientID, type(patientID))
            doctorID = (doctorIDBox.get())
            print(doctorID, type(doctorID))
            reportID = result[0]

            cur.execute (query2, (patientID, doctorID, reportID))
            result = cur.fetchall()
            print('Query 3 done')

            print (date)
            print (filename)
            print (newfilepath)
            conn.commit ()
        except Exception as e:
            print(e)
            print("Error in database function")

            
    window.title('Uploading Reports')
        
    #Set window background color
    window.config(background = "white")
    patient_id_var=tk.IntVar()
    report_var=tk.StringVar()

    # Create a File Explorer label
    patientIDLabel = tk.Label(frame, text='Patient ID: ',font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    patientIDBox = tk.Entry(frame, width=30, bg = "#A3A3B1")
    doctorIDLabel = tk.Label(frame, text='Doctor ID: ',font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    doctorIDBox = tk.Entry(frame, width=30, bg = "#A3A3B1")
    dateLabel = tk.Label(frame, text='Date: ', font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    dateBox = tk.Entry(frame, width=30, bg = "#A3A3B1")
    repNameLabel = tk.Label(frame, text='Name of the Report: ', font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    repNameBox = tk.Entry(frame, width=30, bg = "#A3A3B1")

    label_file_explorer = Label(frame,
                                text = "Click on browse to upload the file here",
                                width = 100, height = 4,
                                fg = "black", justify= "center", bg="#A3A3B1",font=("Verdana", 9))
    
        
    button_explore = HoverButton(frame,
                            text = "Browse", font=("Bahnschrift", 9),activebackground='#00BE00',
                            command = browseFiles) #tkinter.dnd can be used.
    
    # button_submit = HoverButton(frame, activebackground='#00BE00', font=("Bahnschrift", 9),
    #                     text = "Submit")
    
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    patientIDLabel.grid(row=0, column=0)
    patientIDBox.grid(row=0, column=1)
    doctorIDLabel.grid(row=1, column=0)
    doctorIDBox.grid(row=1, column=1)
    repNameLabel.grid(row=2, column=0)
    repNameBox.grid(row=2, column=1)   
    label_file_explorer.grid(column = 0, row = 3, columnspan=2)
    button_explore.grid(column = 0, row = 4, columnspan=2)
    

    window.rowconfigure (0, weight=1, minsize=500)
    window.columnconfigure (0, weight=1, minsize=700)
    
    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.rowconfigure (4, weight=1)
    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)

    # Let the window wait for any events
    window.mainloop()

    conn.commit ()
    conn.close ()
# root=tk.Tk()
# reportUploadScreen(root)