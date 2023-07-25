#Import module
import tkinter as tk
from PIL import Image, ImageTk

#Create class
class LastWindow:
    #Create Window
    def __init__(self):
        self.last = tk.Tk()
        self.last.title("COVID Contact Tracing APP - Form Submitted")  
        self.last.geometry("1020x700")
    #Create Canvas
    #Add buttons
    #For button commands
    #Run Mainloop
        self.last.mainloop()
# Create an instance of the last window class(test)
last = LastWindow()
