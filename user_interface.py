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
        self.get_symptoms() #Calling symptoms data method
        self.exposure() #Calling exposure data method
        self.contact()  #Calling contact data method
        self.test()  #Calling COVID test data method
    #First Question (Vaccination status)
    def vaccination_status (self):
        label_vaccine = tk.Label(self.main, text ="Have you been vaccinated for COVID-19?") #Question label
        label_vaccine.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "w") #Position
        self.var = tk.StringVar()    #Initializing Variable    
        #Initializing options in a list
        vac_status = ["Not Yet", "1st Dose", "2nd Dode (Fully Vaccinated)", "1st Booster Shot", "2nd Booster Shot"]
        #Setting radiobuttons for the question
        for i in range (len(vac_status)):
            self.input_vaccine = tk.Radiobutton(self.main, text=vac_status[i], variable = self.var, value = vac_status[i]) 
            self.input_vaccine.grid(row = 9+i, column = 0, padx = 0, pady = 0, sticky = "w")	     
    #Second Question (Symptoms)
    def get_symptoms(self):
        label_vaccine = tk.Label(self.main, text="Are you experiencing any symptoms in the past 7 days such as:")
        label_vaccine.grid(row=14, column=0, padx=5, pady=5, sticky="w")
        
        #Initializing Symptoms option
        self.check_symptom = []
        options = ["Fever", "Cough", "Colds", "Sore Throat", "Headache", "Diarrhea", "Loss of taste or Smell", "None"]
        
        #Checking symptoms data 
        for i, option in enumerate(options):
            var = tk.StringVar()
            input_symptom = tk.Checkbutton(self.main, text=option, variable=var, onvalue = option, offvalue="", anchor = "w")
            input_symptom.grid(row=15 + (i // 2), column=i % 2, padx=0, pady=0, sticky="w")
            self.check_symptom.append(var)
    #Third Question (Exposure to a probable positive case)
    def exposure(self):
        label_exposure = tk.Label(self.main, text ="Have you had exposure to a probable or confirmed case in the last 14 days?")#Question label
        label_exposure.grid(row=21, column=0, padx=5, pady= 5, sticky="w") #Position
        self.ex_var = tk.StringVar()    #Initializing Variable    
        #Initializing options in a list
        ex_status = ["Yes", "No", "Uncertain"]
        #Setting radiobuttons for the question
        for i in range (len(ex_status)):
            self.input_exposure = tk.Radiobutton(self.main, text=ex_status[i], variable = self.ex_var, value = ex_status[i]) 
            self.input_exposure.grid(row = 22+i, column = 0, padx = 0, pady = 0, sticky = "w")
    #Fourth Question (Contact with someone with symptoms)
    def contact (self):
        label_contact = tk.Label(self.main, text="Have you had in contact with somebody with body pains\n"
                                         "headache, sore throat, fever, diarrhea, caugh, colds, shortness of breath,\n"
                                         "loss of taste or loss of smell in the past 7 days?",
                         justify="left")  #Question label
        label_contact.grid(row=24, column=0, padx=5, pady=5, sticky ="w") #Position
        self.contact_var = tk.StringVar() #Initializing Variable
        #Initializing options in a list
        contact_status = ["Yes", "No"]
        #Setting radiobuttons for the question
        for i in range (len(contact_status)):
            self.input_contact = tk.Radiobutton(self.main, text=contact_status[i], variable = self.contact_var, value = contact_status[i])
            self.input_contact.grid(row=25+i, column = 0, padx = 0, pady = 0, sticky ="w")
    #Fifth Question (If tested for COVID)
    def test (self):
        label_test = tk.Label(self.main, text="Have you been tested for COVID-19 in the last 14 days?") #Question label
        label_test.grid(row = 28, column =0, padx = 5, pady =5, sticky ="w") #Position
        self.test_var = tk.StringVar() #Initializing Variable
        #Initializing options in a list
        test_status = ["No", "Yes - Positive", "Yes - Negative", "Yes - Pending"]
        #Setting radiobuttons for the question
        for i in range (len(test_status)):
            self.input_test = tk.Radiobutton(self.main, text = test_status[i], variable = self.test_var, value = test_status[i]) 
            self.input_test.grid(row=29+i, column = 0, padx=0, pady=0, sticky ="w")