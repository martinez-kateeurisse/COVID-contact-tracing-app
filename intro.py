#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will have the codes for introduction window

# Import necessary modules
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from intro_ui import IntroUserInterface
from file_handling import FileHandling
# Create class
class IntroWindow(FileHandling, IntroUserInterface):
    # Create window
    def __init__(self):
        self.intro = tk.Tk()
        self.intro.title("COVID Contact Tracing APP")
        self.intro.geometry("1020x700")

        #Adding background image
        image_path = "intro_bg.png"

        # Calling the __init__ method 
        super().__init__(self.intro)
        
        #Calling the canvas with the background image
        self.canvas_background(image_path)

        #Calling form opening button
        self.open_form()

        #Calling covid info button
        self.covid_info_button()

        #Calling covid info button
        self.app_info_button()

        #Calling search entry
        self.search_entry_widget = self.search_entry()

        #Calling search button
        self.search_button()

        # Run mainloop
        self.intro.mainloop()





