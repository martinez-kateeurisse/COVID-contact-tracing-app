import tkinter as tk
class TkMethods:
    #Defining main window
    def main_window (self):
        self.main = tk.Tk() #Creating the application main window
        self.main.title("COVID Contact Tracing APP") #Main window title
        self.main.geometry("900x700") #Main window Size
    #Defining Buttons
    def submit_button (self):
        button_submit = tk.Button(self.main, text="Submit", command = self.save_inputs())
        button_submit.grid(row=5, column=1, padx=10, pady=10)