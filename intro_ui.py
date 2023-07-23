#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will have the codes for introduction user interface

#Import modules
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Create Class
class IntroUserInterface:
    #Button for entering form window
    def open_form(self):
        button_open_form = tk.Button(self.intro, text ="Start Contact Tracing Form", bg = "plum1", fg="DarkOrchid4")
        button_open_form.grid(row = 3, column = 0, sticky ="news", padx=20, pady=20)

    #Search Engine
    #Displaying search result