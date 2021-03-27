import tkinter as tk
from tkinter import *
from tkinter import ttk


def view():
    root1 = Tk()
    frame1 = Frame(root1)
    frame1.pack(side=tk.LEFT, padx=20)

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5), show='headings', height='3')
    view1.pack()

    view1.heading(1, text='Appointment ID')
    view1.heading(2, text='Date')
    view1.heading(3, text='Time')
    view1.heading(4, text='Purpose')
    view1.heading(5, text='Status')

    root1.title('Appointment Data')
    root1.geometry('1300x1000')

    root1.mainloop()


def delete():
    root = tk.Tk()

    frame = tk.Frame(root, padx=20, pady=20, bg="lightblue")
    frame.grid(row=0, column=0, sticky='news')

    AppointmentIDLabel = tk.Label(frame, text='AppointmentID ')
    AppointmentIDBox = ttk.Entry(frame, width=30)
    AppointmentIDLabel.grid(row=1, column=0)
    AppointmentIDBox.grid(row=1, column=1)

    delete = tk.Button(frame, text='Delete')

    delete.grid(row=2, column=0, columnspan=2)

    root.rowconfigure(0, weight=1, minsize=200)
    root.columnconfigure(0, weight=1, minsize=300)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(0, weight=1)

    root.mainloop()

view()
# delete()