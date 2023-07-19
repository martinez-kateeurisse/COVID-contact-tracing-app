#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

#This python file will include the codes for user interface of the form

#Import Necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
        label_last_name = tk.Label(self.personal_info_frame, text="Last Name")
        label_last_name.grid(row=0, column=0)
        label_first_name = tk.Label(self.personal_info_frame, text="First Name")
        label_first_name.grid(row=0, column=1)
        label_middle_name = tk.Label(self.personal_info_frame, text="Middle Name")
        label_middle_name.grid(row=0, column=2)

        #Name entry fields
        input_last_name = tk.Entry(self.personal_info_frame)
        input_first_name = tk.Entry(self.personal_info_frame)
        input_middle_name = tk.Entry(self.personal_info_frame)
        input_last_name.grid(row=1, column=0, padx=5, pady=6) 
        input_first_name.grid(row=1, column=1, padx=5, pady=6) 
        input_middle_name.grid(row=1, column=2, padx=5, pady=6) 
    
    #Defining method for Age's data
    def age (self):
        #Age label, inputs(spinbox)
        label_age = tk.Label(self.personal_info_frame, text="Age")
        age_spinbox = tk.Spinbox(self.personal_info_frame, from_=1, to=120, width = 10)
        label_age.grid(row=0, column=3)
        age_spinbox.grid(row=1, column=3, padx =10, pady=5)
    
    #Defining method for Gender's data
    def gender(self):
        #Gender labels, inputs(combobox)
        label_gender = tk.Label(self.personal_info_frame, text="Gender")
        gender_combobox = ttk.Combobox(self.personal_info_frame, values = ["Male", "Female", "Other"], width=7)
        label_gender.grid(row=0, column = 4)
        gender_combobox.grid(row=1, column = 4,padx =10, pady=5)
    
    #Defining method for Address data
    def address(self):
        #Address labels
        address_title=tk.Label(self.personal_info_frame, text="Current Address:", font=("Tahoma", 10, "bold"))
        address_title.grid(row=2, column=0, sticky="w")
        label_street_address = tk.Label(self.personal_info_frame, text="Street/Blck/House No.")
        label_street_address.grid(row=3, column=0)
        label_city_address = tk.Label(self.personal_info_frame, text="City/Town")
        label_city_address.grid(row=3, column=1)
        label_state_address = tk.Label(self.personal_info_frame, text="State/Province")
        label_state_address.grid(row=3, column=2)
        label_country_address = tk.Label(self.personal_info_frame, text="Country")
        label_country_address.grid(row=3, column=3)
        label_postal_code = tk.Label(self.personal_info_frame, text="Postal Code")
        label_postal_code.grid(row=3, column=4)

        #Address entry fields
        input_street_address = tk.Entry(self.personal_info_frame)
        input_city_address = tk.Entry(self.personal_info_frame)
        input_state_address = tk.Entry(self.personal_info_frame)
        input_country_address = tk.Entry(self.personal_info_frame)
        input_postal_code = tk.Entry(self.personal_info_frame, width = 10)
        input_street_address.grid(row=4, column=0, padx=5, pady=5) 
        input_city_address.grid(row=4, column=1, padx=5, pady=5) 
        input_state_address.grid(row=4, column=2, padx=5, pady=5) 
        input_country_address.grid(row=4, column=3, padx=5, pady=5) 
        input_postal_code.grid(row=4, column=4, padx=5, pady=5)

    #Defining method for contact info's data
    def contact_info(self):
        #Contact Information Title
        contact_info_title=tk.Label(self.personal_info_frame, text="Contact Information:", font=("Tahoma", 10, "bold"))
        contact_info_title.grid(row=5, column=0, sticky="w")
        
        #Contact Information Labels
        label_phone_number = tk.Label(self.personal_info_frame, text="Phone Number")
        label_phone_number.grid(row=6, column=0)
        label_email = tk.Label(self.personal_info_frame, text="Email")
        label_email.grid(row=6, column=1)
        label_contact_person = tk.Label(self.personal_info_frame, text="Contact Person:")
        label_contact_person.grid(row=6, column=2)
        label_contperson_num = tk.Label(self.personal_info_frame, text="Phone Number:")
        label_contperson_num.grid(row=7, column=2)
        label_contperson_email = tk.Label(self.personal_info_frame, text="Email:")
        label_contperson_email.grid(row=8, column=2)
        label_contperson_rel = tk.Label(self.personal_info_frame, text="Relationship w/ Contact Person")
        label_contperson_rel.grid(row=8, column=0)
        
        #Contact Information entry fields
        input_phone_number = tk.Entry(self.personal_info_frame)
        input_email = tk.Entry(self.personal_info_frame)
        input_contact_person = tk.Entry(self.personal_info_frame, width = 30)
        input_contperson_num = tk.Entry(self.personal_info_frame)
        input_contperson_rel = tk.Entry(self.personal_info_frame)
        input_contperson_email = tk.Entry(self.personal_info_frame)
        input_phone_number.grid(row=7, column=0, padx=5, pady=5)
        input_email.grid(row=7, column=1, padx=5, pady=5)
        input_contact_person.grid(row=6, column=3, padx=5, pady=5)
        input_contperson_num.grid(row=7, column=3, padx=5, pady=5, sticky="w")
        input_contperson_rel.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        input_contperson_email.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    def personal_info_configure(self):
        for widget in self.personal_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)