#Import module
import tkinter as tk
from PIL import Image, ImageTk

#Create class
class AppInfo:
    #Create Window
    def __init__(self):
        self.app_info = tk.Tk()
        self.app_info.title("Covid Contact Tracing APP - App Info")
        self.app_info.geometry("1020x700")

        # Load the original background image
        self.image_path = "app_info_window.png"
        self.original_image = Image.open(self.image_path)

        # Create canvas
        self.canvas = tk.Canvas(self.app_info)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Set the initial background image
        self.update_background_image()

        # Bind the window resize event 
        self.app_info.bind("<Configure>", self.resize_image)

        #Call button methods
        self.covid_info_button()

        self.app_info_button()

        self.home_button()
        
        #run mainloop
        self.app_info.mainloop()

    #Updating background image
    def update_background_image(self):
        # Get the current size of the canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Resize the original image to fit the canvas size
        self.image = self.original_image.resize((canvas_width, canvas_height), Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(self.image)

        # Create the background image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background)


    def resize_image(self, event):
        # Update the background image when the window is resized
        self.update_background_image()

    # Add Buttons
    #Covid info button
    def covid_info_button(self):
            # Load the image for the button
            image = Image.open("covid_info.png")

            # Resize the image 
            new_width = 140
            new_height = 160
            resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

            # Create the PhotoImage from the resized image
            button_image = ImageTk.PhotoImage(resized_image)

            # Create the button with the resized image
            button = tk.Button(self.covid_info, image=button_image, borderwidth=0, command = self.open_covid_info_window)
            button.image = button_image 
            button.place(x=35, y=180)
    #Button for app info
    def app_info_button(self):
        # Load the image for the button
        image = Image.open("app_info.png")

        # Resize the image 
        new_width = 140
        new_height = 160
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.covid_info, image=button_image, borderwidth=0)
        button.image = button_image 
        button.place(x=35, y=370) 
    #Button for home
    def home_button(self):
        # Load the image for the button
        image = Image.open("home_button.png")

        # Resize the image 
        new_width = 130
        new_height = 130
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.covid_info, image=button_image, borderwidth=0, command = self.back_to_home)
        button.image = button_image 
        button.place(x=38, y=550) 
    #Opening app info window
    def open_covid_info_window(self):
        # Close the covid_info window
        self.app_info.destroy()

        # Open the app info window
        self.covid_info = CovidInfo()
    
    #Backing home
    def back_to_home (self):
        # Close the covid_info window
        self.app_info.destroy()

        # Open the app info window
        self.intro_window = IntroWindow()
#info = AppInfo()