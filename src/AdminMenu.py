import tkinter as tk

root = tk.Tk()

frame = tk.Frame (root, padx=20, pady=20)
frame.grid(row=0, column=0, sticky='news')

intro = tk.Label (frame, text="Admin Menu", wraplength=800)
viewapp = tk.Button (frame, text="View Appointments")
editapp = tk.Button (frame, text="Edit Appointments")
addreports = tk.Button (frame, text="Add and View Reports")

intro.grid(row=0, column=0)
viewapp.grid(row=1, column=0)
editapp.grid(row=2, column=0)
addreports.grid(row=3, column=0)

root.rowconfigure (0, weight=1, minsize=600)
root.columnconfigure (0, weight=1, minsize=800)

frame.rowconfigure (0, weight=1)
frame.rowconfigure (1, weight=1)
frame.rowconfigure (2, weight=1)
frame.rowconfigure (3, weight=1)
# frame.rowconfigure (4, weight=1)
# frame.rowconfigure (5, weight=1)
# frame.rowconfigure (6, weight=2)
frame.columnconfigure (0, weight=1)
# frame.columnconfigure (1, weight=1)

root.mainloop()