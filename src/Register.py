from datetime import date
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
from button import HoverButton

import ProgramVar as pv
import PatientMenu
# have to add DOB, gender, password confirmation and address

def registerScreen (root):
    # root = tk.Tk()

    genderVar = tk.StringVar()

    def submitCallback ():
        conn = sql.connect(pv.databasePath)
        cur = conn.cursor()

        # IMPORTANT: The date is being stored in the databse in YYYY-MM-DD format (I don't know how to change it)

        fname = fnameBox.get()
        lname = lnameBox.get()
        uname = unameBox.get()
        password = passBox.get()
        confPassword = confBox.get()
        phone = phoneBox.get()
        email = emailBox.get()
        gender = genderVar.get()
        address = addrBox.get()
        dob = dobselect.get_date()

        # check if any field is empty or date has not been changed (except phone, email, address)
        if (not fname) or (not lname) or (not uname) or (not password) or (not gender) or (date.today() == dob):
            print ("Something is empty :(")
        else:
            if (password == confPassword):
                # Add the entries ka data into the db
                query = "INSERT INTO patient (first_name, last_name, username, password, phone_no, email, birth_date, gender, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                params = (fname, lname, uname, password, phone, email, dob, gender, address)
                print (params)
                cur.execute (query, params)

                query = "SELECT patient_id FROM patient WHERE username = ?"
                cur.execute (query, (uname, ))
                result = cur.fetchall()

                if (len(result) > 0):
                    print (result)
                    print ("Data saved to db successfully")

        print (gender, type(dob))

        conn.commit ()
        conn.close ()

        # Open Patient Menu and close Register screen
        newWind.withdraw()
        PatientMenu.patientMenuScreen(root, result[0][0])

    def enterCallback(event):
        submitCallback()



    root.deiconify()
    newWind = tk.Toplevel(root, )
    newWind.bind('<Return>', enterCallback)



    frame = tk.LabelFrame(newWind, text='New Patient Registration', padx=10, pady=10, font=("Verdana", 10), bg="#2C3A57", fg = "red")
    frame.grid(row=0, column=0, sticky='news')
    radioFrame = tk.Frame (frame, padx=100, pady=10, bg="lightblue")



    fnameLabel = tk.Label(frame, text='First Name: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    fnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    lnameLabel = tk.Label(frame, text='Last Name: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    lnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    unameLabel = tk.Label(frame, text='Username: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    unameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    passLabel = tk.Label(frame, text='Password: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    passBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    
    confLabel = tk.Label(frame, text='Confirm Password: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    confBox = ttk.Entry(frame, width=30, bg="#A3A3B1")
    
    phoneLabel = tk.Label(frame, text='Phone Number: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    phoneBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    emailLabel = tk.Label(frame, text='E-mail: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    emailBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    submit = HoverButton(frame, text='Submit', activebackground='#00BE00', font=("Bahnschrift", 9))
    
    addrLabel = tk.Label(frame, text='Address: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    addrBox = ttk.Entry(frame, width=30, bg="#A3A3B1")
    
    dobLabel = tk.Label(frame, text='Select Date Of Birth: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    dobselect = tkc.DateEntry (frame)
    
    genderLabel = tk.Label(frame, text='Gender: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    maleRadio = ttk.Radiobutton (radioFrame, text='Male', variable=genderVar, value='MALE', bg="#A3A3B1")
    femaleRadio = ttk.Radiobutton (radioFrame, text='Female', variable=genderVar, value='FEMALE', bg="#A3A3B1")
    otherRadio = ttk.Radiobutton (radioFrame, text='Other', variable=genderVar, value='OTHER', bg="#A3A3B1")
    
    submit = tk.Button(frame, text='Submit', command=submitCallback)

    fnameLabel.grid(row=0, column=0)
    fnameBox.grid(row=0, column=1)
    lnameLabel.grid(row=1, column=0)
    lnameBox.grid(row=1, column=1)
    unameLabel.grid(row=2, column=0)
    unameBox.grid(row=2, column=1)
    passLabel.grid(row=3, column=0)
    passBox.grid(row=3, column=1)
    confLabel.grid(row=4, column=0)
    confBox.grid(row=4, column=1)
    phoneLabel.grid(row=5, column=0)
    phoneBox.grid(row=5, column=1)
    emailLabel.grid(row=6, column=0)
    emailBox.grid(row=6, column=1)
    addrLabel.grid(row=7, column=0)
    addrBox.grid(row=7, column=1)
    dobLabel.grid(row=8, column=0)
    dobselect.grid(row=8, column=1)
    genderLabel.grid(row=9, column=0)
    radioFrame.grid(row=9, column=1, sticky='news')
    submit.grid(row=10, column=0, columnspan=2)

    maleRadio.grid(row=0, column=0, sticky='w')
    femaleRadio.grid(row=1, column=0, sticky='w')
    otherRadio.grid(row=2, column=0, sticky='w')

    newWind.rowconfigure (0, weight=1, minsize=1600)
    newWind.columnconfigure (0, weight=1, minsize=1200)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.rowconfigure (4, weight=1)
    frame.rowconfigure (5, weight=1)
    frame.rowconfigure (6, weight=1)
    frame.rowconfigure (7, weight=1)
    frame.rowconfigure (8, weight=1)
    frame.rowconfigure (9, weight=1)
    frame.rowconfigure (10, weight=2)
    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)

    radioFrame.rowconfigure (0, weight=1)
    radioFrame.rowconfigure (1, weight=1)
    radioFrame.rowconfigure (2, weight=1)
    radioFrame.columnconfigure (0, weight=1)

    # root.mainloop()

