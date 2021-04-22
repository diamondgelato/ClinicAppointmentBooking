import calendar
import tkinter as tk
from tkinter import ttk

def getAppointment ():
    timeframe = tk.Frame(root, padx=10, pady=10)
    timeframe.grid (row=0, column=1, sticky='news')

    root.columnconfigure (1, weight=1, minsize=500)

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

frame = tk.Frame (root, padx=10, pady=10)
frame.grid(row=0, column=0, sticky='news')

for d in range(len(days)):
    dayLabel = tk.Label (frame, text=days[d], width=5)
    dayLabel.grid (row=0, column=d)

r = 0           # row of the calendar
c = 0           # column of the calendar
for day in monthiter:
    # day = next(monthiter)
    if (day[3] == 0):
        r+=1
        c = 0
    
    dayButton = ttk.Button(frame, text=day[2], width=5, command=getAppointment())
    dayButton.grid (row=r, column=c)
    c+=1

root.rowconfigure (0, weight=1, minsize=700)
root.columnconfigure (0, weight=1, minsize=900)

frame.rowconfigure (0, weight=1)
frame.rowconfigure (1, weight=1)
frame.rowconfigure (2, weight=1)
frame.rowconfigure (3, weight=1)
frame.rowconfigure (4, weight=1)
frame.rowconfigure (5, weight=1)
# frame.rowconfigure (6, weight=2)
frame.columnconfigure (0, weight=1)
frame.columnconfigure (1, weight=1)
frame.columnconfigure (2, weight=1)
frame.columnconfigure (3, weight=1)
frame.columnconfigure (4, weight=1)
frame.columnconfigure (5, weight=1)
frame.columnconfigure (6, weight=1)

root.mainloop()