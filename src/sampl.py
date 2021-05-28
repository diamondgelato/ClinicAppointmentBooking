import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
from button import HoverButton

# Either in start we should not ask for patient ID  OR
# remove patient id from Treeview

window = tk.Tk()
# window = tk.Toplevel(root, )

frame = tk.LabelFrame(window, text='Appointments', padx=10, pady=10,
                      font=("Verdana", 10), bg="#2C3A57", fg="red")
frame.grid(row=0, column=0, sticky='news')

# Create the root window

# Set window title
window.title('Save and View Reports')

# Set window background color
window.config(background="white")

def result():

    treev["columns"] = ("1", "2", "3", "4")

# Defining heading
    treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
    treev.column("1", width=90, anchor='c')
    treev.column("2", width=150, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=150, anchor='c')

# Assigning the heading names to the
# respective columns
    treev.heading("1", text="Id")
    treev.heading("2", text="Name of Patient")
    treev.heading("3", text="Reference Doctor")
    treev.heading("4", text="Purpose of Appointment")

# Inserting the items and their features to the
# columns built
    treev.insert("", 'end', text="L1",
                values=("7", "Sam", "Dr.Mihir Pandya", "Back-ache"))
    treev.insert("", 'end', text="L2",
                values=("9", "Rob", "Dr.Vani Kamani", "knee-pain"))
    treev.insert("", 'end', text="L3",
                values=("12", "Steve", "Dr.Mugdha Kurkure", "throat burn"))

    treev.grid(row=4, column=0)

fnameLabel = tk.Label(frame, text='Patient ID: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
fnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
lnameLabel = tk.Label(frame, text='Date: ', font=("Verdana", 9), bg="#2C3A57", fg="white")
lnameBox = tk.Entry(frame, width=30, bg="#A3A3B1")
button_search = HoverButton(frame,
                            text="Search", font=("Bahnschrift", 9), activebackground='#00BE00',
                            command=result)
button_exit = HoverButton(frame,
                          text="Exit", font=("Bahnschrift", 9), activebackground='#00BE00', command='exit')

# Using treeview widget
treev = ttk.Treeview(window, selectmode='browse')


# Constructing vertical scrollbar
# with treeview
'''
verscrlbar = ttk.Scrollbar(window,
                           orient="vertical",
                           command=treev.yview)

# Calling pack method w.r.t verical scrollbar
verscrlbar.pack(side='right', fill='x')

# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)
'''
# Defining number of columns


fnameLabel.grid(row=0, column=0)
fnameBox.grid(row=0, column=1)
lnameLabel.grid(row=1, column=0)
lnameBox.grid(row=1, column=1)
button_search.grid(column=0, row=2, columnspan=2)
button_exit.grid(column=0, row=3, columnspan=2)

window.rowconfigure(0, weight=1, minsize=400)
window.columnconfigure(0, weight=1, minsize=700)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)
frame.rowconfigure(5, weight=1)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

window.mainloop()
