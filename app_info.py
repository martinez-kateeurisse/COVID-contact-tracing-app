#Import module
import tkinter as tk

#Create class
class AppInfo:
    #Create Window
    def __init__(self):
        self.app_info = tk.Tk()
        self.app_info.title("Covid Contact Tracing APP - App Info")
        self.app_info.geometry("1020x700")
        #Create canvas
        #Add Buttons
        #For button commands
        #run mainloop
        self.app_info.mainloop()

#info = AppInfo()