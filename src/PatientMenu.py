import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = tk.Frame (root, padx=20, pady=20)
frame.grid(row=0, column=0, sticky='news')

intro = tk.Label (frame, text="Patient Menu", wraplength=800)
bookapp = ttk.Button (frame, text="Book Appointments", width=20)
viewreports = ttk.Button (frame, text="View Reports", width=20)

intro.grid(row=0, column=0)
bookapp.grid(row=1, column=0)
viewreports.grid(row=2, column=0)

root.rowconfigure (0, weight=1, minsize=600)
root.columnconfigure (0, weight=1, minsize=800)

frame.rowconfigure (0, weight=1)
frame.rowconfigure (1, weight=1)
frame.rowconfigure (2, weight=1)
frame.columnconfigure (0, weight=1)

root.mainloop()