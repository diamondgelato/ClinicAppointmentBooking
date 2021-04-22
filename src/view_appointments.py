import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Book_Appointment

#Add the Calendar button
#Database connectivity
#Connect the Edit Button to the Edit appointments
#when connected the other program runs before this, should be reverse
def view():
    frame1 = tk.LabelFrame (root, padx=10, pady=10, bg="white", text='The Appointments scheduled for the day')
    frame1.grid(row=1, column=0, sticky='news')

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6), show='headings', height='3')
    view1.pack()

    view1.heading(1, text='Appointment ID')
    view1.heading(2, text='Name of the Doctor')
    view1.heading(3, text='Patient ID')
    view1.heading(4, text='Patient Name')
    view1.heading(5, text='Time')
    view1.heading(6, text='Purpose')

    edit = ttk.Button(frame1, text='Edit', command=Book_Appointment.Book_Appointment)
    edit.pack()


root=tk.Tk() #toplevel change
frame = tk.LabelFrame (root, padx=10, pady=10, bg="lightblue", text='Enter the Date to view the appointments')
frame.grid(row=0, column=0, sticky='news')

submit = ttk.Button(frame, text='Submit', command=view) #onClick=sub(date,time)
submit.grid(row=3, column=0, columnspan=2)

root.mainloop()
# delete()