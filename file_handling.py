#This python file will serve as the data handling file

#Import modules
import csv
from form_user_interface import UserInterface

#Create class
class FileHandling(UserInterface):  
    #Open csv file and append data
    def storage_file(self,csv_file, data):
        with open(csv_file, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    
    #Saving submitted data
    def submit_data(self):
        # Retrieve user input data
        self.last_name = self.input_last_name.get()
        self.first_name = self.input_first_name.get()
        self.middle_name = self.input_middle_name.get()
        self.age = self.age_spinbox.get()
        self.gender = self.gender_combobox.get()
        self.street_address = self.input_street_address.get()
        self.city_address = self.input_city_address.get()
        self.state_address = self.input_state_address.get()
        self.country_address = self.input_country_address.get()
        self.postal_code = self.input_postal_code.get()
        self.phone_number = self.input_phone_number.get()
        self.email = self.input_email.get()
        self.contact_person = self.input_contact_person.get()
        self.contperson_num = self.input_contperson_num.get()
        self.contperson_rel = self.input_contperson_rel.get()
        self.contperson_email = self.input_contperson_email.get()

        # Create a list with the user input data
        data_to_add = [self.last_name, self.first_name, self.middle_name, self.age, self.gender,
                       self.street_address, self.city_address, self.state_address, self.country_address, self.postal_code,
                       self.phone_number, self.email, self.contact_person, self.contperson_num, self.contperson_rel, self.contperson_email]

        # Replace 'file.csv' with the path to your CSV file
        csv_file = 'data_file.csv'

        # Call the function to add data to the CSV file
        self.storage_file(csv_file, data_to_add) 