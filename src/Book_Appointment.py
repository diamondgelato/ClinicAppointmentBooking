import calendar
import tkinter as tk
from tkinter import ttk
from button import HoverButton
from tkinter import messagebox
import sqlite3 as sql
import datetime

import ProgramVar as pv

def Book_Appointment(root, id):
    #Connect to the database connectivity
    #Month needs to be edited

    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()

    
    # adds data to the database
    def addAppointmentDB (doctor, purpose, date, time):
        date = date.split(',')[0]
        date = datetime.date.fromisoformat (date)
        time = time[:-2]
        time = datetime.time.fromisoformat (time)
        
        # add to appointment table
        dbtime = datetime.datetime.combine (date, time)
        params = (str(dbtime), purpose, 'scheduled')
        query = "INSERT INTO appointment (datetime, purpose, status) VALUES (?, ?, ?);"
        
        cur.execute (query, params)

        cur.execute ("SELECT * FROM appointment WHERE datetime = ?", (dbtime, ))
        result = cur.fetchall()
        print (result)

        # add to scheduled_app table
        params1 = (id, doctors[doctor], result[0][0])
        query1 = "INSERT INTO scheduled_app (patient_id, doctor_id, app_id) VALUES (?, ?, ?);"

        cur.execute (query1, params1)
        result1 = cur.fetchall ()
        print (result1)

        conn.commit()


    def getBlockedAppointment (date):
        # database connection: get all scheduled appointments for the day
        date = date.split(',')[0]
        query = 'SELECT datetime FROM appointment WHERE status = "scheduled"'
        cur.execute (query)
        allBlocked = cur.fetchall()
        times = []
        counter = 0

        # add all the times that are blocked, to the times wala list
        for app in allBlocked:
            # print (app[0], date)
            if date in app[0]:

                times.append ((app[0].split(' ')[1], counter, "scheduled"))
                counter+=1

        # add the rest of the times as free to times wala list
        alltimes = ['10:30', '11:00', '11:30', '12:00', '12:30']

        for t in alltimes:
            flag = 0

            for l in times:
                if t in l[0]: 
                    flag = 1

            if flag == 0:
                times.append ((t, counter, "free"))
                counter+=1

        # print (times)
        return times


    def getAppointment (date):
        timeframe = tk.LabelFrame(window, padx=10, pady=10, text="Timings available for the date")
        timeframe.grid (row=2, column=0, sticky='news')
        date_var=date
        var=tk.IntVar()

        times = getBlockedAppointment(date)

        # times=[("10:30am", 0, "free"), ("11:00am", 1, "scheduled"),("11:30am",2, "deleted"),("12:00pm",3,"free"),("12:30pm",4, "free") ]
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

        submit = ttk.Button(timeframe, text='Submit', command=lambda:submission(var,date_var)) #, onClick=sub(date,time)
        submit.grid(row=7, column=0)
        #need to work on the message dialog box


    def submission(time,date):
        if(purpose_var.get()!=""):
            doc=clicked.get()
            pur=purpose_var.get()
            t=time.get()
            date_selected=date
            times=["10:30am", "11:00am","11:30am","12:00pm","12:30pm"]
            var1= "Date: "+date_selected +"\nTime: "+times[t]+"\nDoctor: "+doc+"\nPurpose: "+pur
            msg=tk.messagebox.askquestion("Are you sure?", var1 );
            
            if(msg=="yes"):
                #connect to database
                addAppointmentDB (doc, pur, date_selected, times[t])
            else:
                # close the window
                pass
        else:
            var2="Please fill in the purpose"
            msg1=tk.messagebox.showerror("ERROR", var2)
    

    # Getting calendar related data
    # monday = 0
    def cal(year, month):
        firstday = calendar.weekday(year, month, 1)

        calobj = calendar.Calendar(firstweekday=firstday)
        calobj = calendar.Calendar()

        monthiter = calobj.itermonthdays4(year, month) 
        monthiter1 = monthiter
        currentmonth = month

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

            app=str(day[0])+"-"+str(day[1]).zfill(2)+"-"+str(day[2]).zfill(2)+","+days[day[3]]
            dayButton = ttk.Button(frame2, text=day[2], width=5, command=lambda app= app:getAppointment(app)) 
            dayButton.grid (row=r, column=c)
            c+=1
        if(month==1):
            prev=ttk.Button(frame2, text="Previous", width=10, command=lambda c= c:cal(year-1, 12)) 
            
        else:
            prev=ttk.Button(frame2, text="Previous", width=10, command=lambda c= c:cal(year, month-1) )
            
        if(month==12):
            nextm=ttk.Button(frame2, text="Next", width=10, command=lambda c= c:cal(year+1, 1))
        else:
            nextm=ttk.Button(frame2, text="Next", width=10, command=lambda c= c:cal(year, month+1))
        
        prev.grid(row=0, column=0)
        nextm.grid(row=0, column=6)
        yearnmonth1=tk.Label(frame2, text="Month: "+str(months[month-1]), width=10)
        yearnmonth1.grid(row=0, column=3)
        yearnmonth2=tk.Label(frame2, text="Year: "+str(year), width=10)
        yearnmonth2.grid(row=1, column=3)


    days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    months=['January', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December']

    # Building GUI
    window = tk.Toplevel(root)

    frame = tk.LabelFrame (window, padx=10, pady=10, text='Please enter your details for booking the appointment',
                          font=("Verdana", 10), bg = "#2C3A57", fg = "red")
    frame.grid(row=0, column=0, sticky='news')

    frame2=tk.Frame (window, padx=10, pady=10, bg="#A3A3B1")
    frame2.grid(row=1, column=0, sticky='news')
    # doctors = ["Dr. Mihir Pandya","Dr. Vani Kamani","Dr. Mugdha Kurkure"]

    purpose_var=tk.StringVar()
    clicked = tk.StringVar()
    
    # get doctor names with their ID from database
    query = "SELECT doctor_id, first_name, last_name FROM doctor"
    cur.execute (query)
    dbResult = cur.fetchall()
    doctors = {}

    for x in dbResult:
        docname = "Dr. " + x[1] + " " + x[2]
        doctors[docname] = x[0]
    
    doctornames = list(doctors.keys())

    # initial menu text
    clicked.set(doctornames[0])
    dropLabel=tk.Label(frame, text='Name of the Reference Doctor: ', font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    drop = ttk.OptionMenu(frame, clicked , *doctornames )
    Purpose = tk.Label(frame, text='Purpose of appointment: ', font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    PurposeBox = tk.Entry(frame, width=30, textvariable=purpose_var, bg = "#A3A3B1")


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
    # for day in monthiter:
    #     # day = next(monthiter)
    #     if (day[3] == 0):
    #         r+=1 
    #         c = 0

    #     date_selected=str(day[2])+"/"+str(day[1])+"/"+str(day[0])
    #     dayButton = HoverButton(frame2, text=day[2], width=5,activebackground='#00BE00', font=("Bahnschrift", 9),
    #                             command=getAppointment())
    #     dayButton.grid (row=r, column=c)
    #     c+=1

    cal (2021, 4)
        
    submit = HoverButton(frame2, text='Submit', activebackground='#00BE00', font=("Bahnschrift", 9))
    submit.grid(row=13, column=0, columnspan=7)

    window.rowconfigure (0, weight=1, minsize=300)
    window.columnconfigure (0, weight=1, minsize=500)

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
    frame2.rowconfigure (13, weight=1)

    frame2.columnconfigure (0, weight=1)
    frame2.columnconfigure (1, weight=1)
    frame2.columnconfigure (2, weight=1)
    frame2.columnconfigure (3, weight=1)
    frame2.columnconfigure (4, weight=1)
    frame2.columnconfigure (5, weight=1)
    frame2.columnconfigure (6, weight=1)

    window.mainloop()

    conn.commit()
    conn.close()

# Book_Appointment()
