import tkinter as tk
from file_handling import FileHandling
from tkinter import ttk

class TkMethods(FileHandling):
    #Defining first window
    def first_window (self):
        self.main = tk.Tk() #Creating the application main window
        self.main.title("COVID Contact Tracing APP") #Main window title
        self.main.geometry("700x700") #Main window Size
        self.main.columnconfigure(0, weight=1)
        window_title = tk.Label(self.main, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.main['bg']) #Window Title
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10) 
    
    #Defining the second window
    def second_window (self):
        self.second = tk.Tk()
        self.second.title("COVID Contact Tracing APP - Personal Information")
        self.second.geometry("700x700")
        self.second.columnconfigure(0, weight=1)
        window_title = tk.Label(self.second, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.second['bg']) 
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10)
    
    #Defining the third window
    def third_window (self):
        self.third = tk.Tk()
        self.third.title("COVID Contact Tracing APP - Health Declaration")
        self.third.geometry("700x700")
        self.third.columnconfigure(0, weight=1)
        window_title = tk.Label(self.third, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.third['bg']) 
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10) 

    #Defining Buttons
    def submit_button (self):
        button_submit = tk.Button(self.third, text="Submit", command = self.save_inputs)
        button_submit.grid(row=30, column=1, padx=10, pady=10)

    #Saving inputs
    def save_inputs(self):
        txt = FileHandling()
        user_symptoms = [option.get() for option in self.check_symptom]
        txt.save_inputs(self.input_name.get(), self.input_age.get(), self.input_address.get(), self.input_number.get(), self.var.get(), user_symptoms, self.ex_var.get(),
                        self.contact_var.get(), self.test_var.get())
        txt.storage_file()    