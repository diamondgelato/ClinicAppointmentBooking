import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def Book_Appointment():
    #Connect to the database connectivity
    #Fix the Date for the dialog box- 2/4/21
    #Month needs to be edited

    def invoke():
        selection="You selected the Time "+str(var.get())
        label.config(text=selection)



    def getAppointment ():
        timeframe = tk.LabelFrame(root, padx=10, pady=10, text="Timings available for the date")
        timeframe.grid (row=2, column=0, sticky='news')
        #date="12/4/21"
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
        timeframe.columnconfigure(0, weight=1)
        timeframe.rowconfigure(0, weight=1)
        timeframe.rowconfigure(1, weight=1)
        timeframe.rowconfigure(2, weight=1)
        timeframe.rowconfigure(3, weight=1)
        timeframe.rowconfigure(4, weight=1)
        timeframe.rowconfigure(5, weight=1)
        timeframe.rowconfigure(6, weight=1)
        timeframe.rowconfigure(7, weight=2)

        submit = ttk.Button(timeframe, text='Submit', command=lambda:submission(var)) #, onClick=sub(date,time)
        submit.grid(row=7, column=0)
        #need to work on the message dialog box

    def submission(time):
        doc=clicked.get()
        pur=purpose_var.get()
        t=time.get()
        times=["10.30am", "11.00am","11.30am","12.00pm","12.30pm"]
        var1= "Date: "+date_selected +"\nTime: "+times[t]+"\nDoctor: "+doc+"\nPurpose: "+pur
        msg=tk.messagebox.askquestion("Are you sure?", var1 );
        # if(msg=="yes"):
        #sub()
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
    doctors = ["Dr. Mihir Pandya","Dr. Vani Kamani","Dr. Mugdha Kurkure"]

    purpose_var=tk.StringVar()
    clicked = tk.StringVar()
    date_var=tk.StringVar()
    # initial menu text
    clicked.set( "Dr. Mihir Pandya" )
    dropLabel=tk.Label(frame, text='Name of the Reference Doctor: ')
    drop = ttk.OptionMenu(frame, clicked , *doctors )
    Purpose = tk.Label(frame, text='Purpose of appointment: ')
    PurposeBox = ttk.Entry(frame, width=30, textvariable=purpose_var)


    dropLabel.grid(row=0,column=0)
    drop.grid(row=0, column=1)
    Purpose.grid(row=1, column=0)
    PurposeBox.grid(row=1, column=1)
    # What about the month?
    for d in range(len(days)):
        dayLabel = tk.Label (frame2, text=days[d], width=5)
        dayLabel.grid (row=3, column=d)

    r = 4           # row of the calendar
    c = 0           # column of the calendar
    val1=""
    for day in monthiter:
        # day = next(monthiter)
        if (day[3] == 0):
            r+=1 
            c = 0

        date_selected=str(day[2])+"/"+str(day[1])+"/"+str(day[0])
        dayButton = ttk.Button(frame2, text=day[2], width=5, command=getAppointment)
        dayButton.grid (row=r, column=c)
        c+=1

    root.rowconfigure (0, weight=1, minsize=300)
    root.columnconfigure (0, weight=1, minsize=500)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)

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

#Book_Appointment()
