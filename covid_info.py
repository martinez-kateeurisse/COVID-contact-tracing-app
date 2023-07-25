#Import module
import tkinter as tk
from intro_ui import IntroUserInterface
from PIL import Image, ImageTk
#Create class
class CovidInfo:
    def __init__(self):
        self.covid_info = tk.Tk()
        self.covid_info.title("COVID Contact Tracing APP - Covid-19 Info")  
        self.covid_info.geometry("1020x700")
        
        # Create canvas
        self.canvas = tk.Canvas(self.covid_info)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Load and set the background image
        self.image_path = "covid_info_bg.png"
        self.image = Image.open(self.image_path)
        self.background = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background)
        
        # Bind the window resize event 
        self.covid_info.bind("<Configure>", self.resize_image)

        # Add Buttons
        
        # Run the main loop
        self.covid_info.mainloop()

    def resize_image(self, event):
        # Resize the image according to the window size
        new_width = event.width
        new_height = event.height
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background)

# Create an instance of the CovidInfo class(test)
info = CovidInfo()
