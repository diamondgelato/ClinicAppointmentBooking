import tkinter as tk
from tkinter import ttk
from button import HoverButton


# have to add DOB, gender, password confirmation and address

def registerScreen(root):
    # root = tk.Tk()
    newWind = tk.Toplevel(root, )

    frame = tk.LabelFrame(newWind, text='New Patient Registration', padx=10, pady=10, font=("Verdana", 10), bg="#2C3A57", fg = "red")
    frame.grid(row=0, column=0, sticky='news')

    # I don't know why but ttk.Entry doesn't support bg attribute, tk.Entry supports it so i have changed it

    fnameLabel = tk.Label(frame, text='First Name: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    fnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    lnameLabel = tk.Label(frame, text='Last Name: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    lnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    unameLabel = tk.Label(frame, text='Username: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    unameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    passLabel = tk.Label(frame, text='Password: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    passBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    phoneLabel = tk.Label(frame, text='Phone Number: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    phoneBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    emailLabel = tk.Label(frame, text='E-mail: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
    emailBox = tk.Entry(frame, width=30, bg="#A3A3B1")
    submit = HoverButton(frame, text='Submit', activebackground='#00BE00', font=("Bahnschrift", 9))

    fnameLabel.grid(row=0, column=0)
    fnameBox.grid(row=0, column=1)
    lnameLabel.grid(row=1, column=0)
    lnameBox.grid(row=1, column=1)
    unameLabel.grid(row=2, column=0)
    unameBox.grid(row=2, column=1)
    passLabel.grid(row=3, column=0)
    passBox.grid(row=3, column=1)
    phoneLabel.grid(row=4, column=0)
    phoneBox.grid(row=4, column=1)
    emailLabel.grid(row=5, column=0)
    emailBox.grid(row=5, column=1)
    submit.grid(row=6, column=0, columnspan=2)

    newWind.rowconfigure(0, weight=1, minsize=500)
    newWind.columnconfigure(0, weight=1, minsize=700)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)
    frame.rowconfigure(5, weight=1)
    frame.rowconfigure(6, weight=2)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # root.mainloop()
