import tkinter as tk

def login ():
    root = tk.Tk()

    frame = tk.Frame (root, padx=20, pady=20, bg="lightblue")
    frame.grid (row=0, column=0, sticky='news')

    intro = tk.Label (frame, text="Welcome to Appointment Booking and Reports Management System", wraplength=800)
    uNameLabel = tk.Label (frame, text="Username")
    passLabel = tk.Label (frame, text="Password")
    uName = tk.Entry(frame, width=20)
    password = tk.Entry(frame, width=20)
    login = tk.Button(frame, text='Log In')
    register = tk.Button(frame, text='Register')

    intro.grid (row=0, column=0, columnspan=2)
    uNameLabel.grid (row=1, column=0)
    passLabel.grid (row=2, column=0)
    uName.grid (row=1, column=1)
    password.grid (row=2, column=1)
    login.grid (row=3, column=0)
    register.grid (row=3, column=1)

    root.columnconfigure (0, weight=1, minsize=500)
    root.rowconfigure (0, weight=1, minsize=300)

    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)
    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    # frame.rowconfigure (4, weight=1)

    root.mainloop ()

if __name__ == '__main__':
    login ()