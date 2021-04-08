import tkinter as tk
import Register
import PatientMenu
import AdminMenu

def loginScreen ():

    def loginValidate ():
        # only accept username and password 
        # username: admin and password: admin for admin menu
        # username: patient1 and password: patient1 for patient menu

        username = uName.get()
        password = passwordBox.get()

        if (username == 'admin' and password == 'admin'):
            # go to admin menu 
            AdminMenu.adminMenuScreen (root)
        elif (username == 'patient1' and password == 'patient1'):
            # go to patient menu
            PatientMenu.patientMenuScreen (root)

    root = tk.Tk()

    frame = tk.Frame (root, padx=20, pady=20, bg="lightblue")
    frame.grid (row=0, column=0, sticky='news')

    intro = tk.Label (frame, text="Welcome to Appointment Booking and Reports Management System", wraplength=800)
    uNameLabel = tk.Label (frame, text="Username")
    passLabel = tk.Label (frame, text="Password")
    uName = tk.Entry(frame, width=20)
    passwordBox = tk.Entry(frame, width=20)
    login = tk.Button(frame, text='Log In', command=loginValidate)
    register = tk.Button(frame, text='Register', command=lambda: Register.registerScreen(root))

    intro.grid (row=0, column=0, columnspan=2)
    uNameLabel.grid (row=1, column=0)
    passLabel.grid (row=2, column=0)
    uName.grid (row=1, column=1)
    passwordBox.grid (row=2, column=1)
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
    loginScreen ()