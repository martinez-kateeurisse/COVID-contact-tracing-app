#This python file will include tkinter methods such as creating window and buttons

import tkinter as tk
from file_handling import FileHandling
from tkinter import ttk

class TkMethods(FileHandling):
    #Defining main window
    def main_window (self):
        self.main = tk.Tk() #Creating the application main window
        self.main.title("COVID Contact Tracing APP") #Main window title
        self.main.geometry("700x700") #Main window Size
        self.main.columnconfigure(0, weight=1)
        window_title = tk.Label(self.main, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.main['bg']) #Window Title
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10) 
    
    #Next button from personal info to health declaration
    def personal_info_next (self):
        button_pi_next = tk.Button(self.main, text="Next", command=self.open_health_info)
        button_pi_next.grid(row=6, column=0, columnspan=2, pady=10)
    #Defining Buttons
    def submit_button (self):
        button_submit = tk.Button(self.main, text="Submit", command = self.save_inputs)
        button_submit.grid(row=30, column=1, padx=10, pady=10)
    #Saving inputs
    def save_inputs(self):
        txt = FileHandling()
        user_symptoms = [option.get() for option in self.check_symptom]
        txt.save_inputs(self.input_name.get(), self.input_age.get(), self.input_address.get(), self.input_number.get(), self.var.get(), user_symptoms, self.ex_var.get(),
                        self.contact_var.get(), self.test_var.get())
        txt.storage_file()