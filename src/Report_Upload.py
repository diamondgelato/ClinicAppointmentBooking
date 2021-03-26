# Python program to create
# a file explorer in Tkinter
# import all components
# from the tkinter library

#Doctor name dropdown menu

import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the
# file explorer window
window = tk.Tk()
frame = tk.LabelFrame(window, text='Please upload the reports in pdf format only.', padx=10, pady=10, bg="lightblue")
frame.grid(row=0, column=0, sticky='news')

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
                                                                                         
# Create the root window
  
# Set window title
window.title('Uploading Reports')
  
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
fnameLabel = tk.Label(frame, text='Patient ID: ')
fnameBox = ttk.Entry(frame, width=30)
lnameLabel = tk.Label(frame, text='Date: ')
lnameBox = ttk.Entry(frame, width=30)
unameLabel = tk.Label(frame, text='Name of the Report: ')
unameBox = ttk.Entry(frame, width=30)

label_file_explorer = Label(frame,
                            text = "Click on browse to upload the file here",
                            width = 100, height = 4,
                            fg = "white", justify= "center", bg="grey")
  
     
button_explore = Button(frame,
                        text = "Browse",
                        command = browseFiles) #tkinter.dnd can be used.
  
button_submit = Button(frame,
                     text = "Submit")
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
fnameLabel.grid(row=0, column=0)
fnameBox.grid(row=0, column=1)
lnameLabel.grid(row=1, column=0)
lnameBox.grid(row=1, column=1)
unameLabel.grid(row=2, column=0)
unameBox.grid(row=2, column=1)   
label_file_explorer.grid(column = 0, row = 4, columnspan=2)
button_explore.grid(column = 0, row = 5, columnspan=2)
button_submit.grid(column = 0,row = 6, columnspan=2)

window.rowconfigure (0, weight=1, minsize=500)
window.columnconfigure (0, weight=1, minsize=700)
frame.rowconfigure (0, weight=1)
frame.rowconfigure (1, weight=1)
frame.rowconfigure (2, weight=1)
frame.rowconfigure (3, weight=1)
frame.rowconfigure (4, weight=1)
frame.rowconfigure (5, weight=1)
frame.rowconfigure (6, weight=1)
frame.columnconfigure (0, weight=1)
frame.columnconfigure (1, weight=1)

# Let the window wait for any events
window.mainloop()