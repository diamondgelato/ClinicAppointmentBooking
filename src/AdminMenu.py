import tkinter as tk
import Report_Upload

def adminMenuScreen (root, id):
    # root = tk.Tk()
    print (id)
    newWind = tk.Toplevel (root, )

    frame = tk.Frame (newWind, padx=20, pady=20, bg="lightblue")
    frame.grid(row=0, column=0, sticky='news')

    intro = tk.Label (frame, text="Admin Menu", wraplength=800)
    viewapp = tk.Button (frame, text="View and Edit Appointments")
    # editapp = tk.Button (frame, text="Edit Appointments")
    addreports = tk.Button (frame, text="Add and View Reports", command = lambda: Report_Upload.reportUploadScreen(root))

    intro.grid(row=0, column=0)
    viewapp.grid(row=1, column=0)
    # editapp.grid(row=2, column=0)
    addreports.grid(row=2, column=0)

    newWind.rowconfigure (0, weight=1, minsize=200)
    newWind.columnconfigure (0, weight=1, minsize=300)

    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    # frame.rowconfigure (3, weight=1)
    frame.columnconfigure (0, weight=1)

    # root.mainloop()