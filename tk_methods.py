import tkinter as tk
class TkMethods:
    #Initializing main window
    def __init__ (self):
        self.main = tk.Tk() #Creating the application main window
        self.main.title("COVID Contact Tracing APP") #Main window title
        self.main.geometry("900x700") #Main window Size
    #Defining method for Name's data
    def name (self):
        label_name = tk.Label(self.main, text ="Name: ") #For the user's name
        label_name.grid(row = 1, column = 0, padx = 5, pady = 5)
        input_name = tk.Entry(self.main)		#For the user's name
        input_name.grid(row = 1, column = 1, padx = 5, pady = 5)
    #Defining method for Age's data
    def age (self):
        label_age = tk.Label(self.main, text ="Age: ") #For the user's age
        label_age.grid(row = 2, column = 0, padx = 5, pady = 5)
        input_age = tk.Entry(self.main)		#For the user's age
        input_age.grid(row = 2, column = 1, padx = 5, pady = 5)	
    #Defining method for Address' data
    def address (self):
        label_address = tk.Label(self.main, text ="Address: ") #For the user's address
        label_address.grid(row = 3, column = 0, padx = 5, pady = 5)
        input_address = tk.Entry(self.main)		#For the user's address
        input_address.grid(row = 3, column = 1, padx = 5, pady = 5)	
    #Defining method for Number's data
    def number (self):
        label_number = tk.Label(self.main, text ="Phone number: ") #For the user's phone number
        label_number.grid(row = 4, column = 0, padx = 5, pady = 5)
        input_number = tk.Entry(self.main)		#For the user's number
        input_number.grid(row = 4, column = 1, padx = 5, pady = 5)	



		
