#This python file is for User-interface methods

#Importing modules
import tkinter as tk
from tk_methods import TkMethods

#class with inheritance
class UserInterface(TkMethods):
#Personal Info section
    def personal_info (self):
        self.section1_title = tk.Label(self.main, text="Personal Information", font=("Courier 10 pitch", 12), bg=self.main['bg']) #Section Title
        self.section1_title.pack(fill=tk.X, padx=10, pady=10)
        self.name()
        self.age()
        self.address()
        self.number()

    #Defining method for Name's data
    def name (self):
        frame = tk.Frame(self.main)
        frame.pack(fill=tk.X, padx=5, pady=5)

        label_name = tk.Label(frame, text="Name:")
        label_name.pack(side=tk.LEFT)

        self.input_name = tk.Entry(frame)
        self.input_name.pack(side=tk.LEFT)
    #Defining method for Age's data
    def age (self):
        frame = tk.Frame(self.main)
        frame.pack(fill=tk.X, padx=5, pady=5)

        label_age = tk.Label(frame, text="Age:")
        label_age.pack(side=tk.LEFT)

        self.input_age = tk.Entry(frame)
        self.input_age.pack(side=tk.LEFT)	
    #Defining method for Address' data
    def address (self):
        frame = tk.Frame(self.main)
        frame.pack(fill=tk.X, padx=5, pady=5)

        label_address = tk.Label(frame, text="Address:")
        label_address.pack(side=tk.LEFT)

        self.input_address = tk.Entry(frame)
        self.input_address.pack(side=tk.LEFT)	
    #Defining method for Number's data
    def number (self):
        frame = tk.Frame(self.main)
        frame.pack(fill=tk.X, padx=5, pady=5)

        label_number = tk.Label(frame, text="Phone number:")
        label_number.pack(side=tk.LEFT)

        self.input_number = tk.Entry(frame)
        self.input_number.pack(side=tk.LEFT)	

    #Health Declaration section
    def health_info (self):
        self.section1_title = tk.Label(self.main, text="Health Declaration", font=("Courier 10 pitch", 12), bg=self.main['bg']) #Section Title
        self.section1_title.pack(fill=tk.X, padx=10, pady=10)
        self.vaccination_status() #Calling vaccination status method
        self.get_symptoms() #Calling symptoms data method
        self.exposure() #Calling exposure data method
        self.contact()  #Calling contact data method
        self.test()  #Calling COVID test data method
    #First Question (Vaccination status)
    def vaccination_status (self):
        label_vaccine = tk.Label(self.main, text ="Have you been vaccinated for COVID-19?") #Question label
        label_vaccine.pack(anchor="w", padx=5, pady=5) #Position
        self.var = tk.StringVar()    #Initializing Variable    
        #Initializing options in a list
        vac_status = ["Not Yet", "1st Dose", "2nd Dode (Fully Vaccinated)", "1st Booster Shot", "2nd Booster Shot"]
        #Setting radiobuttons for the question
        for status in vac_status:
            input_vaccine = tk.Radiobutton(self.main, text=status, variable=self.var, value=status)
            input_vaccine.pack(anchor="w", padx=5, pady=2)	     
    #Second Question (Symptoms)
    def get_symptoms(self):
        label_vaccine = tk.Label(self.main, text="Are you experiencing any symptoms in the past 7 days such as:")
        label_vaccine.pack(anchor="w", padx=5, pady=5)#Position
        #Initializing Symptoms option
        self.check_symptom = []
        options = ["Fever", "Cough", "Colds", "Sore Throat", "Headache", "Diarrhea", "Loss of taste or Smell", "None"]
        
        #Checking symptoms data 
        for option in options:
            var = tk.StringVar()
            input_symptom = tk.Checkbutton(self.main, text=option, variable=var, onvalue=option, offvalue="", anchor="w")
            input_symptom.pack(anchor="w", padx=5, pady=2)
            self.check_symptom.append(var)
    #Third Question (Exposure to a probable positive case)
    def exposure(self):
        label_exposure = tk.Label(self.main, text ="Have you had exposure to a probable or confirmed case in the last 14 days?")#Question label
        label_exposure.pack(anchor="w", padx=5, pady=5) #Position
        self.ex_var = tk.StringVar()    #Initializing Variable    
        #Initializing options in a list
        ex_status = ["Yes", "No", "Uncertain"]
        #Setting radiobuttons for the question
        for status in ex_status:
            input_exposure = tk.Radiobutton(self.main, text=status, variable=self.ex_var, value=status)
            input_exposure.pack(anchor="w", padx=5, pady=2)

    #Fourth Question (Contact with someone with symptoms)
    def contact (self):
        label_contact = tk.Label(self.main, text="Have you had in contact with somebody with body pains\n"
                                         "headache, sore throat, fever, diarrhea, caugh, colds, shortness of breath,\n"
                                         "loss of taste or loss of smell in the past 7 days?",
                         justify="left")  #Question label
        label_contact.pack(anchor="w", padx=5, pady=5) #Position
        self.contact_var = tk.StringVar() #Initializing Variable
        #Initializing options in a list
        contact_status = ["Yes", "No"]
        #Setting radiobuttons for the question
        for status in contact_status:
            input_contact = tk.Radiobutton(self.main, text=status, variable=self.contact_var, value=status)
            input_contact.pack(anchor="w", padx=5, pady=2)

    #Fifth Question (If tested for COVID)
    def test (self):
        label_test = tk.Label(self.main, text="Have you been tested for COVID-19 in the last 14 days?") #Question label
        label_test.pack(anchor="w", padx=5, pady=5) #Position
        self.test_var = tk.StringVar() #Initializing Variable
        #Initializing options in a list
        test_status = ["No", "Yes - Positive", "Yes - Negative", "Yes - Pending"]
        #Setting radiobuttons for the question
        for status in test_status:
            input_test = tk.Radiobutton(self.main, text=status, variable=self.test_var, value=status)
            input_test.pack(anchor="w", padx=5, pady=2)
