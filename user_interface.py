import tkinter as tk
from tk_methods import TkMethods

class UserInterface(TkMethods):
    #Personal Info section
    def personal_info (self):
        self.section1_title = tk.Label(self.main, text="Personal Information", font=("Courier 10 pitch", 12), bg=self.main['bg']) #Section Title
        self.section1_title.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10)     
        #Defining method for Name's data
        def name (self):
            label_name = tk.Label(self.main, text ="Name: ") #For the user's name
            label_name.grid(row = 2, column = 0, padx = 5, pady = 5)
            self.input_name = tk.Entry(self.main)		#For the user's name
            self.input_name.grid(row = 2, column = 1, padx = 5, pady = 5)
        #Defining method for Age's data
        def age (self):
            label_age = tk.Label(self.main, text ="Age: ") #For the user's age
            label_age.grid(row = 3, column = 0, padx = 5, pady = 5)
            self.input_age = tk.Entry(self.main)		#For the user's age
            self.input_age.grid(row = 3, column = 1, padx = 5, pady = 5)	
        #Defining method for Address' data
        def address (self):
            label_address = tk.Label(self.main, text ="Address: ") #For the user's address
            label_address.grid(row = 4, column = 0, padx = 5, pady = 5)
            self.input_address = tk.Entry(self.main)		#For the user's address
            self.input_address.grid(row = 4, column = 1, padx = 5, pady = 5)	
        #Defining method for Number's data
        def number (self):
            label_number = tk.Label(self.main, text ="Phone number: ") #For the user's phone number
            label_number.grid(row = 5, column = 0, padx = 5, pady = 5)
            self.input_number = tk.Entry(self.main)		#For the user's number
            self.input_number.grid(row = 5, column = 1, padx = 5, pady = 5)	
        name(self)
        age(self)
        address(self)
        number(self)
    #Health Declaration section
    def health_info (self):
        self.section1_title = tk.Label(self.main, text="Health Declaration", font=("Courier 10 pitch", 12), bg=self.main['bg']) #Section Title
        self.section1_title.grid(row=7, column=0, columnspan=3, sticky='ew', padx=10)
        self.vaccination_status() #Calling vaccination status method
        self.symptoms() #Calling symptoms data method
    #First Question (Vaccination status)
    def vaccination_status (self):
        label_vaccine = tk.Label(self.main, text ="Have you been vaccinated for COVID-19?") #Question label
        label_vaccine.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "w") #Position
        self.var = tk.StringVar()    #Initializing Variable    
        #Initializing options in a list
        status = ["Not Yet", "1st Dose", "2nd Dode (Fully Vaccinated)", "1st Booster Shot", "2nd Booster Shot"]
        #Setting radiobuttons for the question
        for i in range (len(status)):
            self.input_vaccine = tk.Radiobutton(self.main, text=status[i], variable = self.var, value = status[i]) 
            self.input_vaccine.grid(row = 9+i, column = 0, padx = 0, pady = 0, sticky = "w")	     
    #Second Question (Symptoms)
    def symptoms(self):
        label_vaccine = tk.Label(self.main, text ="Are you experiencing any symptoms in the past 7 days such as:") #Question label
        label_vaccine.grid(row = 14, column = 0, padx = 5, pady = 5, sticky = "w") #Position
        #Initializing Symptoms option
        options = ["Fever", "Cough", "Colds", "Sore Throught", "Headache", "Diarrhea", "Loss of taste or Smell","None"]
        self.check = []
        #Checking symptoms data
        for i in range(len(options)):
            self.check.append(tk.BooleanVar())
            self.input_symptom = tk.Checkbutton(self.main, text = options[i], variable = options[i])
            self.input_symptom.grid(row = 15+i, column = 0, padx = 0, pady = 0, sticky = "w")