import tkinter as tk
from tkinter import ttk
import calendar
import sqlite3 as sql
import datetime

import ProgramVar as pv

def editAppointment (root):
    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()

    appointmentInfo = []
    var=tk.IntVar()

    # gets all the appointments which have the given date and patient ID
    def fetchAppointment (date, id):
        # print (date)
        stringDate = '%' + str(date) + '%'
        # print (stringDate)
        
        query = "SELECT appointment.app_id, patient.patient_id, patient.first_name, patient.last_name, appointment.datetime, appointment.purpose FROM scheduled_app as sa INNER JOIN appointment ON appointment.app_id = sa.app_id INNER JOIN patient ON patient.patient_id = sa.patient_id WHERE appointment.datetime LIKE ? AND patient.patient_id = ?;"
        cur.execute (query, (stringDate, id, ))

        result = cur.fetchall()
        # print (result)

        listy = [0, 1, 2, 4, 5]
        appointmentInfo = []

        for row in result:
            newrow = []
            for x in listy:
                if x == 2:
                    newrow.append (str(row[2] + ' ' + row[3]))
                else:
                    newrow.append (row[x])

            appointmentInfo.append(newrow)
        
        # print (appointmentInfo)
        
        # send back only date and time (separated into separate strings)
        appointments = [tuple([x[0], x[3].split(' ')]) for x in appointmentInfo]

        print (appointments)
        return appointments

        conn.commit ()



    def fetchAppointmentByDate (date):
        stringDate = '%' + str(date) + '%'

        query = "SELECT appointment.app_id, appointment.datetime, appointment.status FROM appointment WHERE appointment.datetime LIKE ?;"

        cur.execute (query, (stringDate, ))

        result = cur.fetchall()
        print (result)

    # fetchAppointmentByDate (datetime.date.fromisoformat('2021-05-04'))



    def fetchAppointmentByPatient (id):
        query = "SELECT patient.patient_id, appointment.app_id, appointment.datetime, appointment.purpose FROM scheduled_app as sa INNER JOIN appointment ON appointment.app_id = sa.app_id INNER JOIN patient ON patient.patient_id = sa.patient_id WHERE patient.patient_id = ?;"
        
        cur.execute (query, (id, ))

        result = cur.fetchall()

        appointments = [tuple(x[2].split(' ')) for x in result]
        return appointments

    # fetchAppointmentByDate (1)
    # fetchAppointment (datetime.date.fromisoformat('2021-05-04'), 1)
    


    # updates the given appointment ID to the datetime given by newdatetime 
    def updateAppointment (app_id, newdatetime):
        query = 'UPDATE appointment SET datetime = ? WHERE app_id = ?'
        stringDate = str(newdatetime)

        cur.execute (query, (stringDate, app_id))
        result = cur.fetchall ()
        print (result)
        print ('Record updated to date time', stringDate)

        conn.commit ()



    def getBlockedAppointment (date):
        # database connection: get all scheduled appointments for the day
        # date = date.split(',')[0]
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
        alltimes = ['10:30:00', '11:00:00', '11:30:00', '12:00:00', '12:30:00']

        for t in alltimes:
            flag = 0

            for l in times:
                if t in l[0]: 
                    flag = 1

            if flag == 0:
                times.append ((t, counter, "free"))
                counter+=1

        times.sort (key = lambda x: x[0])
        # print (times)
        return times



    #Scrolling option 
    def getlist():
        # Need to display all the timings and dates of the appointments which have been taken by the patient

        # dbconnection needed.
        # Show it on the GUI
        appointmentstaken=tk.LabelFrame(window, padx=10, pady=10, bg="#2C3A57", fg="red", font=("Verdana", 10), text='Appointments of the Patient')
        appointmentstaken.grid(row=1, column=0, sticky='news')

        id = int(PatientIDBox.get())

        # db connectivity (use def fetchAppointmentByPatient)
        appointments = fetchAppointmentByPatient(id)
        # appointments=[("16/4/21", "10.30am"), ("12/4/21", "11.30am")] 

        r,r1=0,0
        for date, time in appointments:
            datelabel=tk.Label(appointmentstaken, text=date, fg="white", bg="#2C3A57")
            datelabel.grid(row=r, column=0)
            timelabel=tk.Label(appointmentstaken, text=time, fg="white", bg="#2C3A57")
            timelabel.grid(row=r1, column=1)
            r+=1
            r1+=1



    def ShowAppointment(date):
        timeframe = tk.LabelFrame(window, padx=10, font=("Verdana", 10), text="Timings available for the date")
        timeframe.grid (row=3, column=0, sticky='news')
        # pt_id=patient_var.get()

        # use def fetchAppointmentByDate
        print (date)
        times = getBlockedAppointment (date.isoformat())
        # print(times)

        # times=[("10.30am", 0, "free", 0), ("11.00am", 1, "scheduled", 21032051),("11.30am",2, "scheduled", 21032053),("12.00pm",3,"free", 0),("12.30pm",4, "scheduled", 21032052) ]
        
        i, index=0,0
        for time, val, state in times:

            if(state=="scheduled"): 
                r=ttk.Radiobutton(timeframe, text=time, variable=var, width=20, padding=20, value=val, state= "disabled" )
                r.grid(row=i, column=0)
                present=val
            else: 
                r=ttk.Radiobutton(timeframe, text=time, variable=var, width=20, padding=20, value=val, command=lambda: print(var.get()), state= "normal")
                status=ttk.Label(timeframe, text=state)
                r.grid(row=i, column=0)
                status.grid(row=i, column=1)
                if(state=="scheduled"):
                    current=val
                    index=i
                
                

            i+=1
        save = ttk.Button(timeframe, text='Save', command=lambda: submission(times[var.get() - 1][0], date))
        save.grid(row=13, column=0, columnspan=7)



    # time - string, date - datetime object
    def submission(newtime, date):
        #db connectivity
        print ('in submission')
        print (date, newtime)
        id = PatientIDBox.get()

        appointment = fetchAppointment(date, id)
        print (appointment)

        # update value of datetime only if there has been a change in it
        if (appointment[0][1] != newtime):
            print ("different time")
            # then Add a alert dialog box
            conf = False
            msg = tk.messagebox.askquestion ("Confirm", "Confirm changes to appointment?")

            if msg == 'yes':
                # after dialog box confirmation
                stringDate = date.isoformat() + ' ' + newtime
                updateAppointment (appointment[0][0], stringDate)
                # print (appointment[0][0], stringDate)
                
                # update into appointments value of datetime (so stupid to add a new entry, I wonder who would do that)
                
                window.destroy()
            else:
                pass
        else:
            print ("same time")
            

        # Getting calendar related data
        # monday = 0
    


    # creates widgets for the calendar
    def cal(year, month):
        firstday = calendar.weekday(year, month, 1)

        calobj = calendar.Calendar(firstweekday=firstday)
        calobj = calendar.Calendar()

        monthiter = calobj.itermonthdays4(year, month) 
        monthiter1 = monthiter
        currentmonth = month

        # Prints weekday names 
        for d in range(len(days)):
            dayLabel = tk.Label (frame2, text=days[d], width=5)
            dayLabel.grid (row=3, column=d)

        r = 4           # row of the calendar
        c = 0           # column of the calendar
        val1=""

        # Number Buttons in Calendar
        for day in monthiter:
            # day = next(monthiter)
            if (day[3] == 0):
                r+=1 
                c = 0

            # app=str(day[2])+"/"+str(day[1])+"/"+str(day[0])+","+days[day[3]]
            app = datetime.date(day[0], day[1], day[2])
            # print(app)
            dayButton = ttk.Button(frame2, text=day[2], width=5, command=lambda app= app:ShowAppointment(app)) 
            dayButton.grid (row=r, column=c)
            c+=1
        
        # Previous and Next Button
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
    present=0;

    # Building GUI
    # root = tk.Tk()
    window=tk.Toplevel(root)
    window.title("Edit Appointments")

    patient_var=tk.IntVar()
        #Frame to enter the Patient ID whose appointment needs to be edited
    frame = tk.LabelFrame(window, bg="#2C3A57", fg="white", text='Update appointments')
    frame.grid(row=0, column=0, sticky='news') #frame 1

    PatientID = tk.Label(frame, text='PatientID', bg="#2C3A57", fg="white")
    PatientIDBox = tk.Entry(frame, width=10, textvariable= patient_var)

    PatientID.grid(row=0, column=0)
    PatientIDBox.grid(row=0, column=1)

    ShowappBox=ttk.Button(frame, text='View the appointments', command=getlist)
    ShowappBox.grid(row=1, column=0, columnspan=2)

    #appointmenttaken frame 2
    frame2 = tk.Frame(window, padx=10, pady=10, bg="white")
    frame2.grid(row=2, column=0, sticky='news') #frame 3
    #timeframe frame 4

    year=2021
    month=4
    cal(2021, 4)

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    # frame.rowconfigure(2, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    # frame.columnconfigure(2, weight=1)

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

    # root.title('Edit Appointments')
    # root.geometry("600x750+10+20")
    # root.mainloop()

    # conn.commit()
    # conn.close()

    # view()
    # delete()
