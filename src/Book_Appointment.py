import calendar
import tkinter as tk
from tkinter import ttk
from button import HoverButton

#Remove PatientID and Phone Number
#Name of the doctor- dropdown menu
#Add a frame for the timings
#Free and delete timings- NOT scheduled for the db.connectivity

def bookAppointmentScreen (root):
    def getAppointment ():
        timeframe = tk.Frame(newWind, padx=10, pady=10, bg="lightgrey")
        timeframe.grid (row=0, column=1, sticky='news')

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
    # root = tk.Tk()
    newWind = tk.Toplevel (root, )

    frame = tk.LabelFrame (newWind, padx=10, pady=10, text='Please enter your details for booking the appointment',
                           font=("Verdana", 10), bg = "#2C3A57", fg = "red")
    frame.grid(row=0, column=0, sticky='news')

    frame2=tk.Frame (newWind, padx=10, pady=10, bg="#A3A3B1")
    frame2.grid(row=5, column=0, sticky='news')

    ID = tk.Label(frame, text='Patient ID: ',font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    IDBox = tk.Entry(frame, width=30,bg = "#A3A3B1")
    Phone = tk.Label(frame, text='Phone Number: ',font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    PhoneBox= tk.Entry(frame, width=30,bg = "#A3A3B1")
    Purpose = tk.Label(frame, text='Purpose of appointment: ',font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    PurposeBox = tk.Entry(frame, width=30,bg = "#A3A3B1")

    ID.grid(row=0, column=0)
    IDBox.grid(row=0, column=1)
    Phone.grid(row=1, column=0)
    PhoneBox.grid(row=1, column=1)
    Purpose.grid(row=2, column=0)
    PurposeBox.grid(row=2, column=1)

    for d in range(len(days)):
        dayLabel = tk.Label (frame2, text=days[d], width=5)
        dayLabel.grid (row=3, column=d)

    r = 4           # row of the calendar
    c = 0           # column of the calendar
    for day in monthiter:
        # day = next(monthiter)
        if (day[3] == 0):
            r+=1
            c = 0
        
        dayButton = HoverButton(frame2, text=day[2], width=5,activebackground='#00BE00', font=("Bahnschrift", 9),
                                command=getAppointment())
        dayButton.grid (row=r, column=c)
        c+=1

    submit = HoverButton(frame2, text='Submit', activebackground='#00BE00', font=("Bahnschrift", 9))
    submit.grid(row=13, column=0, columnspan=7)

    newWind.rowconfigure (0, weight=1, minsize=400)
    newWind.columnconfigure (0, weight=1, minsize=600)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)

    # frame.rowconfigure (6, weight=2)
    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)
    # frame.columnconfigure (2, weight=1)
    # frame.columnconfigure (3, weight=1)
    # frame.columnconfigure (4, weight=1)
    # frame.columnconfigure (5, weight=1)
    # frame.columnconfigure (6, weight=1)

    frame2.rowconfigure (0, weight=1)
    frame2.rowconfigure (1, weight=1)
    frame2.rowconfigure (2, weight=1)
    frame2.rowconfigure (3, weight=1)
    frame2.rowconfigure (4, weight=1)
    frame2.rowconfigure (5, weight=1)
    frame2.rowconfigure (6, weight=1)
    frame2.rowconfigure (7, weight=1)
    frame2.rowconfigure (8, weight=1)
    frame2.rowconfigure (9, weight=1)
    frame2.rowconfigure (10, weight=1)
    frame2.rowconfigure (11, weight=1)
    frame2.rowconfigure (12, weight=1)

    frame2.columnconfigure (0, weight=1)
    frame2.columnconfigure (1, weight=1)
    frame2.columnconfigure (2, weight=1)
    frame2.columnconfigure (3, weight=1)
    frame2.columnconfigure (4, weight=1)
    frame2.columnconfigure (5, weight=1)
    frame2.columnconfigure (6, weight=1)

    # root.mainloop()