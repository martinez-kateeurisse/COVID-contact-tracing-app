#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will have the codes for introduction window

#Import necessary modules
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Create class
class IntroWindow:
#Create window
    def __init__(self):
        intro = tk.Tk()
        intro.title("COVID Contact Tracing APP") #Title
        intro.geometry("1020x700") #Window size
    #Create Canvas
        intro_canvas = tk.Canvas(intro)
        intro_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    #Add Image

    #Run mainloop
        intro.mainloop()

#Call the class (test)
intro_gui = IntroWindow()