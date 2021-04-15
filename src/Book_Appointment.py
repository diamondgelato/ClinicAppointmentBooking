import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from tkinter import*

#Free and delete timings- NOT scheduled for the db.connectivity

#Need to figure out the message dialog box+ getting the date printed in the dialog box

def invoke():
    selection="You selected the Time "+str(var.get())
    label.config(text=selection)



def getAppointment ():
    timeframe = tk.LabelFrame(root, padx=10, pady=10, text="Timings available for the date")
    timeframe.grid (row=2, column=0, sticky='news')
    #date=str(value1)
    var=tk.IntVar()

    times=[("10.30am", 0, "free"), ("11.00am", 1, "scheduled"),("11.30am",2, "deleted"),("12.00pm",3,"free"),("12.30pm",4, "free") ]
    i=0
    for time, val, state in times:

        if(state=="scheduled"):
            r=r=tk.Radiobutton(timeframe, text=time, variable=var, width=20, padx=20, value=val, command=lambda: print(var.get()), state= "disabled" )
            r.grid(row=i, column=0)
        else: 
            r=tk.Radiobutton(timeframe, text=time, variable=var, width=20, padx=20, value=val, command=lambda: print(var.get()), state= "normal")
            r.grid(row=i, column=0)
            times[var.get()]=(time, val, "scheduled")
        
        i+=1
    timeframe.rowconfigure(7, weight=1)
    timeframe.columnconfigure(0, weight=1)
    timeframe.columnconfigure(1, weight=1)
    timeframe.columnconfigure(2, weight=1)
    timeframe.columnconfigure(3, weight=1)
    timeframe.columnconfigure(4, weight=1)
    timeframe.columnconfigure(5, weight=1)
    timeframe.columnconfigure(6, weight=1)

    submit = tk.Button(timeframe, text='Submit')#, onClick=sub(date,time)
    submit.grid(row=7, column=0)
    #need to work on the message dialog box

# def sub(value1, value):
#     var= "Date: "+value1 +"\nTime: "+value+"\nDoctor: "
#     msg=tk.messagebox.askquestion("Are you sure?", var );
#     # if(msg=="yes"):
#     #     sub()
        
#connect to database
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
root = tk.Tk()

frame = tk.LabelFrame (root, padx=10, pady=10, bg="lightblue", text='Please enter your details for booking the appointment')
frame.grid(row=0, column=0, sticky='news')

frame2=tk.Frame (root, padx=10, pady=10, bg="white")
frame2.grid(row=1, column=0, sticky='news')
doctors = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

# ID = tk.Label(frame, text='Patient ID: ')
# IDBox = ttk.Entry(frame, width=30)
# Phone = tk.Label(frame, text='Phone Number: ')
# PhoneBox= tk.Entry(frame, width=30)
clicked = tk.StringVar()
# initial menu text
clicked.set( "Monday" )
dropLabel=tk.Label(frame, text='Name of the Reference Doctor: ')
drop = ttk.OptionMenu(frame, clicked , *doctors )
Purpose = tk.Label(frame, text='Purpose of appointment: ')
PurposeBox = ttk.Entry(frame, width=30)

# ID.grid(row=0, column=0)
# IDBox.grid(row=0, column=1)
# Phone.grid(row=1, column=0)
# PhoneBox.grid(row=1, column=1)

dropLabel.grid(row=0,column=0)
drop.grid(row=0, column=1)
Purpose.grid(row=1, column=0)
PurposeBox.grid(row=1, column=1)

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
    
    dayButton = ttk.Button(frame2, text=day[2], width=5, command=getAppointment)
    dayButton.grid (row=r, column=c)
    c+=1



root.rowconfigure (0, weight=1, minsize=300)
root.columnconfigure (0, weight=1, minsize=500)

frame.rowconfigure (0, weight=1)
frame.rowconfigure (1, weight=1)
# frame.rowconfigure (2, weight=1)
# frame.rowconfigure (3, weight=1)

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

root.mainloop()