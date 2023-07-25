#Import module
import tkinter as tk
from PIL import Image, ImageTk

#Create class
class LastWindow:
    #Create Window
    def __init__(self):
        self.last = tk.Tk()
        self.last.title("COVID Contact Tracing APP - Form Submitted")  
        self.last.geometry("1020x700")

    # Load the original background image
        self.image_path = "submitted_bg.png"
        self.original_image = Image.open(self.image_path)

        # Create canvas
        self.canvas = tk.Canvas(self.last)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Set the initial background image
        self.update_background_image()

        # Bind the window resize event 
        self.last.bind("<Configure>", self.resize_image)

        #Call the buttons
        self.covid_info_button()
        self.app_info_button()
        self.home_button()
        self.exit_button()

        #Run Mainloop
        self.last.mainloop()
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

    #Add buttons
    #Covid Info button
    def covid_info_button(self):
            # Load the image for the button
            image = Image.open("covid_info.png")

            # Resize the image 
            new_width = 150
            new_height = 150
            resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

            # Create the PhotoImage from the resized image
            button_image = ImageTk.PhotoImage(resized_image)

            # Create the button with the resized image
            button = tk.Button(self.last, image=button_image, borderwidth=0, command = self.open_covid_info_window)
            button.image = button_image 
            button.place(x=55, y=50)
    #Button for app info
    def app_info_button(self):
        # Load the image for the button
        image = Image.open("app_info.png")

        # Resize the image 
        new_width = 150
        new_height = 150
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.last, image=button_image, borderwidth=0, command=self.open_app_info_window)
        button.image = button_image 
        button.place(x=55, y=235) 
    #Button for home
    def home_button(self):
        # Load the image for the button
        image = Image.open("home_button.png")

        # Resize the image 
        new_width = 150
        new_height = 150
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.last, image=button_image, borderwidth=0, command = self.back_to_home)
        button.image = button_image 
        button.place(x=55, y=420) 
    #Button for exit
    def exit_button(self):
        # Load the image for the button
        image = Image.open("exit_button.png")

        # Resize the image 
        new_width = 200
        new_height = 70
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create the PhotoImage from the resized image
        button_image = ImageTk.PhotoImage(resized_image)

        # Create the button with the resized image
        button = tk.Button(self.last, image=button_image, borderwidth=0, command = self.quit_program)
        button.image = button_image 
        button.place(x=30, y=580) 

    #For button commands
        
    #Opening app info window
    def open_covid_info_window(self):
        # Close the covid_info window
        self.last.destroy()
        #Importing class
        from covid_info import CovidInfo
        # Open the app info window
        self.app_info = CovidInfo()

    #Opening app info window
    def open_app_info_window(self):
        # Close the covid_info window
        self.last.destroy()
        #Importing class
        from app_info import AppInfo
        # Open the app info window
        self.app_info = AppInfo()
    
    #Back to home
    def back_to_home (self):
        # Close the covid_info window
        self.last.destroy()
        #Importing class
        from intro import IntroWindow
        # Open the app info window
        self.intro_window = IntroWindow()

    #Quitting program
    def quit_program(self):
        # quit program
        self.last.destroy()

# Create an instance of the last window class(test)
last = LastWindow()
