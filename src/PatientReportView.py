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

#db connectivity
#View Buttons code

def view_date():
    view1.heading(1, text='Report ID')
    view1.heading(2, text='Patient ID')
    view1.heading(3, text='Patient Name')
    view1.heading(4, text='Name of the Report')
    view1.heading(5, text='Click here to view')

def view_patient():

    view1.heading(1, text='Report ID')
    view1.heading(2, text='Date')
    view1.heading(3, text='Patient Name')
    view1.heading(4, text='Name of the Report')
    view1.heading(5, text='Click here to view')


root=tk.Tk() #toplevel change
window=tk.Toplevel(root)
frame = tk.LabelFrame (window, padx=10, pady=10, bg="lightblue", text='Enter the details to view reports')
frame.grid(row=0, column=0, sticky='news')
frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="white", text='View the Reports')
frame1.grid(row=1, column=0, sticky='news')

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5), show='headings', height='3')
view1.grid(row=0,column=0)

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

window.mainloop()
# delete()

