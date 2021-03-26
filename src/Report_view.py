# Importing tkinter to make gui in python
from tkinter import Tk
  
# Importing tkPDFViewer to place pdf file in gui.
# In tkPDFViewer library there is
# an tkPDFViewer module. That I have imported as pdf
from tkPDFViewer import tkPDFViewer as pdf
  
# Initializing tk
root = Tk()
  
# Set the width and height of our root window.
root.geometry("550x750")
  
# creating object of ShowPdf from tkPDFViewer.
v1 = pdf.ShowPdf()
  
# Adding pdf location and width and height.
v2 = v1.pdf_view(root,
                 pdf_location = "C:\\Users\\Vani\\Downloads\\10_AOAC_2USU112_Mobile_App_Development.doc", width = 50, height = 100, bar="true")
  
# Placing Pdf in my gui.
v2.pack()
root.mainloop()