import tkinter as tk
from tkinter import ttk
import calendar
import sqlite3 as sql
import datetime

import ProgramVar as pv

def editAppointment (root):
    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()

    # gets all the appointments which have the given date and patient ID
    def fetchAppointment (date, id):
        # print (date)
        stringDate = str(date)
        # print (stringDate)
        
        query = "SELECT appointment.app_id, doctor.first_name, doctor.last_name, patient.patient_id, patient.first_name, patient.last_name, appointment.datetime, appointment.purpose FROM scheduled_app as sa INNER JOIN appointment ON appointment.app_id = sa.app_id INNER JOIN patient ON patient.patient_id = sa.patient_id INNER JOIN doctor ON doctor.doctor_id = sa.doctor_id WHERE appointment.datetime LIKE ? AND patient.patient_id = ?;"
        cur.execute (query, ('%' + stringDate + '%', id, ))

        result = cur.fetchall()
        # print (result)

        listy = [0, 1, 3, 4, 6, 7]

        for row in result:
            newrow = []
            for x in listy:
                if x == 1:
                    newrow.append (str(row[1] + ' ' + row[2]))
                elif x == 4:
                    newrow.append (str(row[4] + ' ' + row[5]))
                else:
                    newrow.append (row[x])
        
        print (newrow)
        return newrow

        conn.commit ()

    # fetchAppointment (datetime.date.fromisoformat('2021-05-04'), 1)
    
    # updates the given appointment ID to the datetime given by newdatetime 
    def updateAppoinment (app_id, newdatetime):
        query = 'UPDATE appointment SET datetime = ? WHERE app_id = ?'
        stringDate = str(newdatetime)

        cur.execute (query, (stringDate, app_id))
        result = cur.fetchall ()
        print (result)
        print ('Record updated to date time', stringDate)

        conn.commit ()

    #Scrolling option 
    def getlist():
        #Need to display all the timings and dates of the appointments which are left.
        #dbconnection needed.
        #Show it on the GUI
        appointmentstaken=tk.LabelFrame(window, padx=10, pady=10, bg="cyan", text='Appointments of the Patient')
        appointmentstaken.grid(row=1, column=0, sticky='news')
        appointments=[("16/4/21", "10.30am"), ("12/4/21", "11.30am")] #db connectivity

        r,r1=0,0
        for date, time in appointments:
            datelabel=tk.Label(appointmentstaken, text=date)
            datelabel.grid(row=r, column=0)
            timelabel=tk.Label(appointmentstaken, text=time)
            timelabel.grid(row=r1, column=1)
            r+=1
            r1+=1
            
    def ShowAppointment(date):
        timeframe = tk.LabelFrame(window, padx=10, text="Timings available for the date")
        timeframe.grid (row=3, column=0, sticky='news')
        pt_id=patient_var.get()
        date_var=date
        var=tk.IntVar()
        patient_var.set(0)

        # get all appointments where date = (given date)

        times=[("10.30am", 0, "free", 0), ("11.00am", 1, "scheduled", 21032051),("11.30am",2, "scheduled", 21032053),("12.00pm",3,"free", 0),("12.30pm",4, "scheduled", 21032052) ]
        i, index=0,0
        for time, val, state, p_id in times:

            if(state=="scheduled" and pt_id!=p_id ): 
                r=ttk.Radiobutton(timeframe, text=time, variable=var, width=20, padding=20, value=val, state= "disabled" )
                r.grid(row=i, column=0)
                present=val;
            else: 
                r=ttk.Radiobutton(timeframe, text=time, variable=var, width=20, padding=20, value=val, command=lambda: print(var.get()), state= "normal")
                status=ttk.Label(timeframe, text=state )
                r.grid(row=i, column=0)
                status.grid(row=i, column=1)
                if(state=="scheduled"):
                    current=val
                    index=i
                
                

            i+=1
        save = ttk.Button(timeframe, text='Save', command=lambda: submission(var, date_var))
        save.grid(row=13, column=0, columnspan=7)

    def submission(time,date):
        #db connectivity
        print ('in submission')

        if(r!=val):
            num=var.get()
            times[index]=(time, val, "free", 0)
            times[num]=(time, val, "scheduled", p_id)
            #Add a information dialog box

            # after dialog box confirmation
            # insert into appointments values (given datetime, previous purpose, 'scheduled')
            # get id of above entry
            # insert into scheduled_app values (given patient id, doctor id from prev appointment (see how you gonna find that), current appointment id)
            

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

            app=str(day[2])+"/"+str(day[1])+"/"+str(day[0])+","+days[day[3]]
            dayButton = ttk.Button(frame2, text=day[2], width=5, command=lambda app= app:ShowAppointment(app)) 
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
    present=0;

    # Building GUI
    # root = tk.Tk()
    window=tk.Toplevel(root)
    window.title("Edit Appointments")
    # canvas = tk.Canvas(window, borderwidth=0, background="#ffffff")
    # scroll_bar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    # canvas.configure(yscrollcommand=scroll_bar.set)
    # scroll_bar.pack( side = RIGHT, fill = Y )
    # canvas.pack(side="left",fill="both", expand=True)
    # canvas.create_window((4,4), window=frame, anchor="nw")

    patient_var=tk.IntVar()
        #Frame to enter the Patient ID whose appointment needs to be edited
    frame = tk.LabelFrame(window, bg="light blue",text='Update appointments')
    frame.grid(row=0, column=0, sticky='news') #frame 1

    # canvas=tk.Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
    # vbar=tk.Scrollbar(frame,orient='vertical')
    # vbar.grid(row=0, column=0, sticky='E', rowspan=3, columnspan=3)
    # vbar.config(command=canvas.yview)
    # canvas.config(width=300,height=300)
    # canvas.config( yscrollcommand=vbar.set)
    # canvas.grid(row=0, column=0, sticky='E' , rowspan=3, columnspan=3)





    PatientID = tk.Label(frame, text='PatientID ')
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

    # for d in range(len(days)):
    #     dayLabel = ttk.Label(frame2, text=days[d], width=5)
    #     dayLabel.grid(row=3, column=d)

    # r = 4  # row of the calendar
    # c = 0  # column of the calendar
    # for day in monthiter:
    #         # day = next(monthiter)
    #     if (day[3] == 0):
    #         r += 1
    #         c = 0

    #     dayButton = ttk.Button(frame2, text=day[2], width=5, command=ShowAppointment)
    #     dayButton.grid(row=r, column=c)
    #     c += 1



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

    conn.commit()
    conn.close()

    # view()
    # delete()