# Python program to create
# a file explorer in Tkinter
# import all components
# from the tkinter library

#Doctor name dropdown menu

import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
from button import HoverButton
  
# import filedialog module
from tkinter import filedialog
  
def reportUploadScreen (root):
    # Function for opening the
    # file explorer window
    # window = tk.Tk()
    window = tk.Toplevel (root)
    frame = tk.LabelFrame(window, text='Please upload the reports in pdf format only.', padx=10, pady=10,
                          font=("Verdana", 10), bg="#2C3A57",  fg = "red")

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
        button_submit = Button(frame,
                        text = "Submit", command=sub)
        button_submit.grid(column = 0,row = 4, columnspan=2)
                                                                                            
    # Create the root window
    
    # Set window title
    def sub():
        if(report_var.get()!="" and patient_id_var.get()!=0):
            report=report_var.get()
            p_id=patient_id_var.get()
            p_id=str(p_id)
            var1= "Patient ID: "+p_id +"\nName of the report: "+report
            msg=tk.messagebox.askquestion("Are you sure?", var1 );
            #if(msg=="yes"):
            #db connectivity
        else:
            var2="Please fill in the details"
            msg1=tk.messagebox.showerror("ERROR", var2)
            


            

    window.title('Uploading Reports')
    
    
    #Set window background color
    window.config(background = "white")
    patient_id_var=tk.IntVar()
    report_var=tk.StringVar()

    # Create a File Explorer label
    fnameLabel = tk.Label(frame, text='Patient ID: ',font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    fnameBox = tk.Entry(frame, width=30, bg = "#A3A3B1")
    lnameLabel = tk.Label(frame, text='Date: ', font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    lnameBox = tk.Entry(frame, width=30, bg = "#A3A3B1")
    unameLabel = tk.Label(frame, text='Name of the Report: ', font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    unameBox = tk.Entry(frame, width=30, bg = "#A3A3B1")

    label_file_explorer = Label(frame,
                                text = "Click on browse to upload the file here",
                                width = 100, height = 4,
                                fg = "black", justify= "center", bg="#A3A3B1",font=("Verdana", 9))
    
        
    button_explore = HoverButton(frame,
                            text = "Browse", font=("Bahnschrift", 9),activebackground='#00BE00',
                            command = browseFiles) #tkinter.dnd can be used.
    
    button_submit = HoverButton(frame, activebackground='#00BE00', font=("Bahnschrift", 9),
                        text = "Submit")
    
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    fnameLabel.grid(row=0, column=0)
    fnameBox.grid(row=0, column=1)
    # lnameLabel.grid(row=1, column=0)
    # lnameBox.grid(row=1, column=1)
    unameLabel.grid(row=1, column=0)
    unameBox.grid(row=1, column=1)   
    label_file_explorer.grid(column = 0, row = 2, columnspan=2)
    button_explore.grid(column = 0, row = 3, columnspan=2)
    

    window.rowconfigure (0, weight=1, minsize=500)
    window.columnconfigure (0, weight=1, minsize=700)
    
    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.rowconfigure (4, weight=1)
    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)

    # Let the window wait for any events
    window.mainloop()
root=tk.Tk()
reportUploadScreen(root)