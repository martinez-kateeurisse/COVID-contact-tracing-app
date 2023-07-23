#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will have the codes for introduction user interface
#Import Necessary modules
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage

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