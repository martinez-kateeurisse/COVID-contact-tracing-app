#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will include the codes for user interface of the form

#Import Necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

#Create Class
class UserInterface:
    #Saving Personal Information
    def personal_info(self):
        self.personal_info_frame = tk.LabelFrame(self.frame, text = "Personal Information\n", font=("", 11, "bold"))
        self.personal_info_frame.grid(row= 0, column=0, padx=10, pady=20)
        #Calling each info method
        self.name()
        self.age()
        self.gender()
        self.address()
        self.contact_info()
        self.personal_info_configure()
    #Defining method for Name's data
    def name (self):
        #Name labels
        self.label_last_name = tk.Label(self.personal_info_frame, text="Last Name")
        self.label_last_name.grid(row=0, column=0)
        self.label_first_name = tk.Label(self.personal_info_frame, text="First Name")
        self.label_first_name.grid(row=0, column=1)
        self.label_middle_name = tk.Label(self.personal_info_frame, text="Middle Name")
        self.label_middle_name.grid(row=0, column=2)

        #Name entry fields
        self.input_last_name = tk.Entry(self.personal_info_frame)
        self.input_first_name = tk.Entry(self.personal_info_frame)
        self.input_middle_name = tk.Entry(self.personal_info_frame)
        self.input_last_name.grid(row=1, column=0, padx=5, pady=6) 
        self.input_first_name.grid(row=1, column=1, padx=5, pady=6) 
        self.input_middle_name.grid(row=1, column=2, padx=5, pady=6) 
    
    #Defining method for Age's data
    def age (self):
        #Age label, inputs(spinbox)
        self.label_age = tk.Label(self.personal_info_frame, text="Age")
        self.age_spinbox = tk.Spinbox(self.personal_info_frame, from_=1, to=120, width = 10)
        self.label_age.grid(row=0, column=3)
        self.age_spinbox.grid(row=1, column=3, padx =10, pady=5)
    
    #Defining method for Gender's data
    def gender(self):
        #Gender labels, inputs(combobox)
        self.label_gender = tk.Label(self.personal_info_frame, text="Gender")
        self.gender_combobox = ttk.Combobox(self.personal_info_frame, values = ["Male", "Female", "Other"], width=7)
        self.label_gender.grid(row=0, column = 4)
        self.gender_combobox.grid(row=1, column = 4,padx =10, pady=5)
    
    #Defining method for Address data
    def address(self):
        #Address labels
        self.address_title=tk.Label(self.personal_info_frame, text="Current Address:", font=("Tahoma", 10, "bold"))
        self.address_title.grid(row=2, column=0, sticky="w")
        self.label_street_address = tk.Label(self.personal_info_frame, text="Street/Blck/House No.")
        self.label_street_address.grid(row=3, column=0)
        self.label_city_address = tk.Label(self.personal_info_frame, text="City/Town")
        self.label_city_address.grid(row=3, column=1)
        self.label_state_address = tk.Label(self.personal_info_frame, text="State/Province")
        self.label_state_address.grid(row=3, column=2)
        self.label_country_address = tk.Label(self.personal_info_frame, text="Country")
        self.label_country_address.grid(row=3, column=3)
        self.label_postal_code = tk.Label(self.personal_info_frame, text="Postal Code")
        self.label_postal_code.grid(row=3, column=4)

        #Address entry fields
        self.input_street_address = tk.Entry(self.personal_info_frame)
        self.input_city_address = tk.Entry(self.personal_info_frame)
        self.input_state_address = tk.Entry(self.personal_info_frame)
        self.input_country_address = tk.Entry(self.personal_info_frame)
        self.input_postal_code = tk.Entry(self.personal_info_frame, width = 10)
        self.input_street_address.grid(row=4, column=0, padx=5, pady=5) 
        self.input_city_address.grid(row=4, column=1, padx=5, pady=5) 
        self.input_state_address.grid(row=4, column=2, padx=5, pady=5) 
        self.input_country_address.grid(row=4, column=3, padx=5, pady=5) 
        self.input_postal_code.grid(row=4, column=4, padx=5, pady=5)

    #Defining method for contact info's data
    def contact_info(self):
        #Contact Information Title
        self.contact_info_title=tk.Label(self.personal_info_frame, text="Contact Information:", font=("Tahoma", 10, "bold"))
        self.contact_info_title.grid(row=5, column=0, sticky="w")
        
        #Contact Information Labels
        self.label_phone_number = tk.Label(self.personal_info_frame, text="Phone Number")
        self.label_phone_number.grid(row=6, column=0)
        self.label_email = tk.Label(self.personal_info_frame, text="Email")
        self.label_email.grid(row=6, column=1)
        self.label_contact_person = tk.Label(self.personal_info_frame, text="Contact Person:")
        self.label_contact_person.grid(row=6, column=2)
        self.label_contperson_num = tk.Label(self.personal_info_frame, text="Phone Number:")
        self.label_contperson_num.grid(row=7, column=2)
        self.label_contperson_email = tk.Label(self.personal_info_frame, text="Email:")
        self.label_contperson_email.grid(row=8, column=2)
        self.label_contperson_rel = tk.Label(self.personal_info_frame, text="Relationship w/ Contact Person")
        self.label_contperson_rel.grid(row=8, column=0)
        
        #Contact Information entry fields
        self.input_phone_number = tk.Entry(self.personal_info_frame)
        self.input_email = tk.Entry(self.personal_info_frame)
        self.input_contact_person = tk.Entry(self.personal_info_frame, width = 30)
        self.input_contperson_num = tk.Entry(self.personal_info_frame)
        self.input_contperson_rel = tk.Entry(self.personal_info_frame)
        self.input_contperson_email = tk.Entry(self.personal_info_frame, width = 30)
        self.input_phone_number.grid(row=7, column=0, padx=5, pady=5)
        self.input_email.grid(row=7, column=1, padx=5, pady=5)
        self.input_contact_person.grid(row=6, column=3, padx=5, pady=5)
        self.input_contperson_num.grid(row=7, column=3, padx=5, pady=5, sticky="w")
        self.input_contperson_rel.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        self.input_contperson_email.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    def personal_info_configure(self):
        for widget in self.personal_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
    
    #Saving Health Declaration
    def health_info(self):
        #Health Info Frame
        self.health_info_frame = tk.LabelFrame(self.frame, text = "Health Declaration\n", font=("", 11, "bold"))
        self.health_info_frame.grid(row= 1, column=0,sticky="news" ,padx=10, pady=10)
        
        #Calling info methods
        self.vaccine_status()
        self.symptoms()
        self.exposure()
        self.contact()
        self.test()

    #First Question (Vaccination Status)
    def vaccine_status(self):
        self.label_vaccine = tk.Label(self.health_info_frame, text ="Have you been vaccinated for COVID-19?") #Question label
        self.label_vaccine.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w") #Position
        self.var = tk.StringVar()    #Initializing Variable    
        
        #Initializing options in a list
        vac_status = ["Not Yet", "1st Dose", "2nd Dose (Fully Vaccinated)", "1st Booster Shot", "2nd Booster Shot"]
        
        #Setting radiobuttons for the question
        for i in range (len(vac_status)):
            self.input_vaccine = tk.Radiobutton(self.health_info_frame, text=vac_status[i], variable = self.var, value = vac_status[i]) 
            self.input_vaccine.grid(row = 1+i, column = 0, padx = 0, pady = 0, sticky = "w")	     
   
    #Second Question (Symptoms)
    def symptoms (self):
        self.label_symptoms = tk.Label(self.health_info_frame, text="Are you experiencing any symptoms in the past 7 days such as:")
        self.label_symptoms.grid(row=14, column=0, padx=5, pady=5, sticky="w")
                
        #Initializing Symptoms option
        self.check_symptom = []
        self.options = ["Fever", "Cough", "Colds", "Sore Throat", "Headache", "Diarrhea", "Loss of taste or Smell", "None"]
                
        #Checking symptoms data 
        for i, option in enumerate(self.options):
            var = tk.StringVar()
            input_symptom = tk.Checkbutton(self.health_info_frame, text=option, variable=var, onvalue = option, offvalue="", anchor = "w")
            input_symptom.grid(row=15 + (i // 2), column=i % 2, padx=0, pady=0, sticky="w")
            self.check_symptom.append(var)
    
    #Third Question (Exposure to a probable positive case)
    def exposure(self):
        self.label_exposure = tk.Label(self.health_info_frame, text ="Have you had exposure to a probable or confirmed case in the last 14 days?")#Question label
        self.label_exposure.grid(row=21, column=0, padx=5, pady= 5, sticky="w") #Position
        self.ex_var = tk.StringVar()    #Initializing Variable    
        
        #Initializing options in a list
        ex_status = ["Yes", "No", "Uncertain"]
        
        #Setting radiobuttons for the question
        for i in range (len(ex_status)):
            self.input_exposure = tk.Radiobutton(self.health_info_frame, text=ex_status[i], variable = self.ex_var, value = ex_status[i]) 
            self.input_exposure.grid(row = 22+i, column = 0, padx = 0, pady = 0, sticky = "w")

    #Fourth Question (Contact with someone with symptoms)
    def contact (self):
        self.label_contact = tk.Label(self.health_info_frame, text="Have you had in contact with somebody with body pains\n"
                                                "headache, sore throat, fever, diarrhea, caugh, colds, shortness of breath,\n"
                                                "loss of taste or loss of smell in the past 7 days?",
                                justify="left")  #Question label
        self.label_contact.grid(row=24, column=0, padx=5, pady=5, sticky ="w") #Position
        self.contact_var = tk.StringVar() #Initializing Variable
        
        #Initializing options in a list
        contact_status = ["Yes", "No"]
        
        #Setting radiobuttons for the question
        for i in range (len(contact_status)):
            input_contact = tk.Radiobutton(self.health_info_frame, text=contact_status[i], variable = self.contact_var, value = contact_status[i])
            input_contact.grid(row=25+i, column = 0, padx = 0, pady = 0, sticky ="w")
    
    #Fifth Question (If tested for COVID)
    def test (self):
        self.label_test = tk.Label(self.health_info_frame, text="Have you been tested for COVID-19 in the last 14 days?") #Question label
        self.label_test.grid(row = 28, column =0, padx = 5, pady =5, sticky ="w") #Position
        self.test_var = tk.StringVar() #Initializing Variable
        
        #Initializing options in a list
        test_status = ["No", "Yes - Positive", "Yes - Negative", "Yes - Pending"]
        
        #Setting radiobuttons for the question
        for i in range (len(test_status)):
            input_test = tk.Radiobutton(self.health_info_frame, text = test_status[i], variable = self.test_var, value = test_status[i]) 
            input_test.grid(row=29+i, column = 0, padx=0, pady=0, sticky ="w")

    #Do's and Dont's info
    def dos_and_donts(self):
        # Do's and Dont's Frame
        info_frame = tk.LabelFrame(self.frame, text="Do's and Don'ts\n", font=("", 11, "bold"))
        info_frame.grid(row=1, column=1, padx=0, pady=0, sticky="news")

        # Label to display the text from the file
        label_info = tk.Label(info_frame, text=self.show_info())  # Call the show_info() function
        label_info.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # Position

    #Showing do's and dont's info
    def show_info(self):
        # Opening and reading txt file
        with open("dos_and_donts.txt", "r") as file:
            dos_and_donts = file.read()
            return dos_and_donts
            
    #Accepting terms and condition
    def terms_and_condition (self):
        self.terms_frame = tk.LabelFrame(self.frame, text = "Terms and Condition\n", font=("", 11, "bold"))
        self.terms_frame.grid(row= 2, column=0,sticky="news" ,padx=10, pady=10)
        self.read_terms()
        self.terms_check()
    
    #Showing Terms and Conditions
    def show_terms(self):
        try:
            #Opening and reading txt file
            with open("terms_and_condition.txt", "r") as file:
                terms_and_condition = file.read()
                #Showing messagebox
                messagebox.showinfo("Text from File", terms_and_condition)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")
    
    #Button to read terms and condition
    def read_terms(self):
        read_button = tk.Button(self.terms_frame, text="Read Terms and Conditions here", command= self.show_terms)
        read_button.grid(row=0, column=0, padx=10, pady=10)       
    
    #Checkbutton for terms and condition
    def terms_check(self):
        #Checkbutton for terms and condition
        self.accept_terms = tk.StringVar(value = "Terms Not Accepted")
        self.terms_checkbutton = tk.Checkbutton(self.terms_frame, text="I've read and accept the terms and conditions.", 
                                           variable = self.accept_terms, onvalue="Terms Accepted" ,offvalue="Terms Not Accepted")
        self.terms_checkbutton.grid(row=0,column=1)

    #Submit button
    def submit_button (self):
        submit_button = tk.Button(self.frame, text="Submit", bg="gray", fg="white", command = self.submit_data)
        submit_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    
    #Logo image
    def form_image(self):
        #Image frame
        self.image_frame = tk.LabelFrame(self.frame)
        self.image_frame.grid(row=0, column=1, sticky="news", padx=10, pady=10)      
        #Original image
        original_image = Image.open("form_logo.png")
        #Resize Image
        resized_image = original_image.resize((150, 270))
        self.photo = ImageTk.PhotoImage(resized_image)
        # Create a Label to display the resized image
        image_label = tk.Label(self.image_frame, image=self.photo)
        image_label.grid(row=0, column=0, padx=10, pady=10)
    
    #Saving inputs
    def save_inputs(self):
        txt = self.FileHandling()
        user_symptoms = [option.get() for option in self.check_symptom]
        txt.save_inputs(self.input_last_name.get(),self.input_first_name.get(), self.input_middle_name.get(), self.input_age.get(), self.input_address.get(), self.input_number.get(), self.var.get(), user_symptoms, self.ex_var.get(),
                        self.contact_var.get(), self.test_var.get())
        txt.storage_file()

    #Opening last window
    def open_last_window(self):
        # Close the covid_info window
        self.main.destroy()
        #Importing class
        from last_window import LastWindow
        # Open the app info window
        self.last_window = LastWindow()