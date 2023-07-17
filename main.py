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
app_frame = Frame(ui.main)
app_frame.pack(fill=BOTH, expand=1)

#Create a Canvas
app_canvas = Canvas(app_frame)
app_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#Add a Scrollbar to the canvas
app_scrollbar = ttk.Scrollbar(app_frame, orient = VERTICAL, command=app_canvas.yview)
app_scrollbar.pack(side=RIGHT, fill = Y)

#Configure the canvas
app_canvas.configure(yscrollcommand=app_scrollbar.set)
app_canvas.bind('<Configure>', lambda e: app_canvas.configure(scrollregion = app_canvas.bbox("all")))

#Create another frame inside the canvas
canvas_frame = Frame(app_canvas)

#Add the new frame to a window in the canvas
app_canvas.create_window((0,0), window = canvas_frame, anchor = "nw")

# Create widgets inside the canvas_frame
for frame in info_frame:
    frame.pack(in_=canvas_frame, padx=10, pady=10, fill=BOTH, expand=True)

# Update the scroll region of the canvas
app_canvas.update_idletasks()
app_canvas.configure(scrollregion=app_canvas.bbox("all"))

#Running the mainloop
ui.main.mainloop()