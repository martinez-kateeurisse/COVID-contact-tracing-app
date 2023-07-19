#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will serve as the main file for the form (second frame/window)

#Import Necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Import class
from form_user_interface import UserInterface

#Create class
class FormTk(UserInterface):
    def __init__(self):
        main = tk.Tk()
        main.title("COVID Contact Tracing APP") #Title
        main.geometry("820x700")  # Window Size

        # Creating a Canvas
        canvas = tk.Canvas(main)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adding a Scrollbar
        scrollbar = ttk.Scrollbar(main, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configuring the Canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Creating a Frame inside the Canvas
        self.frame = tk.Frame(canvas)

        # Adding the Frame to the Canvas
        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        
        # Updating the Canvas scrollregion
        canvas.update_idletasks()

        #Run mainloop
        main.mainloop()


