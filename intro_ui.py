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
        button_open_form = tk.Button(self.intro, text ="Start Contact Tracing Form", bg = "plum1", fg="DarkOrchid4", font=("", 11, "bold"))
        button_open_form.grid(row = 3, column = 0, sticky ="news", padx=20, pady=20)
        button_open_form.config(width=15, height=2)

    #Add Image
    def intro_image(self):
        #Image frame
        self.image_frame = tk.LabelFrame(self.intro)
        self.image_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)      
        self.intro_logo = Image.open("Intro_logo.png")
        self.intro_logo = ImageTk.PhotoImage(self.intro_logo)
        self.logo_label = tk.Label(image = self.intro_logo)
        self.logo_label.image = self.intro_logo
        self.logo_label.grid(column=0, row=0)

    #Search Engine
    def search_engine (self):
        self.search_frame = tk.LabelFrame(self.intro, borderwidth=0, highlightthickness=0 )
        self.search_frame.grid(row= 0, column=1,sticky="news")
        #Searching button
        search_button = tk.Button(self.search_frame, text ="Search Entry", bg = "plum1", fg="DarkOrchid4", font=("", 11, "bold") )
        search_button.grid(row= 1, column=1, padx=10, pady=20)
        #Searching input field
        input_search = tk.Entry(self.search_frame, width = 50)
        input_search.grid(row=1, column=2, padx=20, pady=20)
    #COvid Info button(self)
    def covid_info (self):
        #Covid info
        covid_info_button=tk.Button(self.search_frame, text="Covid-19 Info", bg = "plum1", fg="DarkOrchid4", font=("", 11, "bold"))
        covid_info_button.grid(row=0, column=1, sticky="w", padx=20, pady=20)
        
    #Displaying search result