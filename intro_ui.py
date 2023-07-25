#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will have the codes for introduction user interface
#Import Necessary modules
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from form_tk import FormTk
#Create Class
class IntroUserInterface:
#Define instance variables
    def __init__(self, intro):
        self.intro = intro

    #Resizing the background image
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
        canvas.image = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image)
    
    #Creating the canvas with the bg image
    def canvas_background(self, image_path):
        global original_image
        global canvas

        # Create the canvas
        canvas = tk.Canvas(self.intro, width=500, height=400)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Load the background image
        original_image = Image.open(image_path)
        canvas.image = ImageTk.PhotoImage(original_image)

        # Place image on canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image)

        # Bind the resize_image 
        canvas.bind("<Configure>", self.resize_image)

    #Button for opening the form
    def open_form(self):
        button_open_form = tk.Button(self.intro, text="Start Contact Tracing Form", bg="plum1", fg="DarkOrchid4", font=("", 17, "bold"), command=self.open_form_window)
        button_open_form.place(x=46, y=500)
        button_open_form.config(width=30, height=3)
        
    #Button for covid info
    def covid_info_button(self):

        # Load the image for the button
        image = Image.open("covid_info.png")

        # Resize the image 
        new_width = 150
        new_height = 170
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.intro, image=button_image, borderwidth=0, command = self.open_covid_info_window)
        button.image = button_image 
        button.place(x=600, y=30) 
    
    #Button for app info
    def app_info_button(self):
        # Load the image for the button
        image = Image.open("app_info.png")

        # Resize the image 
        new_width = 150
        new_height = 170
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.intro, image=button_image, borderwidth=0, command = self.open_app_info_window)
        button.image = button_image 
        button.place(x=800, y=30) 

    #Search Engine Entry field
    def search_entry(self):
        search_entry = tk.Entry(self.intro, font=("Constantia", 18),width=30,)
        search_entry.place(x=550, y=250)
        self.search_results_listbox = tk.Listbox(self.intro,bg="thistle1", font=("Constantia", 11), width=45, height=13)
        self.search_results_listbox.place(x=590, y=350)
        return search_entry
    def search_button(self):
        # Load the image for the button
        image = Image.open("search_button.png")

        # Resize the image 
        new_width = 150
        new_height = 37
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.intro, image=button_image, borderwidth=0, command=self.search_data)
        button.image = button_image 
        button.place(x=850, y=248) 

    #For Opening windows
    
    #Form window
    def open_form_window(self):
        # Close the introduction window
        self.intro.destroy()

        # Create and open the form window
        self.form_window = FormTk()
    
    #Opening covid info window
    def open_covid_info_window(self):
        # Close the covid_info window
        self.intro.destroy()

        # Open the app info window
        self.covid_info = CovidInfo()
    
    #Opening app info window
    def open_app_info_window(self):
        # Close the covid_info window
        self.intro.destroy()

        # Open the app info window
        self.app_info = AppInfo()
