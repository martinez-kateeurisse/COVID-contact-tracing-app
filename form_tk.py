#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will serve as the main file for the form (second frame/window)

#Import Necessary modules
import tkinter as tk
from tkinter import ttk

#Import class
from file_handling import FileHandling

#Create class
class FormTk(FileHandling):
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("COVID Contact Tracing APP - Form") #Title
        self.main.geometry("1020x700")  # Window Size
        self.main.configure(bg="lavender")
        window_title = tk.Label(self.main, text="COVID CONTACT TRACING FORM", font=("Courier 10 pitch", 14, "bold"),fg="DarkOrchid4", bg="lavender") #Form Title
        window_title.pack(pady=10)
        
        # Creating a Canvas
        canvas = tk.Canvas(self.main)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adding a Scrollbar
        scrollbar = ttk.Scrollbar(self.main, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configuring the Canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Creating a Frame inside the Canvas
        self.frame = tk.Frame(canvas, bg ="lavender")

        # Adding the Frame to the Canvas
        canvas.create_window((0, 0), window=self.frame, anchor="nw")

        #Calling image method
        self.form_image()
        
        #Calling personal information method
        self.personal_info()

        #Calling health declaration method
        self.health_info()

        #Calling terms and condition method
        self.terms_and_condition()
        
        self.dos_and_donts()

        #Calling submit button method
        self.submit_button()
        
        # After setting up the GUI, update the Canvas scrollregion
        canvas.update_idletasks()
        
        #Run mainloop
        self.main.mainloop()
