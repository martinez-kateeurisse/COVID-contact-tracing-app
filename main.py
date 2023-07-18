#This will serve as the main file of the program in which the methods will be called

from tkinter import *
import tkinter as tk

#Import class
from user_interface import UserInterface

#Initialize class
ui = UserInterface()

#Calling the main window method
ui.main_window()

info_frame = (ui.personal_info(), ui.health_info(), ui.submit_button())
#For adding scrollbar to the window

def on_scroll(*args):
    text.yview(*args)
    scrollbar.set(*args)

# Create the text widget
text = tk.Text(ui.main, wrap=tk.WORD)
text.grid(row=0, column=0, sticky="nsew")

# Create the vertical scrollbar
scrollbar = tk.Scrollbar(ui.main, orient="vertical", command=on_scroll)
scrollbar.grid(row=0, column=1, sticky="ns")

# Configure grid weights to make the widgets resize properly
ui.main.grid_rowconfigure(0, weight=1)
ui.main.grid_columnconfigure(0, weight=1)

text.insert("1.0", info_frame)

#Running the mainloop
ui.main.mainloop()