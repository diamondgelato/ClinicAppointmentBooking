import tkinter as tk
from tkinter import *
from tkinter import ttk


def view():
    root1 = Tk()
    frame1 = Frame(root1)
    frame1.pack(side=tk.LEFT, padx=20)

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5), show='headings', height='3')
    view1.pack()
#    tree.column('size', width=100, anchor='center')
 #   tree.heading('size', text='Size')
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


def edit():
    import calendar
    import tkinter as tk
    from tkinter import ttk

    def getAppointment():
        timeframe = tk.Frame(edit, padx=10, pady=10, bg="lightblue")
        timeframe.grid(row=0, column=1, sticky='news')

    # Getting calendar related data
    # monday = 0
    firstday = calendar.weekday(2021, 4, 1)

    calobj = calendar.Calendar(firstweekday=firstday)
    calobj = calendar.Calendar()

    monthiter = calobj.itermonthdays4(2021, 4)
    monthiter1 = monthiter
    currentmonth = 4

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Building GUI
    edit = tk.Tk()

    frame = tk.LabelFrame(edit, padx=10, pady=10, bg="lightblue",
                          text='Update records')
    frame.grid(row=0, column=0, sticky='news')

    frame2 = tk.Frame(edit, padx=10, pady=10, bg="white")
    frame2.grid(row=5, column=0, sticky='news')

    PatientID = tk.Label(frame, text='PatientID ')
    PatientIDBox = tk.Entry(frame, width=30)
    Time = tk.Label(frame, text='Time ')
    TimeBox = tk.Entry(frame, width=30)
    Purpose = tk.Label(frame, text='Purpose of appointment ')
    PurposeBox = ttk.Entry(frame, width=30)

    PatientID.grid(row=0, column=0)
    PatientIDBox.grid(row=0, column=1)
    Time.grid(row=2, column=0)
    TimeBox.grid(row=2, column=1)
    Purpose.grid(row=1, column=0)
    PurposeBox.grid(row=1, column=1)

    for d in range(len(days)):
        dayLabel = tk.Label(frame2, text=days[d], width=5)
        dayLabel.grid(row=3, column=d)

    r = 4  # row of the calendar
    c = 0  # column of the calendar
    for day in monthiter:
        # day = next(monthiter)
        if (day[3] == 0):
            r += 1
            c = 0

        dayButton = ttk.Button(frame2, text=day[2], width=5, command=getAppointment())
        dayButton.grid(row=r, column=c)
        c += 1

    save = tk.Button(frame2, text='Save')
    save.grid(row=13, column=0, columnspan=7)

    edit.rowconfigure(0, weight=1, minsize=400)
    edit.columnconfigure(0, weight=1, minsize=600)

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    frame2.rowconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)
    frame2.rowconfigure(2, weight=1)
    frame2.rowconfigure(3, weight=1)
    frame2.rowconfigure(4, weight=1)
    frame2.rowconfigure(5, weight=1)
    frame2.rowconfigure(6, weight=1)
    frame2.rowconfigure(7, weight=1)
    frame2.rowconfigure(8, weight=1)
    frame2.rowconfigure(9, weight=1)
    frame2.rowconfigure(10, weight=1)
    frame2.rowconfigure(11, weight=1)
    frame2.rowconfigure(12, weight=1)

    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.columnconfigure(2, weight=1)
    frame2.columnconfigure(3, weight=1)
    frame2.columnconfigure(4, weight=1)
    frame2.columnconfigure(5, weight=1)
    frame2.columnconfigure(6, weight=1)

    edit.mainloop()


edit()
# view()
# delete()