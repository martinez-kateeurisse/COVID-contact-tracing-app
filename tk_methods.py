import tkinter as tk
from file_handling import FileHandling

#Create class
class TkMethods(FileHandling):
    def first_window(self):
        self.first = tk.Tk()  # Creating the application main window
        self.first.title("COVID Contact Tracing APP")  # Main window title
        self.first.geometry("700x700")  # Main window Size
        self.first.columnconfigure(0, weight=1)
        window_title = tk.Label(self.first, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.first['bg'])  # Window Title
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10)

        button_start = tk.Button(self.first, text = "Start Survey", command = self.open_second_window)
        button_start.grid(row=6, column=0, columnspan=2, pady=10)

    #Opening second window
    def open_second_window(self):
        self.first.destroy()
    
    #Second Window
    def second_window(self):
        self.second = tk.Tk()
        self.second.title("COVID Contact Tracing APP - Personal Information")
        self.second.geometry("700x700")
        self.second.columnconfigure(0, weight=1)
        window_title = tk.Label(self.second, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.second['bg'])
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10)
        self.personal_info()
        button_next = tk.Button(self.second, text = "Next", command = self.open_third_window)
        button_next.grid(row=6, column=0, columnspan=2, pady=10)

    #Opening Third window
    def open_third_window(self):
        self.personal_inputs()
        self.second.destroy()
    
    #Third window
    def third_window(self):
        self.third = tk.Tk()
        self.third.title("COVID Contact Tracing APP - Health Declaration")
        self.third.geometry("700x700")
        self.third.columnconfigure(0, weight=1)
        window_title = tk.Label(self.third, text="COVID Contact Tracing APP", font=("Courier 10 pitch", 14), bg=self.third['bg'])
        window_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=10)
        self.health_info()
        button_submit = tk.Button(self.third, text = "Submit", command = self.health_inputs)
        button_submit.grid(row=6, column=0, columnspan=2, pady=10)

        button_quit = tk.Button(self.third, text = "Quit", command = self.quit_window)
        button_quit.grid(row=7, column=0, columnspan=2, pady=10)

    #Exiting the app/window
    def quit_window(self, user_data_from_second, user_data_from_third):
        # Save the input data to a text file
        self.save_inputs(user_data_from_second, user_data_from_third)

        self.third.destroy()
    
    # Saving inputs
    def personal_inputs(self):
        self.personal_inputs(self.input_name.get(), self.input_age.get(), self.input_address.get(), self.input_number.get())
        self.storage_file() 
    def health_inputs(self):  
        user_symptoms = [option.get() for option in self.check_symptom]
        self.save_inputs(self.var.get(), user_symptoms, self.ex_var.get(), self.contact_var.get(), self.test_var.get())
        self.storage_file() 
    
    def save_inputs(self):
        self.save_inputs(self.personal_inputs, self.health_inputs)