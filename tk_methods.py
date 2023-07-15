import tkinter as tk
from file_handling import FileHandling
class TkMethods(FileHandling):
    #Defining main window
    def main_window (self):
        self.main = tk.Tk() #Creating the application main window
        self.main.title("COVID Contact Tracing APP") #Main window title
        self.main.geometry("700x500") #Main window Size
        window_title = tk.Label(self.main, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.main['bg']) #Window Title
        window_title.grid(row=0, column=0, columnspan=3, sticky='ew', padx=10)                      
    #Defining Buttons
    def submit_button (self):
        button_submit = tk.Button(self.main, text="Submit", command = self.save_inputs)
        button_submit.grid(row=15, column=1, padx=10, pady=10)
    def save_inputs(self):
        txt = FileHandling()
        txt.save_inputs(self.input_name.get(), self.input_age.get(), self.input_address.get(), self.input_number.get())
        txt.storage_file()