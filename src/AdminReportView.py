# Python program to create
# a file explorer in Tkinter
# import all components
# from the tkinter library

import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
# import filedialog module
from tkinter import filedialog
import tkcalendar as tkc
from button import HoverButton

#db connectivity
#View Buttons code

def AdminReportScreen (root):
    def view_date():
        view1.heading(1, text='Report ID')
        view1.heading(2, text='Patient ID')
        view1.heading(3, text='Patient Name')
        view1.heading(4, text='Name of the Report')
        view1.heading(5, text='Click here to view')

    def view_patient():

        view1.heading(1, text='Report ID')
        view1.heading(2, text='Date')
        view1.heading(3, text='Patient Name')
        view1.heading(4, text='Name of the Report')
        view1.heading(5, text='Click here to view')


    # root=tk.Tk() #toplevel change
    window=tk.Toplevel(root)
    frame = tk.LabelFrame (window, padx=10, pady=10, bg="lightblue", text='Enter the details to view reports')
    frame.grid(row=0, column=0, sticky='news')
    frame1 = tk.LabelFrame (window, padx=10, pady=10, bg="white", text='View the Reports')
    frame1.grid(row=1, column=0, sticky='news')

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

    view1 = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5), show='headings', height='3')
    view1.grid(row=0,column=0, sticky='ew')

    pt_id=tk.IntVar()
    date_label=tk.Label(frame, text="Select the date: ")
    date_select=tkc.DateEntry(frame)
    date_label.grid(row=0, column =0)
    date_select.grid(row=0, column=1)
    submit = ttk.Button(frame, text='View', command=view_date) #onClick=sub(date,time)
    submit.grid(row=0, column=2)

    id_label=tk.Label(frame, text="Enter the Patient ID: ")
    id_select=tk.Entry(frame, width=30, textvariable=pt_id )
    id_label.grid(row=1, column =0)
    id_select.grid(row=1, column=1)
    submit = ttk.Button(frame, text='View Patient\'s Reports', command=view_patient) #onClick=sub(date,time)
    submit.grid(row=1, column=2)

    # window.mainloop()
    # delete()


    def reportViewScreen(root):
        # Function for opening the
        # file explorer window
        # window = tk.Tk()
        window = tk.Toplevel(root, )

        frame = tk.LabelFrame(window, text='You can only download the files here.', padx=10, pady=10,
                            font=("Verdana", 10), bg="#2C3A57", fg="red")
        frame.grid(row=0, column=0, sticky='news')

        def SaveFiles():
            filename = filedialog.asksaveasfilename(initialdir="/",
                                                    title="Save the file",
                                                    filetypes=(("Text files",
                                                                "*.pdf*"),
                                                            ("all files",
                                                                "*.*")))  # Get the file to be saved from the database.

            # Change label contents
            label_file_explorer.configure(text="File To be Saved: " + filename)

        # Create the root window

        # Set window title
        window.title('Save and View Reports')

        # Set window background color
        window.config(background="white")

        # Create a File Explorer label
        fnameLabel = tk.Label(frame, text='Patient ID: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
        fnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
        lnameLabel = tk.Label(frame, text='Date: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
        lnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")

        label_file_explorer = Label(frame,
                                    text="Click on search to save the file",
                                    width=100, height=4, justify="center",
                                    fg = "black", bg="#A3A3B1",font=("Verdana", 9))

        button_search = HoverButton(frame,
                            text="Search",font=("Bahnschrift", 9),activebackground='#00BE00',
                            command=SaveFiles)

        button_exit = HoverButton(frame,
                            text="Exit",font=("Bahnschrift", 9),activebackground='#00BE00', command='exit')

        # Grid method is chosen for placing
        # the widgets at respective positions
        # in a table like structure by
        # specifying rows and columns
        fnameLabel.grid(row=0, column=0)
        fnameBox.grid(row=0, column=1)
        lnameLabel.grid(row=1, column=0)
        lnameBox.grid(row=1, column=1)

        label_file_explorer.grid(column=0, row=3, columnspan=2)
        button_search.grid(column=0, row=4, columnspan=2)
        button_exit.grid(column=0, row=5, columnspan=2)

        window.rowconfigure(0, weight=1, minsize=500)
        window.columnconfigure(0, weight=1, minsize=700)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)
        frame.rowconfigure(5, weight=1)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Let the window wait for any events
        window.mainloop()
