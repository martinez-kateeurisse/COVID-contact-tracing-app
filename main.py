#This will serve as the main file of the program in which the methods will be called

from tkinter import *
from tkinter import ttk

#Import class
from user_interface import UserInterface

#Initialize class
ui = UserInterface()

#Calling the main window method
ui.main_window()

info_frame = (ui.personal_info(), ui.health_info(), ui.submit_button())
#For adding scrollbar to the window
    #Create a Main Frame
main_frame = Frame(ui.main)
main_frame.pack(fill=BOTH, expand=1)
    #Create a Canvas
    #Add a Scrollbar to the canvas
    #Configure the canvas
    #Create another frame inside the canvas
    #Add the new frame to a window in the canvas

#Calling the method for Pesonal info data
#ui.personal_info()
#Calling the method for Health Declaration data
#ui.health_info()

#Submit button for saving inputs
#ui.submit_button()

#Running the mainloop
ui.main.mainloop()