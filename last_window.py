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
    #For button commands

# Create an instance of the last window class(test)
last = LastWindow()
