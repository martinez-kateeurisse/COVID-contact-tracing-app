#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will have the codes for introduction window

#Import necessary modules
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from intro_ui import IntroUserInterface
#Create class
class IntroWindow(IntroUserInterface):
#Create window
    def __init__(self):
        self.intro = tk.Tk()
        self.intro.title("COVID Contact Tracing APP") #Title
        self.intro.geometry("1020x700") #Window size
    #Create Canvas
        intro_canvas = tk.Canvas(self.intro)
        intro_canvas.grid(columnspan=2)
    
    # Creating a Frame inside the Canvas
        self.intro_frame = tk.Frame(intro_canvas)

    # Adding the Frame to the Canvas
        intro_canvas.create_window((0, 0), window=self.intro_frame, anchor="nw")
        
    #Call itroduction logo 
        self.intro_image()
    #Call open button
        self.open_form()
    #Call search engine label button
        self.search_engine()
    #Call Covid info button
        self.covid_info()
    #Run mainloop
        self.intro.mainloop()

#Call the class (test)
intro_gui = IntroWindow() 


