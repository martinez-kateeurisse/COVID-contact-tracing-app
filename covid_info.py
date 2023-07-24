#Import module
import tkinter as tk

#Create class
class CovidInfo:
    #Create Window
    def __init__(self):
        self.covid_info = tk.Tk()
        self.covid_info.title("COVID Contact Tracing APP - Covid-19 Info")  
        self.covid_info.geometry("1020x700")
        #Create canvas
        #Add Buttons
        #For button commands
        #run mainloop
        self.covid_info.mainloop()

info = CovidInfo()
