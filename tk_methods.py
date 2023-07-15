import tkinter as tk
class TkMethods:
    def __init__ (self):
        self.main = tk.Tk() #Creating the application main window
        self.main.title("COVID Contact Tracing APP") #Main window title
        self.main.geometry("900x700") #Main window Size
    def name (self):
        label_name = tk.Label(self.main, text ="Name: ") #For the user's name
        label_name.grid(row = 1, column = 0, padx = 5, pady = 5)
        input_name = tk.Entry(self.main)		#For the user's name
        input_name.grid(row = 1, column = 1, padx = 5, pady = 5)

