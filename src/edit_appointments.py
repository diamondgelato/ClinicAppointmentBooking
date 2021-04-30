import tkinter as tk
from tkinter import ttk
import calendar


# def view():
#     root1 = Tk()
#     frame1 = Frame(root1)
#     frame1.pack(side=tk.LEFT, padx=20)
#     view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5), show='headings', height='3')
#     view1.pack()
#     tree.column('size', width=100, anchor='center')
#     tree.heading('size', text='Size')
#     view1.heading(1, text='Appointment ID')
#     view1.heading(2, text='Date')
#     view1.heading(3, text='Time')
#     view1.heading(4, text='Purpose')
#     view1.heading(5, text='Status')
#     root1.title('Appointment Data')
#     root1.geometry('1300x1000')
#     root1.mainloop()

# def delete():
#     root = tk.Tk()

#     frame = tk.Frame(root, padx=20, pady=20, bg="lightblue")
#     frame.grid(row=0, column=0, sticky='news')

#     AppointmentIDLabel = tk.Label(frame, text='AppointmentID ')
#     AppointmentIDBox = ttk.Entry(frame, width=30)
#     AppointmentIDLabel.grid(row=1, column=0)
#     AppointmentIDBox.grid(row=1, column=1)

#     delete = tk.Button(frame, text='Delete')

#     delete.grid(row=2, column=0, columnspan=2)

#     root.rowconfigure(0, weight=1, minsize=200)
#     root.columnconfigure(0, weight=1, minsize=300)
#     frame.rowconfigure(1, weight=1)
#     frame.columnconfigure(0, weight=1)

#     root.mainloop()


# def edit():
#     import calendar
#     import tkinter as tk
#     from tkinter import ttk
from src.button import HoverButton


def getlist():
    #Need to display all the timings and dates of the appointments which are left.
    #dbconnection needed.
    #Show it on the GUI
    appointmentstaken=tk.LabelFrame(root, padx=10, pady=10, bg="cyan", text='Appointments of the Patient')
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
        
def ShowAppointment():
    timeframe = tk.LabelFrame(root, padx=10, text="Timings available for the date")
    timeframe.grid (row=3, column=0, sticky='news')
    pt_id=patient_var.get()
    var=tk.IntVar()
    patient_var.set(0)
    times=[("10.30am", 0, "free", 0), ("11.00am", 1, "scheduled", 21032051),("11.30am",2, "scheduled", 21032053),("12.00pm",3,"free", 0),("12.30pm",4, "scheduled", 21032052) ]
    i, index=0,0;
    for time, val, state, p_id in times:

        if(state=="scheduled" and pt_id!=p_id ): 
            r=ttk.Radiobutton(timeframe, text=time, variable=var, width=20, padding=20, value=val, state= "disabled" )
            r.grid(row=i, column=0)
        else: 
            r=ttk.Radiobutton(timeframe, text=time, variable=var, width=20, padding=20, value=val, command=lambda: print(var.get()), state= "normal")
            status=ttk.Label(timeframe, text=state )
            r.grid(row=i, column=0)
            status.grid(row=i, column=1)
            if(state=="scheduled"):
                current=val
                index=i
            
            

        i+=1
    save = ttk.Button(timeframe, text='Save', command=submission)
    save.grid(row=13, column=0, columnspan=7)

def submission():
    #db connectivity
    if(r!=val):
        num=var.get()
        times[index]=(time, val, "free", 0)
        times[num]=(time, val, "scheduled", p_id)
        #Add a information dialog box
        
                



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
patient_var=tk.IntVar()
    #Frame to enter the Patient ID whose appointment needs to be edited
frame = tk.LabelFrame(root, bg="#2C3A57",text='Update records')
frame.grid(row=0, column=0, sticky='news') #frame 1
PatientID = tk.Label(frame, text='PatientID ', font=("Verdana", 10), bg="#2C3A57", fg="red")
PatientIDBox = tk.Entry(frame, width=30, textvariable= patient_var, bg = "#A3A3B1")
PatientID.grid(row=0, column=0)
PatientIDBox.grid(row=0, column=1)
# PatientID.pack()
# PatientIDBox.pack()
ShowappBox=HoverButton(frame, text='View the appointments', command=getlist)

ShowappBox.grid(row=0, column=2, columnspan=2)
#appointmenttaken frame 2
frame2 = tk.Frame(root, padx=10, pady=10, bg="white")
frame2.grid(row=2, column=0, sticky='news') #frame 3
#timeframe frame 4


for d in range(len(days)):
    dayLabel = tk.Label(frame2, text=days[d], width=5, font=("Verdana", 10), bg="#2C3A57", fg="red")
    dayLabel.grid(row=3, column=d)

r = 4  # row of the calendar
c = 0  # column of the calendar
for day in monthiter:
        # day = next(monthiter)
    if (day[3] == 0):
        r += 1
        c = 0

    dayButton = tk.Button(frame2, text=day[2], width=5, command=ShowAppointment)
    dayButton.grid(row=r, column=c)
    c += 1

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

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

root.title('Edit Appointments')
root.geometry("400x500+10+20")
root.mainloop()


# view()
# delete()